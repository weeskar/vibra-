from flask import Blueprint, render_template, session, redirect, url_for
from vibra.models import Usuario, Conexion
from vibra.utils import es_match_mutuo
from vibra.demo_data import PERFILES_PRUEBA
from vibra import db

match_bp = Blueprint('match', __name__)

@match_bp.route('/match')
def match():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))
    usr = Usuario.query.get(session['usuario_id'])
    p = usr.perfil
    conectados_ids = [c.conectado_a_id for c in Conexion.query.filter_by(usuario_id=usr.id).all()]
    total_usuarios = Usuario.query.count()
    candidatos = []

    if total_usuarios <= 1:
        for perfil in PERFILES_PRUEBA:
            if perfil['nombre'] == usr.nombre:
                continue
            if perfil.get('pais','').lower() != (p.pais or '').lower():
                continue
            if p.orientacion == 'hetero' and perfil['genero'] == p.genero:
                continue
            if p.orientacion == 'homo' and perfil['genero'] != p.genero:
                continue
            candidatos.append(perfil)
    else:
        otros_usuarios = Usuario.query.filter(Usuario.id != usr.id).all()
        for otro in otros_usuarios:
            perf = otro.perfil
            if not perf:
                continue
            if (perf.pais or '').lower() != (p.pais or '').lower():
                continue
            if p.orientacion == 'hetero' and perf.genero == p.genero:
                continue
            if p.orientacion == 'homo' and perf.genero != p.genero:
                continue
            if otro.id in conectados_ids:
                continue
            candidatos.append({
                'id': otro.id,
                'nombre': otro.nombre,
                'edad': perf.edad,
                'genero': perf.genero,
                'orientacion': perf.orientacion,
                'pais': perf.pais,
                'ciudad': perf.ciudad,
                'idioma': perf.idioma,
                'avatar': perf.avatar,
                'bio': perf.bio,
                'intereses': perf.intereses,
            })

    return render_template('match.html', perfiles=candidatos, nombre=usr.nombre)

@match_bp.route('/conectar/<int:perfil_id>', methods=['POST'])
def conectar(perfil_id):
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))
    from vibra.models import Conexion
    mi_id = session['usuario_id']
    ya_existe = Conexion.query.filter_by(usuario_id=mi_id, conectado_a_id=perfil_id).first()
    
    if not ya_existe:
        conexion = Conexion(usuario_id=mi_id, conectado_a_id=perfil_id, tipo='like')
        db.session.add(conexion)
        db.session.commit()

        # Detectar si el otro también dio like → es match mutuo
        if es_match_mutuo(mi_id, perfil_id):
            from flask import flash
            flash("💫 ¡Tienes una conexión mutua! Ya puedes ver su perfil en 'Mis matches'.", "success")
        else:
            flash("✔ Has enviado una solicitud de conexión.", "success")
    return redirect(url_for('match.match'))

@match_bp.route('/rechazar/<int:perfil_id>', methods=['POST'])
def rechazar(perfil_id):
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))
    from vibra.models import Conexion
    mi_id = session['usuario_id']
    ya_existe = Conexion.query.filter_by(usuario_id=mi_id, conectado_a_id=perfil_id).first()
    if not ya_existe:
        conexion = Conexion(usuario_id=mi_id, conectado_a_id=perfil_id, tipo='nope')
        db.session.add(conexion)
        db.session.commit()
    return redirect(url_for('match.match'))

@match_bp.route('/mis-matches')
def mis_matches():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))
    
    from vibra.models import Usuario, Conexion
    from vibra.utils import es_match_mutuo

    mi_id = session['usuario_id']
    mis_likes = Conexion.query.filter_by(usuario_id=mi_id, tipo='like').all()
    matches = []

    for like in mis_likes:
        if es_match_mutuo(mi_id, like.conectado_a_id):
            otro = Usuario.query.get(like.conectado_a_id)
            if otro and otro.perfil:
                matches.append({
                    'id': otro.id,
                    'nombre': otro.nombre,
                    'edad': otro.perfil.edad,
                    'avatar': otro.perfil.avatar,
                    'bio': otro.perfil.bio,
                    'ciudad': otro.perfil.ciudad,
                    'pais': otro.perfil.pais,
                })

    return render_template('mis_matches.html', matches=matches)


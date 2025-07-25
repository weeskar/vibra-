from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from vibra.models import Usuario, Perfil, Conexion
from vibra.utils import es_match_mutuo
from vibra import db
from vibra.demo_data import PAISES, IDIOMAS, CIUDADES
from vibra.utils import allowed_file
import json
import os

perfil_bp = Blueprint('perfil', __name__)
# Carga única del archivo JSON al iniciar
RUTA_CPS = os.path.join(os.path.dirname(__file__), '../data/codigos_postales_es.json')
with open(RUTA_CPS, encoding='utf-8') as f:
    CODIGOS_POSTALES = json.load(f)

@perfil_bp.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))
    usr = Usuario.query.get(session['usuario_id'])
    perfil = usr.perfil
    pais_actual = perfil.pais or PAISES[0]
    ciudades_actuales = CIUDADES.get(pais_actual, [])

    if request.method == 'POST':
        usr.nombre          = request.form.get('nombre', usr.nombre)
        perfil.edad         = int(request.form.get('edad', perfil.edad or 18))
        perfil.pais         = request.form.get('pais', perfil.pais)
        perfil.ciudad       = request.form.get('ciudad', perfil.ciudad)
        perfil.codigo_postal = request.form.get('codigo_postal', '')
        perfil.codigo_postal = request.form.get('codigo_postal', '')

# 💡 Autocompleta ciudad, provincia y país usando el CP si está en la base
        cp = perfil.codigo_postal.strip()
        if cp in CODIGOS_POSTALES:
            datos = CODIGOS_POSTALES[cp]
            perfil.ciudad = datos.get('ciudad', perfil.ciudad)
            perfil.provincia = datos.get('provincia', perfil.provincia)
            perfil.pais = datos.get('pais', perfil.pais)
        perfil.idioma       = request.form.get('idioma', perfil.idioma)
        perfil.genero       = request.form.get('genero', perfil.genero)
        perfil.orientacion  = request.form.get('orientacion', perfil.orientacion)
        perfil.bio          = request.form.get('bio', perfil.bio)
        perfil.intereses    = request.form.get('intereses', perfil.intereses)
        perfil.frase_favorita = request.form.get('frase_favorita', perfil.frase_favorita)
        perfil.chakra = request.form.get('chakra', perfil.chakra)
        file = request.files.get('avatar')
        if file and allowed_file(file.filename):
            fname = f"{usr.id}_{file.filename}"
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], fname))
            perfil.avatar = fname
        db.session.commit()
        flash('Perfil actualizado.', 'success')
        return redirect(url_for('perfil.perfil'))

    return render_template(
        'perfil.html',
        usuario=usr,
        paises=PAISES,
        ciudades=CIUDADES.get(perfil.pais or PAISES[0], []),
        idiomas=IDIOMAS
    )

@perfil_bp.route('/usuario/<int:perfil_id>')
def ver_perfil_usuario(perfil_id):
    perfil = Perfil.query.get_or_404(perfil_id)
    usuario = perfil.usuario
    soy_yo = session.get('usuario_id') == usuario.id
    yo_id = session.get('usuario_id')
    match_mutuo = es_match_mutuo(yo_id, usuario.id) if not soy_yo else False
    like_ya_dado = Conexion.query.filter_by(usuario_id=yo_id, conectado_a_id=usuario.id, tipo='like').first() is not None

    return render_template(
        'perfil_publico.html', 
        perfil=perfil, 
        usuario=usuario, 
        soy_yo=soy_yo, 
        match_mutuo=match_mutuo,
        like_ya_dado=like_ya_dado
    )
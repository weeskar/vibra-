#/routes/config.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from vibra.models import Usuario,Conexion
from vibra import db

config_bp = Blueprint('config', __name__)

@config_bp.route('/configuracion', methods=['GET', 'POST'])
def configuracion():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))
    usr = Usuario.query.get(session['usuario_id'])

    if request.method == 'POST':
        # Borrar conexiones en las que aparece este usuario
        Conexion.query.filter_by(usuario_id=usr.id).delete()
        Conexion.query.filter_by(conectado_a_id=usr.id).delete()
        
        db.session.delete(usr.perfil)
        db.session.delete(usr)
        db.session.commit()
        session.clear()
        flash("Cuenta eliminada correctamente.", "success")
        return redirect(url_for('home.home'))

    return render_template('configuracion.html')
#vibra/routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from vibra.models import Usuario, Perfil
from vibra import db
from datetime import datetime, date
from vibra.demo_data import PAISES, IDIOMAS, CIUDADES
from vibra.utils import calcular_signo_zodiacal 
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre  = request.form['nombre']
        email   = request.form['email']
        pwd     = request.form['password']
        confirm = request.form['confirm']
        fecha_nacimiento_str = request.form['fecha_nacimiento']

        if pwd != confirm:
            flash('Las contraseñas no coinciden.', 'error')
            return redirect(url_for('auth.registro'))
        if Usuario.query.filter_by(email=email).first():
            flash('El email ya está registrado.', 'error')
            return redirect(url_for('auth.registro'))
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Fecha de nacimiento inválida.', 'error')
            return redirect(url_for('auth.registro'))

        hoy = date.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if edad < 18:
            flash('Debes tener al menos 18 años.', 'error')
            return redirect(url_for('auth.registro'))
        hashed = generate_password_hash(pwd)
        usr = Usuario(nombre=nombre, email=email, password=hashed)
        db.session.add(usr)
        db.session.commit()
        # Calculamos el signo zodiacal a partir de la fecha de nacimiento
        signo = calcular_signo_zodiacal(fecha_nacimiento)

        # Creamos el perfil del usuario incluyendo el signo calculado
        perfil = Perfil(
            usuario_id=usr.id,
            fecha_nacimiento=fecha_nacimiento,
            edad=edad,
            signo=signo  # ⬅️ Guardamos el signo en la base de datos
        )
        db.session.add(perfil)
        db.session.commit()
        flash('Registro exitoso. Por favor inicia sesión.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('registro.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd   = request.form['password']
        usr   = Usuario.query.filter_by(email=email).first()
        if usr and check_password_hash(usr.password, pwd):
            session['usuario_id']     = usr.id
            session['usuario_nombre'] = usr.nombre
            session['es_premium']     = usr.es_premium  # 🔧 corregido
            return redirect(url_for('perfil.perfil'))
        flash('Credenciales incorrectas.', 'error')
        return redirect(url_for('auth.login'))
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.home'))

@auth_bp.route('/actualizar_a_premium')
def actualizar_a_premium():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    usuario = Usuario.query.get(session['usuario_id'])
    if usuario:
        usuario.es_premium = True
        db.session.commit()

        # 🔁 ¡Actualiza la sesión!
        session['es_premium'] = True

        flash('¡Felicidades! Ahora eres usuario Premium.', 'success')

    return redirect(url_for('config.configuracion'))

@auth_bp.route('/cancelar_premium', methods=['POST'])
def cancelar_premium():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    usuario = Usuario.query.get(session['usuario_id'])
    if usuario:
        usuario.es_premium = False
        db.session.commit()
        session['es_premium'] = False  # 👈 Actualiza la sesión también

        flash('Tu suscripción Premium ha sido cancelada.', 'info')

    return redirect(url_for('config.configuracion'))
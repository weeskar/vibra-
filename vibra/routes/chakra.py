# chakra.py (flujo completo paso a paso)
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from vibra.models import Usuario
from vibra import db
import os
import json

# Importamos las preguntas desde data
from vibra.data.chakra_test_data import CHAKRA_PREGUNTAS

chakra_bp = Blueprint('chakra', __name__)

# Página de introducción
@chakra_bp.route('/chakra/test')
def chakra_test_intro():
    return render_template('chakra_test_intro.html')


# Página paso a paso, una por chakra
@chakra_bp.route('/chakra/test/paso/<int:paso>', methods=['GET', 'POST'])
def chakra_test_paso(paso):
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    chakras = list(CHAKRA_PREGUNTAS.keys())  # ['raiz', 'sacro', ...]
    total = len(chakras)

    if paso < 1 or paso > total:
        return redirect(url_for('chakra.chakra_test_intro'))

    if request.method == 'POST':
        # Guardamos respuestas del paso actual en la sesión
        respuestas = session.get('chakra_respuestas', {})
        chakra_clave = chakras[paso - 1]
        puntuacion = sum([int(request.form.get(f'p{i}', 0)) for i in range(3)])
        respuestas[chakra_clave] = puntuacion
        session['chakra_respuestas'] = respuestas

        if paso == total:
            return redirect(url_for('chakra.chakra_test_resultado'))
        else:
            return redirect(url_for('chakra.chakra_test_paso', paso=paso + 1))

    chakra_clave = chakras[paso - 1]
    datos = CHAKRA_PREGUNTAS[chakra_clave]

    return render_template(
        'chakra_test_step.html',
        paso=paso,
        total=total,
        chakra=chakra_clave,
        datos=datos
    )


# Resultado final
@chakra_bp.route('/chakra/test/resultado')
def chakra_test_resultado():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    respuestas = session.get('chakra_respuestas', {})
    if not respuestas:
        return redirect(url_for('chakra.chakra_test_intro'))

    # Determinar chakra con mayor puntuación
    chakra_final = max(respuestas, key=lambda k: respuestas[k])
    datos = CHAKRA_PREGUNTAS[chakra_final]

    # Guardar en perfil del usuario
    usuario = Usuario.query.get(session['usuario_id'])
    if usuario and usuario.perfil:
        usuario.perfil.chakra = chakra_final
        db.session.commit()
        flash(f"✨ Tu chakra predominante es {datos['nombre']}", "success")

    # Limpiar las respuestas para futuros tests
    session.pop('chakra_respuestas', None)

    return render_template('chakra_test_result.html', chakra=chakra_final, datos=datos)
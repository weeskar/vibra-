from vibra.models import Conexion
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def es_match_mutuo(usuario_id, otro_id):
    like_a = Conexion.query.filter_by(usuario_id=usuario_id, conectado_a_id=otro_id, tipo='like').first()
    like_b = Conexion.query.filter_by(usuario_id=otro_id, conectado_a_id=usuario_id, tipo='like').first()
    return like_a and like_b

def calcular_signo_zodiacal(fecha):
    # Obtenemos el día y el mes de la fecha de nacimiento
    dia = fecha.day
    mes = fecha.month

    # Convertimos la fecha a un número de tipo MMDD (ej: 14 de marzo → 314)
    fecha_num = mes * 100 + dia

    # Lista ordenada por fechas límite de cada signo
    # Cada tupla contiene: (fecha_límite_en_MMDD, "Signo")
    signos = [
        (120, "Capricornio"),   # Hasta el 20 de enero
        (219, "Acuario"),       # Hasta el 19 de febrero
        (320, "Piscis"),        # Hasta el 20 de marzo
        (420, "Aries"),         # Hasta el 20 de abril
        (521, "Tauro"),         # Hasta el 21 de mayo
        (621, "Géminis"),       # Hasta el 21 de junio
        (722, "Cáncer"),        # Hasta el 22 de julio
        (823, "Leo"),           # Hasta el 23 de agosto
        (923, "Virgo"),         # Hasta el 23 de septiembre
        (1023, "Libra"),        # Hasta el 23 de octubre
        (1122, "Escorpio"),     # Hasta el 22 de noviembre
        (1221, "Sagitario"),    # Hasta el 21 de diciembre
        (1231, "Capricornio")   # Resto del año → Capricornio de nuevo
    ]

    # Recorremos la lista para encontrar el signo correspondiente
    for limite, signo in signos:
        if fecha_num <= limite:
            return signo

    # Si por alguna razón no se encuentra (muy raro), devolvemos Capricornio por defecto
    return "Capricornio"
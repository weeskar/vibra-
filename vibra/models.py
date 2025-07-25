from vibra import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    es_premium = db.Column(db.Boolean, default=False)
    perfil = db.relationship('Perfil', backref='usuario', uselist=False)

class Perfil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    edad = db.Column(db.Integer, default=18)
    pais = db.Column(db.String(40), default='España')
    ciudad = db.Column(db.String(40), default='')
    provincia = db.Column(db.String(50), default='')
    codigo_postal = db.Column(db.String(10), default='')
    idioma = db.Column(db.String(20), default='Español')
    genero = db.Column(db.String(10), default='')
    orientacion = db.Column(db.String(20), default='hetero')
    bio = db.Column(db.Text, default='')
    intereses = db.Column(db.String(200), default='')
    avatar = db.Column(db.String(200), default='')
    frase_favorita = db.Column(db.String(120))
    chakra = db.Column(db.String(20))
    signo = db.Column(db.String(20))

class Conexion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    conectado_a_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # 'like' o 'nope'
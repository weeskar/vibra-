# chakra_test_data.py
# Este archivo contiene las preguntas del Test de Chakras
# Cada chakra tiene una lista de preguntas, cada una con opciones de respuesta
# Las opciones están valoradas con un puntaje (0 a 2)

CHAKRA_PREGUNTAS = {
    "raiz": {
        "nombre": "Chakra Raíz",
        "color": "🌱",
        "descripcion": "Representa la seguridad, estabilidad y conexión con lo físico.",
        "preguntas": [
            {
                "texto": "¿Cómo te sientes respecto a tu seguridad económica y necesidades básicas?",
                "opciones": [
                    ("Me siento inseguro/a y constantemente en modo supervivencia", 0),
                    ("Tengo lo justo pero no siempre me siento estable", 1),
                    ("Me siento estable, seguro/a y en paz con mis necesidades", 2)
                ]
            },
            {
                "texto": "¿Cómo describirías tu relación con tu cuerpo físico?",
                "opciones": [
                    ("Evito sentirlo o cuidarlo", 0),
                    ("Intento cuidarlo aunque me cuesta", 1),
                    ("Estoy conectado/a, lo respeto y cuido", 2)
                ]
            },
            {
                "texto": "¿Cómo vives tu sentido de pertenencia (familia, hogar, entorno)?",
                "opciones": [
                    ("Me siento desconectado/a, sin raíces", 0),
                    ("Tengo lazos pero a veces me siento fuera de lugar", 1),
                    ("Siento que pertenezco y tengo una base sólida", 2)
                ]
            }
        ]
    },

    "sacro": {
        "nombre": "Chakra Sacro",
        "color": "🧡",
        "descripcion": "Conectado con la creatividad, el placer y las emociones.",
        "preguntas": [
            {
                "texto": "¿Qué tan fácil te resulta disfrutar del placer (arte, comida, intimidad)?",
                "opciones": [
                    ("Siento culpa o bloqueo al disfrutar", 0),
                    ("Me permito disfrutar a veces", 1),
                    ("Disfruto sin culpas, plenamente", 2)
                ]
            },
            {
                "texto": "¿Cómo gestionas tus emociones?",
                "opciones": [
                    ("Me abruman o las reprimo", 0),
                    ("Las reconozco pero me cuesta expresarlas", 1),
                    ("Fluyo con ellas y las expreso con libertad", 2)
                ]
            },
            {
                "texto": "¿Sientes que tu energía creativa está activa?",
                "opciones": [
                    ("Estoy bloqueado/a creativamente", 0),
                    ("A veces me inspiro pero me freno", 1),
                    ("Tengo ideas, inspiración y me expreso", 2)
                ]
            }
        ]
    },

    "plexo": {
        "nombre": "Chakra Plexo Solar",
        "color": "🔆",
        "descripcion": "Representa el poder personal, la autoestima y la acción.",
        "preguntas": [
            {
                "texto": "¿Cómo describirías tu nivel de autoestima actualmente?",
                "opciones": [
                    ("Me cuesta valorarme o confiar en mí", 0),
                    ("Estoy aprendiendo a reconocer mi valor", 1),
                    ("Confío en mí mismo/a y en mis capacidades", 2)
                ]
            },
            {
                "texto": "¿Tomas decisiones con confianza?",
                "opciones": [
                    ("Me cuesta mucho decidir o actuar", 0),
                    ("Tomo decisiones aunque con dudas", 1),
                    ("Decido con claridad y firmeza", 2)
                ]
            },
            {
                "texto": "¿Cómo manejas la frustración o el fracaso?",
                "opciones": [
                    ("Me derrumbo fácilmente", 0),
                    ("Me cuesta pero intento aprender", 1),
                    ("Lo veo como una oportunidad de crecimiento", 2)
                ]
            }
        ]
    },
    "corazon": {
        "nombre": "Chakra Corazón",
        "color": "💚",
        "descripcion": "Relaciona el amor, la compasión y la conexión emocional.",
        "preguntas": [
            {
                "texto": "¿Cómo vives tus relaciones personales?",
                "opciones": [
                    ("Me cuesta abrirme emocionalmente", 0),
                    ("Intento confiar pero tengo heridas", 1),
                    ("Soy abierto/a y me relaciono con amor", 2)
                ]
            },
            {
                "texto": "¿Perdonas fácilmente cuando te han herido?",
                "opciones": [
                    ("Guardo rencor o me cuesta soltar", 0),
                    ("Me esfuerzo en perdonar aunque me cuesta", 1),
                    ("Perdono con el corazón y me libero", 2)
                ]
            },
            {
                "texto": "¿Te sientes conectado/a emocionalmente con los demás?",
                "opciones": [
                    ("Siento distancia o desconexión", 0),
                    ("A veces conecto, pero no siempre me es fácil", 1),
                    ("Siento amor y empatía frecuentemente", 2)
                ]
            }
        ]
    },
    "garganta": {
        "nombre": "Chakra Garganta",
        "color": "💙",
        "descripcion": "Asociado a la comunicación, expresión y autenticidad.",
        "preguntas": [
            {
                "texto": "¿Te resulta fácil expresar lo que realmente piensas o sientes?",
                "opciones": [
                    ("Evito decir lo que siento o pienso", 0),
                    ("Lo intento aunque a veces me callo", 1),
                    ("Me comunico de forma auténtica y clara", 2)
                ]
            },
            {
                "texto": "¿Eres capaz de decir 'no' cuando es necesario?",
                "opciones": [
                    ("Me cuesta mucho poner límites", 0),
                    ("A veces lo hago, pero me siento culpable", 1),
                    ("Pongo límites sanos con confianza", 2)
                ]
            },
            {
                "texto": "¿Te sientes cómodo/a mostrando tu verdad al mundo?",
                "opciones": [
                    ("Siento miedo al juicio o al rechazo", 0),
                    ("Depende de la situación", 1),
                    ("Sí, soy fiel a mí mismo/a", 2)
                ]
            }
        ]
    },
    "tercer_ojo": {
        "nombre": "Chakra Tercer Ojo",
        "color": "🔮",
        "descripcion": "Representa la intuición, visión interna y percepción espiritual.",
        "preguntas": [
            {
                "texto": "¿Confías en tu intuición a la hora de tomar decisiones?",
                "opciones": [
                    ("No, me guío solo por lo racional", 0),
                    ("A veces me dejo guiar por mi intuición", 1),
                    ("Sí, escucho y confío en mi voz interior", 2)
                ]
            },
            {
                "texto": "¿Tienes facilidad para visualizar tus metas o sueños?",
                "opciones": [
                    ("Me cuesta imaginar o proyectar el futuro", 0),
                    ("A veces visualizo, pero me desconcentro", 1),
                    ("Sí, visualizo claramente mis objetivos", 2)
                ]
            },
            {
                "texto": "¿Te consideras alguien con conexión espiritual o percepción elevada?",
                "opciones": [
                    ("No, no me siento conectado/a con eso", 0),
                    ("A veces siento algo más allá", 1),
                    ("Sí, percibo más allá de lo visible", 2)
                ]
            }
        ]
    },
     "corona": {
        "nombre": "Chakra Corona",
        "color": "👑",
        "descripcion": "Asociado al propósito espiritual, sabiduría y conexión superior.",
        "preguntas": [
            {
                "texto": "¿Sientes que tu vida tiene un propósito más allá de lo material?",
                "opciones": [
                    ("No, vivo el día a día sin pensar en eso", 0),
                    ("A veces me lo pregunto", 1),
                    ("Sí, siento una misión o llamado profundo", 2)
                ]
            },
            {
                "texto": "¿Te tomas momentos para la reflexión o conexión espiritual?",
                "opciones": [
                    ("No, me cuesta parar o conectar", 0),
                    ("A veces lo intento, pero sin constancia", 1),
                    ("Sí, tengo prácticas o momentos espirituales", 2)
                ]
            },
            {
                "texto": "¿Cómo te sientes frente a lo desconocido o lo trascendente?",
                "opciones": [
                    ("Me genera miedo o rechazo", 0),
                    ("Siento curiosidad", 1),
                    ("Me inspira y me conecta con algo mayor", 2)
                ]
            }
        ]
    }   
}


import argparse
import itertools
from datetime import datetime

# --- Listas de Datos (Modificables y Ampliable)
# Mantengo las mismas listas que el script original para consistencia.
PALABRAS_COMUNES = [
    "amor", "casa", "perro", "gato", "sol", "luna", "familia", "trabajo", "escuela",
    "argentina", "futbol", "mate", "asado", "amigo", "clave", "secreto", "contraseña",
    "password", "admin", "root", "123456", "qwerty", "hola", "messi", "maradona",
    "libertad", "esperanza", "verano", "invierno", "primavera", "otoño", "cielo",
    "estrella", "montaña", "rio", "mar", "playa", "ciudad", "pueblo", "calle",
    "auto", "moto", "bicicleta", "viaje", "musica", "rock", "cumbia", "tango",
    "computadora", "celular", "internet", "wifi", "red", "sistema", "programa", "teleglobo", "dificil",
    "Dificil", "D1ficil", "Difici1", "D1f1c1l", "D1F1C1L", "D1F1c!l", "simple",
    "dolar", "cripto", "comida", "agua", "fuego", "tierra", "aire", "noche", "dia",
    "mañana", "tarde", "hoy", "ayer", "siempre", "nunca", "luz", "sombra",
    "libros", "pelicula", "serie", "juego", "deporte", "arte", "ciencia", "historia",
    "dinero", "mercado", "empresa", "gobierno", "presidente", "politica", "eleccion",
    "mundo", "universo", "planeta", "tiempo", "espacio", "numero", "letra", "palabra",
    "frase", "sentimiento", "felicidad", "tristeza", "miedo", "enojo", "sorpresa",
    "salud", "enfermedad", "hospital", "medico", "abogado", "ingeniero", "arquitecto",
    "maestro", "policia", "bombero", "soldado", "pintura", "escultura", "teatro",
    "innovacion", "desarrollo", "comunicacion", "educacion", "aprendizaje", "conocimiento",
    "sabiduria", "experiencia", "memoria", "futuro", "pasado", "presente", "realidad",
    "fantasia", "sueño", "pesadilla", "vida", "muerte", "nacimiento", "crecimiento",
    "cambio", "evolucion", "revolucion", "cultura", "sociedad", "comunidad",
    "amistad", "relacion", "pareja", "cuerpo", "mente", "alma", "espiritu",
    "energia", "fuerza", "poder", "valor", "coraje", "valentia", "temor",
    "pasion", "emocion", "paz", "guerra", "conflicto", "justicia", "injusticia",
    "ley", "crimen", "castigo", "verdad", "mentira", "engaño", "traicion",
    "lealtad", "confianza", "respeto", "tolerancia", "igualdad", "esclavitud",
    "derechos", "deberes", "responsabilidad", "compromiso", "esfuerzo",
    "dedicacion", "exito", "fracaso", "oportunidad", "riesgo", "aventura",
    "desafio", "logro", "victoria", "derrota", "premio", "recompensa",
    "sacrificio", "heroina", "heroe", "villano", "magia", "fantasma",
    "monstruo", "angel", "demonio", "dios", "diablo", "galaxia", "satelite",
    "cometa", "asteroide", "oscuridad", "calor", "frio", "viento", "lluvia",
    "nieve", "tormenta", "rayo", "trueno", "arcoiris", "niebla", "brisa",
    "oceano", "lago", "valle", "bosque", "selva", "desierto", "volcan",
    "isla", "peninsula", "continente", "pais", "barrio", "avenida", "plaza",
    "parque", "jardin", "campo", "granja", "cosecha", "siembra", "semilla",
    "planta", "arbol", "flor", "fruta", "verdura", "animal", "insecto",
    "pajaro", "pez", "reptil", "mamifero", "felino", "canino", "caballo",
    "vaca", "cerdo", "oveja", "gallina", "pollo", "huevo", "leche",
    "carne", "pescado", "pan", "arroz", "pasta", "azucar", "sal", "aceite",
    "vino", "cerveza", "cafe", "te", "gaseosa", "jugo", "refresco",
    "desayuno", "almuerzo", "cena", "postre", "golosina", "dulce",
    "amargo", "picante", "salado", "acido", "sabor", "olor", "color",
    "sonido", "tacto", "vista", "oido", "olfato", "gusto", "sentido",
    "pensamiento", "idea", "creacion", "invencion", "descubrimiento",
    "enseñanza", "idioma", "lenguaje", "matematica", "fisica", "quimica",
    "biologia", "astronomia", "geologia", "geografia", "literatura",
    "danza", "cine", "fotografia", "video", "atletismo", "natacion",
    "basquet", "voley", "tenis", "rugby", "boxeo", "judo", "karate",
    "taekwondo", "esgrima", "equitacion", "golf", "ciclismo",
    "automovilismo", "motociclismo", "surf", "skate", "snowboard", "ski",
    "escalada", "montañismo", "senderismo", "acampada", "pesca", "caza",
    "navegacion", "vela", "remo", "kayak", "submarinismo", "paracaidismo",
    "parapente", "alaDelta", "globoaerostatico", "avion", "helicoptero",
    "barco", "tren", "colectivo", "subte", "taxi", "remis", "monopatin",
    "patineta", "caminata", "corrida", "trotar", "marcha", "carrera", "salto",
    "lanzamiento", "oficina", "fabrica", "taller", "laboratorio",
    "universidad", "biblioteca", "museo", "estadio", "gimnasio", "piscina",
    "balneario", "capital", "provincia", "departamento", "region",
    "cosmos", "amanecer", "atardecer", "estacion", "clima", "temperatura",
    "nube", "relampago", "granizo", "humedad", "sequia", "inundacion",
    "terremoto", "tsunami", "huracan", "tornado", "ciclón", "monzon",
    "rafaga", "calma", "ruido", "silencio", "cancion", "melodia", "ritmo",
    "armonia", "nota", "acorde", "banda", "orquesta", "solista", "cantante",
    "guitarra", "piano", "bateria", "bajo", "violin", "flauta", "saxo",
    "trompeta", "clarinete", "oboe", "cello", "arpa", "acordeon",
    "bandoneon", "charango", "bombo", "tambor", "maraca"
]

NOMBRES_PROPIOS = [
    "juan", "maria", "carlos", "sofia", "agustin", "valentina", "mateo", "camila",
    "lionel", "diego", "santiago", "lucia", "emi", "marcos", "lautaro", "julian",
    "enzo", "nicolas", "martina", "lucas", "facundo", "manuel", "victoria", "paula",
    "roberto", "florencia", "alejandro", "andres", "daniela", "javier", "antonio", "valentin",
    "gabriel", "sebastian", "fernando", "pedro", "francisco", "martin", "luciana",
    "belen", "celeste", "natalia", "josefina", "ana", "ivan", "federico", "ramiro",
    "pablo", "agustina", "esteban", "lorena", "teresa", "ricardo", "hugo", "silvia",
    "adriana", "alberto", "alfonso", "amelia", "beatriz", "bernardo", "carla",
    "claudia", "cristian", "daniel", "david", "eduardo", "elena", "emilio",
    "ernesto", "esther", "eva", "fabian", "felipe", "gabriela", "german",
    "gustavo", "hector", "horacio", "ignacio", "ines", "irene", "isabel", "jaime",
    "jorge", "joaquin", "jose", "julia", "karina", "laura", "leonardo", "leticia",
    "liliana", "marcelo", "margarita", "mario", "melisa", "miguel", "mirta", "monica",
    "nancy", "norma", "oscar", "patricia", "raul", "renata", "rita",
    "rocio", "rosa", "ruben", "sandra", "sergio", "sonia", "tomas", "ursula",
    "vanesa", "veronica", "walter", "ximena", "yolanda", "zamira", "abel", "adolfo",
    "adrian", "aitana", "alicia", "alonso", "alvaro", "amanda", "amparo",
    "angel", "antonia", "ariana", "arturo", "benjamin", "berta", "blanca", "borja",
    "braulio", "candela", "cecilia", "clemente", "consuelo", "cora", "cristina",
    "dario", "dolores", "domingo", "dorotea", "eduarda", "elisa", "enrique",
    "esperanza", "estela", "eugenia", "eugenio", "federica", "felicia", "fernanda",
    "fidel", "fortunato", "francisca", "gema", "gervasio", "gisela", "gloria",
    "gonzalo", "graciela", "hilda", "hilario", "ileana", "isidoro", "jenny",
    "jessica", "jimena", "jonatan", "joseluis", "juana", "julio", "justina", "karen",
    "kevin", "kimberly", "laila", "leandro", "leila", "lenny", "lila", "linda",
    "lola", "lourdes", "luis", "macarena", "manuela", "marcia", "marisol", "marlene",
    "mauricio", "maximiliano", "melina", "michell", "miriam", "nayla",
    "nestor", "noelia", "noemi", "ofelia", "olga", "pamela", "paola", "pascual",
    "patricio", "paulina", "pilar", "quim", "rafael", "raquel", "reina", "remigio",
    "rodolfo", "romina", "ronald", "rosana", "rosario", "roxana",
    "salvador", "samuel", "sandrita", "sara", "saul", "sharon",
    "sixto", "sol", "stefania", "stephany", "susana", "tania", "tatiana", "tomasa",
    "trinidad", "ulises", "valeria", "vanessa", "vera", "vicente", "virginia",
    "yago", "yamila", "yasmin", "yessica", "yolanda", "zaida", "zaira", "zulema"
]

APELLIDOS_COMUNES = [
    "gonzalez", "rodriguez", "gomez", "fernandez", "lopez", "diaz", "martinez",
    "perez", "sanchez", "romero", "garcia", "sosa", "castro", "benitez", "ramirez",
    "torres", "flores", "ruiz", "alvarez", "acosta", "gimenez", "medina", "herrera",
    "moreno", "silva", "ferreyra", "blanco", "russo", "suarez", "ortiz", "rivero",
    "paz", "arias", "vazquez", "mendez", "cabrera", "juarez", "galvan", "escobar",
    "vega", "quiroga", "barrios", "aguero", "costa", "ibarra", "aguilar", "alonso",
    "arce", "avila", "ayala", "baez", "balbiani", "barrera", "barros", "bernal",
    "blasco", "burgos", "bustamante", "cabral", "campana", "cantero", "carrizo",
    "cassino", "cruz", "chavez", "cruzado", "daher", "delgado", "dominguez", "duarte",
    "erramuspe", "esquivel", "falco", "fariña", "frias", "gallardo", "gallo",
    "garofalo", "giannone", "gil", "gutierrez", "hernandez", "hidalgo", "ibañez",
    "molina", "monzon", "mora", "morales", "muñoz", "navarro", "nunez", "oliva",
    "ortega", "otero", "padilla", "palacios", "pascual", "portillo", "prieto",
    "quinteros", "ramos", "rojas", "rosales", "rubio", "salazar", "salinas",
    "santana", "santiago", "sierra", "solis", "toledo", "toro", "urbano", "valdez",
    "velazquez", "vera", "vidal", "villalba", "zambon", "zarate", "zuloaga", "zuniga",
    "achaval", "alarcon", "aleman", "andrada", "aranda", "arrieta", "barboza",
    "benavidez", "bustos", "campos", "cardozo", "correa", "cortez", "costilla",
    "cuenca", "duran", "elias", "espinoza", "godoy", "jara", "jimenez", "leiva",
    "lucero", "mansilla", "marquez", "miranda", "mendez", "ortega", "otero",
    "paredes", "pereyra", "pinero", "reyes", "robles", "tejeda", "vargas",
    "videla", "villagra", "villanueva"
]

LUGARES_FAMOSOS = [
    "obelisco", "caminito", "perito", "moreno", "iguazu", "bariloche", "mendoza",
    "ushuaia", "calafate", "libertador", "corrientes", "palermo", "recoleta",
    "santelmo", "laboca", "puertomadero", "talampaya", "aconcagua", "fitzroy",
    "nahuelhuapi", "rosario", "cordoba", "salta", "jujuy", "cataratas", "glaciar",
    "laplata", "mardelplata", "pinamar", "villagesell", "sanmartin", "chubut",
    "tierradelfuego", "patagonia", "valdes", "chalten", "salinasgrandes", "cuyo",
    "sierrasdecordoba", "lujan", "tigre", "colondetigre", "puentelamujer",
    "bosquesdepalermo", "jardinjapones", "planetario", "cabildo", "casarosada",
    "congreso", "teatrocolon", "barriochino", "bancodelnacion",
    "basilicadesanjuan", "catedralmetropolitana", "estadiomonumental", "estadiobocajuniors",
    "malba", "museonacionaldebellaartes", "museosivori", "centroculturalrecoleta",
    "centroculturalkirchner", "parquedelacosta", "parquelezama", "parquecentenario",
    "reservanaturaleccologica", "delta", "puertodebuenosaires", "mercadodesantelmo",
    "mercadodepuertos", "torredegales", "torremolinos", "torredecaballito",
    "costanera", "riachuelo", "lagos", "tucuman", "catamarca", "santiagodelestero",
    "larioja", "sanluis", "sanrafael", "generalroca", "viedma", "neuquen", "comodoro",
    "rivadavia", "puertomadryn", "rawson", "elbolson", "esquel", "trelew",
    "riogallegos", "tolhuin", "caletaolivia", "riogrande", "patagonia", "chalten",
    "elcalafate", "puertonatales", "puntaarenas", "puertomontt", "puertovarvas",
    "chile", "peru", "uruguay", "paraguay", "brasil", "bolivia", "oceanopacifico",
    "oceanoatlantico", "santaclara", "sanbernardo", "lacosta", "gesell",
    "miramar", "necochea", "carilo", "ostende", "valeriadelmar", "lasgrutas",
    "villalaangostura", "sancarlosdebariloche", "puertoblest", "sannicolas",
    "sanpedro", "ramallos", "zarate", "campana", "merlo", "moreno", "moron",
    "mercedes", "chivilcoy", "junin", "pergamino", "olavarria", "tandil", "bahiablanca",
    "coronelsuarez", "marcosjuarez", "riocuarto", "rioter", "villamaria",
    "lasheras", "godoycruz", "lujandecuyo", "maipu", "guaymallen", "lavalle",
    "tunuyan", "tupungato", "malargue", "lamatador", "lavelez", "laferrere",
    "gonzalezcatan", "virreydelpino", "villaurquiza", "villapueyrredon",
    "villadevocion", "palermoview", "jardindebotella", "jardinzoologico",
    "calleflorida", "calletango", "catedral", "manzana", "monumental", "bombonera",
    "puertecarranza", "palaciobarolo", "lagosdebelgrano", "barriobancario", "cajamagica"
]

MODISMOS_ARGENTINOS = [
    "che", "boludo", "quilombo", "bondi", "chabon", "pibe", "mina", "birra",
    "milanga", "scaloneta", "vamos", "fachero", "churro", "guita", "mango",
    "laburo", "trucho", "yeta", "fiaca", "morfi", "zarpado", "careta",
    "gil", "posta", "onda", "chamuyo", "capo", "pata", "gamba", "bollo", "chamullo",
    "gato", "yuta", "cana", "jeton", "orto", "queres", "chaucha", "yuyito", "pilcha",
    "pindonga", "cocoliche", "bichicome", "canyengue", "berretin", "cagazo",
    "fulano", "mengano", "sutano", "tarasca", "mita",
    "fulero", "gilada", "grosso", "mufa", "nafta", "pila", "pichin",
    "piola", "pituco", "pitufo", "polenta", "rancho",
    "mangar", "morfar", "ortiva", "pelotudo",
    "pesos", "pino", "pistero", "planchita", "plomo",
    "poronga", "rayado", "re", "rejo",
    "rolinga", "ruso", "saca", "sarpado", "seca", "seguidilla", "seguidita",
    "tacho", "tano", "tirar", "tito", "toga", "toma", "torta",
    "trucho", "tucu", "tucuman", "turro", "tuyuy", "verga", "villero",
    "virgen", "vueltas", "zapan",
    "zurdo", "abacanado", "abarcar", "abrirse", "aca", "acaso", "aclarar",
    "acortar", "aguila", "ahuecar", "apretar", "apilado", "arruinar",
    "bajon", "banana", "bardo", "bañar", "boca", "bondi", "bronca",
    "cadena", "cagar", "calentar", "chafalon",
    "chafita", "chamullar", "chanta", "chapar", "chapita", "cheto",
    "chivo", "choro", "choto", "chupar", "chuparrosa", "chupin",
    "cilindrada", "clavo", "corte", "creer", "cruzar", "cuadra",
    "cuervo", "cumbia", "cumpa", "dar", "dena", "despelote", "diente",
    "duda", "duro", "embole", "empanada", "enculado", "enfiestado",
    "enganchar", "espada", "facha", "fachero", "facho", "feca",
    "filmar", "flaco", "flequillo", "flojo", "forro",
    "fresita", "frio", "gilastro", "giles",
    "glamoroso", "gomero", "gorra", "grieta", "groncho",
    "guita", "hacerse", "hincapié", "horrible", "huevos", "impresora",
    "injusticia", "jaula", "joda", "jodido", "jopo", "justicia",
    "labia", "laburar", "lacra", "lana", "largar", "lavar", "lector",
    "lindo", "loco", "longa", "macanudo", "machete", "mango",
    "manga", "mano", "manteca", "manotear", "maricon", "mierda",
    "milanga", "minita", "mocho", "muerto", "la12", "losmillos",
    "bostero", "gallina", "hincha", "cancha", "clasico"
]

EQUIPOS_FUTBOL = [
    "river", "boca", "independiente", "racing", "sanlorenzo", "velez", "huracan",
    "estudiantes", "gimnasia", "rosariocentral", "newells", "talleres", "belgrano",
    "lanus", "banfield", "argentinos", "defensayjusticia", "atleticotucuman",
    "colon", "union", "godoycruz", "sanmartin", "aldosivi", "temperley",
    "chacarita", "ferrocarril", "platense", "tigre", "almagro", "brown",
    "quilmes", "sanmiguel", "deportivoarmenio", "almirantebrown",
    "gimnasiayesgrima", "estudiantesdelaplata",
    "argentinosjuniors", "sanlorenzodealmagro",
    "huracan", "velezsarsfield", "racingclub", "riverplate",
    "bocajuniors", "newellsoldboys", "rosariocentral",
    "patronato", "losand", "acassuso",
    "tristansuarez", "deportivocentral", "deportivoespanol",
    "deportivoitali", "deportivoroca", "excursionista", "flandria",
    "lamadrid", "merlo", "midland", "nueva chicago", "olimpiadebahia",
    "sacachispas", "sarmiento", "villa san carlos"
]

TEMAS_TENDENCIA = [
    "oppenheimer", "barbie", "messi", "dibu", "granhermano", "milei", "inflacion",
    "verano", "invierno", "mundial", "copaamerica", "libertadores", "sudamericana",
    "elecciones", "dolar", "blue", "crypto", "bitcoin", "ethereum", "netflix",
    "spotify", "instagram", "tiktok", "twitter", "facebook", "youtube", "google",
    "celular", "inteligenciaartificial", "chatgpt", "iphone", "samsung", "apple",
    "microsoft", "amazon", "tesla", "spacex", "elonmusk", "jeffbezos", "taylorswift",
    "badbunny", "shakira", "karolg", "ricky martin", "jlo", "reggaeton", "pop",
    "trap", "kpop", "anime", "manga", "gaming", "fortnite", "valorant", "fifa",
    "crisis", "economia", "politica", "salud", "vacuna", "virus", "pandemia",
    "clima", "calentamiento", "ambiental", "cambioclimatico", "sequia", "frio",
    "calor", "incendio", "bosque", "naturaleza", "contaminacion", "reciclaje",
    "ecologia", "medioambiente", "energia", "solar", "renovable", "nuclear",
    "petroleo", "gas", "litio", "mineria", "agricultura", "ganaderia", "pesca",
    "tecnologia", "ciencia", "medicina", "genetica", "robotica", "futuro",
    "internet", "redes", "sociales", "whatsapp", "telegram", "discord", "twitch",
    "onlyfans", "patreon", "substack", "criptomonedas", "blockchain", "metaverso",
    "realidadvirtual", "realidad", "aumentada", "eSports", "streaming", "influencer",
    "marketing", "digital", "algoritmo", "bigdata", "ciberseguridad", "hacker",
    "malware", "ransomware", "phishing", "fraude", "online",
    "comercioelectronico", "ecommerce", "tienda", "virtual", "delivery", "logistica",
    "criptos", "fintech", "banca", "pago", "movil", "tarjeta", "credito",
    "debito", "inversion", "acciones", "bolsa", "mercado", "financiero", "startup",
    "unicornio", "emprendimiento", "freelance", "trabajoremoto", "coworking",
    "nomina", "sueldo", "salario", "impuesto", "iva", "ganancias", "renta",
    "devaluacion", "precios", "canasta", "basica", "subsidio",
    "jubilacion", "pension", "seguro", "social", "prepaga",
    "obra", "sindicato", "gremios", "paritarias", "huelga", "paro",
    "protesta", "movilizacion", "marcha", "manifestacion", "discurso", "debate",
    "ley", "decreto", "proyecto", "congreso", "senado", "diputados", "juez",
    "fiscal", "justicia", "policia", "ejercito", "fuerza", "armada",
    "armas", "seguridad", "delincuencia", "robo", "asalto", "violencia",
    "corrupcion", "narco", "trafico", "drogas", "mafia", "pandilla", "banda",
    "cartel", "migracion", "inmigrante", "refugiado", "extranjero", "frontera",
    "pasaporte", "visa", "turismo", "viaje", "destino", "playa", "montaña",
    "capital", "provincia", "region", "pais", "mundo", "universo", "planeta",
    "galaxia", "astronauta", "nasa", "cohete", "satelite", "estacion",
    "espacial", "mars", "moon", "jupiter", "venus", "luna", "estrella",
    "constelacion", "zodiaco", "horoscopo", "astrologia", "astronomia",
    "meditacion", "yoga", "pilates", "mindfulness", "bienestar", "saludmental",
    "ansiedad", "estres", "depresion", "terapia", "psicologo", "psiquiatra",
    "nutricion", "dieta", "ejercicio", "deporte", "fitness", "gimnasio",
    "crossfit", "running", "maraton", "triatlon", "ciclismo", "natacion",
    "senderismo", "escalada", "aventura", "naturaleza", "campo", "bosque",
    "rio", "lago", "isla", "selva", "desierto", "virus"
]

# Combinar todas las listas de palabras en una sola para algunas mutaciones
PALABRAS_BASE = list(set(
    PALABRAS_COMUNES + NOMBRES_PROPIOS + APELLIDOS_COMUNES + LUGARES_FAMOSOS +
    MODISMOS_ARGENTINOS + EQUIPOS_FUTBOL + TEMAS_TENDENCIA
))

# --- Reglas de Mutación ---

def anadir_numeros(palabras):
    """Añade números comunes al final de una lista de palabras."""
    resultados = set()
    numeros_comunes = ["123", "1234", "12345", "1", "2", "3"] + [str(i) for i in range(100)] # Ampliado a 0-99
    anos_comunes = [str(y) for y in range(datetime.now().year - 10, datetime.now().year + 2)]
    
    for palabra in palabras:
        for num in numeros_comunes:
            resultados.add(palabra + num)
        for ano in anos_comunes:
            resultados.add(palabra + ano)
    return resultados

def sustituir_letras(palabras):
    """Sustituye letras por símbolos comunes (leetspeak)."""
    resultados = set()
    mapa_letras = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
    
    for palabra in palabras:
        resultados.add(palabra)
        for original, reemplazo in mapa_letras.items():
            if original in palabra:
                nueva_palabra = palabra.replace(original, reemplazo)
                resultados.add(nueva_palabra)
    return resultados

def mutacion_compleja(palabras):
    """Aplica una serie de mutaciones complejas para generar contraseñas robustas."""
    resultados = set()
    mapa_leetspeak_avanzado = {
        'a': ['@', '4'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 
        's': ['$', '5'], 'l': ['1'], 't': ['7']
    }
    simbolos_finales = ['!', '@', '#', '$', '.', '*', '?']

    for palabra in palabras:
        if len(palabra) < 4: continue # Evitar mutar palabras muy cortas
        
        variaciones_casing = {palabra.lower(), palabra.upper(), palabra.capitalize()}
        
        palabras_a_mutar = set(variaciones_casing)
        for p in variaciones_casing:
            # Aplicar leetspeak
            temp_mutaciones = {p}
            for letra, reemplazos in mapa_leetspeak_avanzado.items():
                if letra in p.lower():
                    for r in reemplazos:
                        # Añadir mutaciones reemplazando la primera ocurrencia
                        temp_mutaciones.add(p.lower().replace(letra, r, 1))
                        # Y con la primera letra en mayúscula
                        capitalized_mut = p.lower().replace(letra, r, 1).capitalize()
                        temp_mutaciones.add(capitalized_mut)
            palabras_a_mutar.update(temp_mutaciones)

        for mutada in list(palabras_a_mutar):
            resultados.add(mutada)
            for simbolo in simbolos_finales:
                resultados.add(mutada + simbolo)
            resultados.add(mutada + "123")
            resultados.add(mutada + str(datetime.now().year)[-2:]) # ej. 23
            resultados.add(mutada + str(datetime.now().year)) # ej. 2023

    return resultados

def generar_combinaciones_argentinas(palabras_base):
    """Combina palabras con nombres, lugares y modismos argentinos."""
    resultados = set()
    fuentes = NOMBRES_PROPIOS + LUGARES_FAMOSOS + MODISMOS_ARGENTINOS + EQUIPOS_FUTBOL
    
    for palabra in palabras_base:
        for item in fuentes:
            resultados.add(palabra + item)
            resultados.add(item + palabra)
            
    for nombre in NOMBRES_PROPIOS:
        for apellido in APELLIDOS_COMUNES:
            resultados.add(nombre + apellido)
            resultados.add(f"{nombre}.{apellido}")
            resultados.add(f"{nombre}_{apellido}")

    return resultados

def generar_patrones_numericos():
    """Genera secuencias numéricas comunes."""
    resultados = set()
    for i in range(10):
        resultados.add(str(i) * 4)
        resultados.add(str(i) * 5)
    
    comunes = ["123456", "123456789", "654321", "147258", "2580", "369", "123123", "456456", "789789"]
    resultados.update(comunes)
    
    # Fechas de nacimiento comunes
    for ano in range(1970, datetime.now().year + 1):
        resultados.add(str(ano))
        for mes in range(1, 13):
            for dia in range(1, 29): # Simplificado a 28 días para evitar fechas inválidas
                resultados.add(f"{dia:02d}{mes:02d}{ano}")
                resultados.add(f"{dia}{mes}{str(ano)[-2:]}")

    return resultados

def generar_patrones_teclado_qwerty():
    """Genera patrones de teclas adyacentes en un teclado QWERTY."""
    resultados = set()
    filas = ["1234567890", "qwertyuiop", "asdfghjkl", "zxcvbnm"]
    
    for fila in filas:
        for i in range(len(fila) - 2):
            resultados.add(fila[i:i+3])
            if i < len(fila) - 3:
                resultados.add(fila[i:i+4])
    
    resultados.update(["123qwe", "qwe123", "asdzxc", "zxcvbnm", "qazwsx", "edcrfv"])
    return resultados

def generar_patrones_teclado_telefono():
    """Genera patrones numéricos comunes en teclados de teléfono."""
    resultados = set()
    patrones = [
        "2580", "0852", "147", "741", "369", "963", "123", "456", "789",
        "25802580", "123123", "112233", "445566", "778899"
    ]
    resultados.update(patrones)
    return resultados

def combinar_con_fechas(palabras):
    """Combina palabras con fechas comunes."""
    resultados = set()
    for palabra in palabras:
        for ano in range(2000, datetime.now().year + 2):
            resultados.add(f"{palabra}{ano}")
            resultados.add(f"{palabra}{str(ano)[-2:]}")
        for dia in range(1, 32):
            resultados.add(f"{palabra}{dia}")
    return resultados

def generar_variaciones_wifi(ssid):
    if not ssid: return set()
    print(f"[*] Generando variaciones para el Wi-Fi: {ssid}...")
    palabras = [ssid, ssid.lower(), ssid.capitalize()]
    resultados = set(palabras)
    resultados.update(anadir_numeros(palabras))
    resultados.update(sustituir_letras(palabras))
    resultados.update(mutacion_compleja(palabras))
    return resultados

def generar_variaciones_nombres_apellidos():
    resultados = set()
    for nombre in NOMBRES_PROPIOS:
        for apellido in APELLIDOS_COMUNES:
            # ej. juanperez, JuanPerez, juanperez123, Juan.Perez2023!
            combos = {nombre + apellido, nombre.capitalize() + apellido.capitalize()}
            resultados.update(combos)
            resultados.update(anadir_numeros(combos))
            resultados.update(mutacion_compleja(combos))
    return resultados

def generar_contrasenas_tendencia():
    return mutacion_compleja(TEMAS_TENDENCIA)

def analizar_patrones_existentes(archivo_existente):
    print(f"[*] ADVERTENCIA: La función de análisis de patrones desde '{archivo_existente}' es compleja y no está implementada en esta versión.")
    return set()

def main():
    parser = argparse.ArgumentParser(
        description="Generador de Super Diccionarios de Contraseñas v4.0 - Edición Potenciada",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Ejemplos de uso:
  # Generar diccionario estándar
  python generador_avanzado_contraseñas.py -o mi_diccionario.txt

  # Generar diccionario para un Wi-Fi específico
  python generador_avanzado_contraseñas.py --wifi "MiRedWifi" -o wifi_pass.txt
"""
    )
    parser.add_argument("-o", "--output", default="super_diccionario_avanzado.txt", help="Nombre del archivo de salida.")
    parser.add_argument("--wifi", help="Nombre de la red Wi-Fi (SSID) para generar variaciones específicas.")
    parser.add_argument("--analizar", help="[NO IMPLEMENTADO] Ruta a un archivo de contraseñas existente para análisis de patrones.")
    
    args = parser.parse_args()
    print("[*] Iniciando la generación del SUPER diccionario (Versión 4.0 Potenciada)...")
    
    contrasenas_generadas = set()

    print("[*] Capa 1: Añadiendo palabras base originales...")
    contrasenas_generadas.update(PALABRAS_BASE)

    print("[*] Capa 2: Aplicando mutaciones numéricas y de leetspeak simple...")
    contrasenas_generadas.update(anadir_numeros(PALABRAS_BASE))
    contrasenas_generadas.update(sustituir_letras(PALABRAS_BASE))

    print("[*] Capa 3: Aplicando mutaciones complejas avanzadas (casing, símbolos, años)...")
    contrasenas_generadas.update(mutacion_compleja(PALABRAS_BASE))

    print("[*] Capa 4: Generando combinaciones con datos de Argentina (nombres, lugares, modismos)...")
    contrasenas_generadas.update(generar_combinaciones_argentinas(PALABRAS_COMUNES))

    print("[*] Capa 5: Generando patrones numéricos (secuencias, fechas de nacimiento)...")
    contrasenas_generadas.update(generar_patrones_numericos())

    print("[*] Capa 6: Generando patrones de teclado QWERTY y de teléfono...")
    contrasenas_generadas.update(generar_patrones_teclado_qwerty())
    contrasenas_generadas.update(generar_patrones_teclado_telefono())

    print("[*] Capa 7: Generando variaciones de nombres y apellidos...")
    contrasenas_generadas.update(generar_variaciones_nombres_apellidos())

    print("[*] Capa 8: Generando contraseñas basadas en tendencias y cultura popular...")
    contrasenas_generadas.update(generar_contrasenas_tendencia())
    
    print("[*] Capa 9: Combinando palabras base con fechas comunes...")
    contrasenas_generadas.update(combinar_con_fechas(PALABRAS_BASE))

    if args.wifi:
        print(f"[*] Capa 10: Generando variaciones específicas para Wi-Fi: {args.wifi}...")
        contrasenas_generadas.update(generar_variaciones_wifi(args.wifi))

    if args.analizar:
        contrasenas_generadas.update(analizar_patrones_existentes(args.analizar))

    print(f"\n[*] Compilando y escribiendo {len(contrasenas_generadas)} contraseñas únicas. Esto puede tardar...")
    try:
        with open(args.output, 'w', encoding='utf-8', errors='ignore') as f:
            # Usamos una lista para ordenar y luego escribimos
            lista_ordenada = sorted(list(contrasenas_generadas))
            for pwd in lista_ordenada:
                f.write(pwd + '\n')
        print(f"\n[+] ¡SUPER DICCIONARIO POTENCIADO FINALIZADO!")
        print(f"[+] Se generó el archivo con {len(contrasenas_generadas)} contraseñas.")
        print(f"[+] Archivo guardado en: {args.output}")
    except IOError as e:
        print(f"\n[!] Error al escribir en el archivo: {e}")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Datos del viaje a Escocia (18-23 agosto 2026).
Fuentes: plan de Gemini + horarios/precios oficiales verificados (Historic Environment Scotland,
Scottish Canals, NTS) en agosto 2026.
"""

TITULO = "Escocia 2026 · Ruta de 6 días"
SUBTITULO = "Base: Blairgowrie Holiday Park · Llegada Glasgow 18/08 09:00 · Vuelta a Alicante 23/08 18:15"

# ---------------------------------------------------------------------------
# SITIOS
# ---------------------------------------------------------------------------
SITIOS = {
    "Glasgow Airport": {
        "lat": 55.8700415, "lon": -4.4345433,
        "categoria": "✈️ Aeropuerto",
        "rating": None,
        "descripcion": "Aeropuerto internacional de Glasgow (GLA). Llegada el día 1 a las 9:00 y salida el día 6 a las 18:15.",
        "que_ver": ["Recogida de equipaje y coche de alquiler (previsto listo ~10:00)", "Tocar el freno: cafetería antes de arrancar la ruta"],
        "horario": "24 h",
        "precio": "—",
    },
    "The Falkirk Wheel": {
        "lat": 56.000782, "lon": -3.840998,
        "categoria": "⚙️ Atracción turística",
        "rating": 4.6,
        "descripcion": "El único ascensor rotatorio de barcos del mundo: conecta el canal Forth & Clyde con el canal Unión elevando barcos 35 metros. Una pieza de ingeniería única en pleno funcionamiento.",
        "que_ver": ["Ver el mecanismo rotativo en funcionamiento (gratis desde el exterior)", "Paseo en barco 'Original Tour' (50-60 min) con salidas cada ~40 min", "Café y tienda en el visitor centre"],
        "horario": "9:45 – 18:00 (1 jun – 15 sep)",
        "precio": "Exterior gratis · Barco ~£15.70–17.70 adulto",
        "nota": "No es imprescindible el paseo en barco; solo verlo girar desde fuera ya justifica la visita.",
    },
    "The Kelpies": {
        "lat": 56.0192301, "lon": -3.7556985,
        "categoria": "🐴 Escultura",
        "rating": 4.7,
        "descripcion": "Dos cabezas de caballo monumentales de acero de 30 m, obra de Andy Scott, en el parque The Helix. La escultura pública más grande de Escocia.",
        "que_ver": ["Fotos de las cabezas de caballo (la estructura impone muchísimo)", "Parque The Helix con rutas a pie", "Tours guiados al interior (se reservan con antelación)"],
        "horario": "Exterior 24 h · Visitor centre ~9:00 – 16:00",
        "precio": "Gratis · Parking The Helix gratis (el de al lado, de pago)",
        "nota": "Parada exprés de 20-30 min: suficiente para fotos. Muy cerca de la Rueda de Falkirk (10-15 min en coche).",
    },
    "Stirling Castle": {
        "lat": 56.122907, "lon": -3.9455615,
        "categoria": "🏰 Castillo",
        "rating": 4.6,
        "descripcion": "Uno de los castillos más importantes de Escocia, en la roca que domina Stirling. Corazón de las guerras de independencia: aquí se coronó María Estuardo en 1543.",
        "que_ver": ["Royal Palace y sus salas con actores de época", "Great Hall, el salón medieval más grande de Escocia", "Vistas del valle y el monumento a William Wallace", "Capilla Real y jardines Queen Anne"],
        "horario": "9:30 – 18:00 (abr–sep) · Última entrada 17:00",
        "precio": "£18.50 online · £20.50 en taquilla · Parking esplanade £4 (se llena pronto)",
        "nota": "Si vas justo de tiempo, el castillo visto desde el exterior + subida al monumento de Wallace ya valen la pena.",
    },
    "Doune Castle": {
        "lat": 56.1851989, "lon": -4.0499458,
        "categoria": "🏰 Castillo",
        "rating": 4.5,
        "descripcion": "Fortaleza medieval del siglo XIV con un estado de conservación sobresaliente. Escenario de rodaje de Outlander, Juego de Tronos y 'Los Caballeros de la Mesa Cuadrada' (Monty Python).",
        "que_ver": ["Gran salón y cocina medieval con guiños a las series grabadas allí", "Audioguía gratuita con humor de Monty Python", "Vistas del valle del Teith"],
        "horario": "9:30 – 17:30 (jun–sep) · Última entrada 16:45",
        "precio": "£10.00 online · £11.00 en taquilla",
    },
    "Blairgowrie Holiday Park": {
        "lat": 56.5990127, "lon": -3.3351506,
        "categoria": "🏕️ Alojamiento (base)",
        "rating": 4.5,
        "descripcion": "Tu base de operaciones durante los 6 días, en Rattray, a las afueras de Blairgowrie (Perthshire). Ideal como centro para las rutas diarias.",
        "que_ver": ["Check-in y descanso", "Supermercado y servicios del parque"],
        "horario": "Recepción típica 9:00 – 21:00",
        "precio": "Ya reservado",
    },
    "Edinburgh Castle": {
        "lat": 55.9485947, "lon": -3.1999135,
        "categoria": "🏰 Castillo",
        "rating": 4.6,
        "descripcion": "El castillo más visitado de Escocia, sobre la roca volcánica que domina la Royal Mile. Mil años de historia como fortaleza y residencia real.",
        "que_ver": ["Crown Jewels y la Piedra del Destino", "Cañón One O'Clock Gun (dispara a las 13:00)", "Capilla de Santa Margarita (lo más antiguo de Edimburgo)", "National War Museum"],
        "horario": "9:30 – 18:00 (abr–sep) · Última entrada 17:00",
        "precio": "Desde ~£22.50 adulto online (compra anticipada recomendada)",
        "nota": "En agosto el Military Tattoo acorta el horario algunos días (8, 15, 22, 28 y 29). El 19/08 el horario es normal. Compra las entradas online con antelación: se agotan.",
    },
    "Edimburgo Centro": {
        "lat": 55.953252, "lon": -3.188267,
        "categoria": "🏙️ Ciudad",
        "rating": None,
        "descripcion": "La capital: Royal Mile, casco antiguo medieval y New Town georgiano. En agosto está en pleno Festival Fringe (el mayor festival de artes del mundo).",
        "que_ver": ["Royal Mile y Grassmarket", "Palacio de Holyroodhouse (extremo de la Royal Mile)", "Calton Hill (vistas panorámicas)", "Princes Street Gardens", "Si hay tiempo: Arthur's Seat, el volcán extinto en el centro"],
        "horario": "Ciudad abierta · Festival Fringe en agosto",
        "precio": "A pie, gratis (castillos y museos aparte)",
    },
    "Inverness": {
        "lat": 57.477773, "lon": -4.224721,
        "categoria": "🏙️ Ciudad",
        "rating": None,
        "descripcion": "Capital de las Highlands, a orillas del río Ness. Punto de partida natural hacia el Lago Ness y el norte.",
        "que_ver": ["Catedral de Inverness y orillas del río Ness", "Castillo de Inverness (actual sede de tribunales)", "Old Town y pub culture", "Parada rápida para comer"],
        "horario": "Ciudad abierta",
        "precio": "—",
    },
    "Urquhart Castle": {
        "lat": 57.3241399, "lon": -4.4420012,
        "categoria": "🏰 Castillo",
        "rating": 4.5,
        "descripcion": "Imponentes ruinas del siglo XIII a orillas del Lago Ness, en Drumnadrochit. Una de las mejores perspectivas del lago y sede del famoso 'monstruo'.",
        "que_ver": ["Torreón (Grant Tower) con vistas al Lago Ness", "Trabuquete (trebuchet) a tamaño real", "Centro de visitantes con tienda y cafetería", "Mirador del lago para buscar a Nessie"],
        "horario": "9:30 – 20:15 (abr–ago) · Última entrada 19:15",
        "precio": "£14.00 online · £16.00 en taquilla",
    },
    "St Andrews Cathedral": {
        "lat": 56.3395621, "lon": -2.788475,
        "categoria": "⛪ Ruinas históricas",
        "rating": 4.6,
        "descripcion": "Restos de la catedral más grande de Escocia (consagrada en 1318 con Robert the Bruce presente), junto al mar del Norte. Las murallas del recinto son de las mejor conservadas del país.",
        "que_ver": ["Ruinas de la catedral junto a los acantilados", "Torre de St Rule (subida con guía, se reserva por teléfono)", "Museo con escultura medieval (en obras en 2026)", "Paseo por el mar y la playa de West Sands"],
        "horario": "9:30 – 17:30 (abr–sep) · Última entrada 16:45",
        "precio": "Gratis en 2026 (museo y torre cerrados por restauración)",
        "nota": "En 2026 las ruinas son de acceso gratuito. También merece la pena el castillo y el Old Course al lado.",
    },
    "Glencoe Visitor Centre": {
        "lat": 56.6717904, "lon": -5.0826363,
        "categoria": "🌲 Reserva natural",
        "rating": 4.6,
        "descripcion": "Centro de visitantes del National Trust for Scotland al pie del valle de Glencoe, con 8 Munros (montañas de +914 m) alrededor. Paisajes de película (Skyfall, Harry Potter, Braveheart).",
        "que_ver": ["Exposición y mapa 3D del valle", "Película 'The Glen Revealed' (cada hora)", "Casa turf & creel reconstruida (siglo XVII)", "Café Highland Coo y tienda", "Glen Etive: desvío de single track al valle salvaje (opcional)"],
        "horario": "9:30 – 17:30 · Café hasta 16:00",
        "precio": "Entrada gratis · Parking £4 (gratis para miembros NTS)",
    },
    "Oban": {
        "lat": 56.415157, "lon": -5.471047,
        "categoria": "🏘️ Ciudad costera",
        "rating": None,
        "descripcion": "La 'puerta de las islas': bonita ciudad costera del oeste con el anfiteatro McCaig's Tower coronando la colina. Ideal para ver el atardecer sobre el mar.",
        "que_ver": ["McCaig's Tower (réplica del Coliseo, vistas al puerto)", "Paseo marítimo y fish & chips", "Destilería Oban (whisky, junto al puerto)", "Atardecer sobre la bahía"],
        "horario": "Ciudad abierta",
        "precio": "—",
        "nota": "Si el cansancio aprieta tras Glencoe, la vuelta directa a la base también es válida (~3h).",
    },
    "Luss": {
        "lat": 56.101491, "lon": -4.6422516,
        "categoria": "🏘️ Pueblo",
        "rating": None,
        "descripcion": "Pintoresco pueblo de piedra a orillas del Loch Lomond, a solo 25 min del aeropuerto de Glasgow. El broche de naturaleza perfecto para el último día.",
        "que_ver": ["Paseo por las orillas del lago (3h con calma)", "Casas de piedra con flores", "Mirador y picnic", "Comer tranquilamente en el pueblo"],
        "horario": "Pueblo abierto",
        "precio": "Gratis",
        "nota": "Plan del día 6: salir 9:30 de la base, llegar a Luss 11:15, salir a las 14:45 hacia el aeropuerto (15:20) para el vuelo de 18:15.",
    },
}

# ---------------------------------------------------------------------------
# RUTAS DE GOOGLE MAPS (extraídas de la conversación de Gemini — enlaces
# 'Ver mapa detallado' con todos los puntos intermedios)
# ---------------------------------------------------------------------------
MAPS = {
    1: "https://www.google.com/maps/dir/Glasgow+Airport,+Glasgow,+Paisley,+United+Kingdom/The+Falkirk+Wheel,+Lime+Road,+Falkirk,+United+Kingdom/The+Kelpies,+269W%2BF7+The+Helix,+Grangemouth,+Falkirk,+United+Kingdom/Stirling+Castle,+Castle+Wynd,+Stirling,+United+Kingdom/Doune+Castle,+Castle+Hill,+Doune,+United+Kingdom/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/data=!4m38!4m37!1m5!1m1!19sChIJ3eARAblOiEgRCzOqGbWIqCQ!2m2!1d-4.4345433!2d55.8700415!1m5!1m1!19sChIJrfWr3_l6iEgRWSwGuUFI4TQ!2m2!1d-3.840998!2d56.000782!1m5!1m1!19sChIJI7mOEHd5iEgR97zKUkBuhTw!2m2!1d-3.7556985!2d56.019230099999994!1m5!1m1!19sChIJp9U8KJJiiEgRZ_tBFfsEUHw!2m2!1d-3.9455614999999997!2d56.122907!1m5!1m1!19sChIJv_zkTdKLiEgROfu3YQrTmVU!2m2!1d-4.0499458!2d56.185198899999996!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!3e0",
    2: "https://www.google.com/maps/dir/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/Edinburgh+Castle,+Castlehill,+Edinburgh,+United+Kingdom/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/data=!4m20!4m19!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!1m5!1m1!19sChIJ98CZIJrHh0gRWApM5esemkY!2m2!1d-3.1999134999999996!2d55.9485947!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!3e0",
    3: "https://www.google.com/maps/dir/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/Inverness,+UK/Urquhart+Castle,+Drumnadrochit,+Inverness,+United+Kingdom/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/data=!4m26!4m25!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!1m5!1m1!19sChIJK94XLVtxj0gRPcQ-LtEJQ2I!2m2!1d-4.224721!2d57.477773!1m5!1m1!19sChIJC2d4AeITj0gR8C09zc8mYZk!2m2!1d-4.4420012!2d57.3241399!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!3e0",
    4: "https://www.google.com/maps/dir/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/St+Andrews+Cathedral,+The+Pends,+St+Andrews,+United+Kingdom/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/data=!4m20!4m19!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!1m5!1m1!19sChIJwxsqb5JXhkgRACV-YwroMQ8!2m2!1d-2.788475!2d56.339562099999995!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!3e0",
    5: "https://www.google.com/maps/dir/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/Glencoe+Visitor+Centre+-+National+Trust+for+Scotland,+Visitor+Centre,+Glencoe,+Ballachulish,+United+Kingdom/Oban,+UK/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/data=!4m26!4m25!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!1m5!1m1!19sChIJGadfB9IwiUgRA52_MNCOR9g!2m2!1d-5.0826363!2d56.6717904!1m5!1m1!19sChIJwfHd0tBBiUgRN8KPgf9K3YM!2m2!1d-5.4710469999999995!2d56.415157!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!3e0",
    6: "https://www.google.com/maps/dir/Blairgowrie+Holiday+Park,+Hatton+Road,+Rattray,+Blairgowrie,+United+Kingdom/Luss,+UK/Glasgow+Airport,+Glasgow,+Paisley,+United+Kingdom/data=!4m20!4m19!1m5!1m1!19sChIJh2KqanAUhkgR0YyjIaFwoBk!2m2!1d-3.3351506!2d56.599012699999996!1m5!1m1!19sChIJDSs0_IeqiUgRPm_72NtfzV8!2m2!1d-4.6422516!2d56.101490999999996!1m5!1m1!19sChIJ3eARAblOiEgRCzOqGbWIqCQ!2m2!1d-4.4345433!2d55.8700415!3e0",
}

# ---------------------------------------------------------------------------
# DÍAS
# ---------------------------------------------------------------------------
DIAS = [
    {
        "dia": 1, "fecha": "18/08 · Martes", "titulo": "De Glasgow a la base (ruta de llegada)",
        "lema": "Rueda de Falkirk → Kelpies → Stirling → Doune → Blairgowrie",
        "resumen": "Llegada a las 9:00, coche listo ~10:00. Ruta optimizada en subida hacia el alojamiento: ingeniería, esculturas y dos castillos.",
        "conduccion": "~2 h 37 min · 175 km (109 mi)",
        "paradas": ["Glasgow Airport", "The Falkirk Wheel", "The Kelpies", "Stirling Castle", "Doune Castle", "Blairgowrie Holiday Park"],
        "detalle": [
            "09:00 — Aterrizaje en Glasgow y recogida del coche (~10:00).",
            "10:45 — The Falkirk Wheel (45 min desde el aeropuerto por M8/M80). Primera parada técnica.",
            "11:15 — The Kelpies (10-15 min). Parada exprés de fotos.",
            "12:00 — Castillo de Stirling (25 min). Entrada + visita.",
            "13:45 — Castillo de Doune (15 min). Parada medieval.",
            "15:15 — Blairgowrie Holiday Park (1 h 15 directos). Check-in y descanso.",
        ],
    },
    {
        "dia": 2, "fecha": "19/08 · Miércoles", "titulo": "Edimburgo, la capital",
        "lema": "Ida y vuelta a Edimburgo desde la base",
        "resumen": "Día completo en la capital: Castillo de Edimburgo por la mañana temprano y Royal Mile. El regreso nocturno es directo (1h30).",
        "conduccion": "~3 h total (1 h 30 por trayecto)",
        "paradas": ["Blairgowrie Holiday Park", "Edinburgh Castle", "Edimburgo Centro", "Blairgowrie Holiday Park"],
        "detalle": [
            "09:00 — Salida de la base hacia Edimburgo.",
            "10:30 — Castillo de Edimburgo (abre 9:30): ve directo a las Crown Jewels, se llenan rápido. El One O'Clock Gun dispara a las 13:00.",
            "13:30 — Royal Mile, Grassmarket y comida.",
            "15:30 — Calton Hill o Princes Street Gardens.",
            "17:30 — Regreso a la base (1h30).",
            "💡 En agosto el centro está a tope por el Festival Fringe; aparca en un Park & Ride y entra en bus.",
        ],
    },
    {
        "dia": 3, "fecha": "20/08 · Jueves", "titulo": "Las Highlands: Inverness y Lago Ness",
        "lema": "Día fuerte al norte: Inverness → Urquhart → Lago Ness",
        "resumen": "La gran tirada del viaje, puesta a mitad de semana para no arriesgar el vuelo. Inverness, el Lago Ness y el castillo en ruinas más fotografiado de Escocia.",
        "conduccion": "~4 h 30 min total",
        "paradas": ["Blairgowrie Holiday Park", "Inverness", "Urquhart Castle", "Blairgowrie Holiday Park"],
        "detalle": [
            "08:30 — Salida hacia Inverness (2h15).",
            "10:45 — Inverness: paseo por el río Ness, catedral y comida.",
            "12:30 — Castillo de Urquhart (40 min desde Inverness). Abierto hasta las 20:15: hay margen.",
            "15:00 — Vuelta a la base (2h15 por la A9).",
            "⚠️ Lleva tiempo de margen: la A9 es la vía más transitada de las Highlands.",
        ],
    },
    {
        "dia": 4, "fecha": "21/08 · Viernes", "titulo": "Costa Este: St Andrews",
        "lema": "Día relajado en la cuna del golf",
        "resumen": "Jornada suave: ruinas de la catedral junto al mar, el Old Course y acantilados. Opcional por la mañana: Dunkeld y The Hermitage, a 30 min de la base.",
        "conduccion": "~2 h 30 min total",
        "paradas": ["Blairgowrie Holiday Park", "St Andrews Cathedral", "Blairgowrie Holiday Park"],
        "detalle": [
            "Opcional AM — Dunkeld y The Hermitage (sendero junto al río, cascada y abetos gigantes).",
            "10:30 — Salida a St Andrews (1h).",
            "11:30 — Catedral en ruinas (gratis en 2026) y paseo por los acantilados.",
            "13:30 — Old Course y casco histórico; comida.",
            "16:30 — Regreso a la base (1h).",
        ],
    },
    {
        "dia": 5, "fecha": "22/08 · Sábado", "titulo": "El Oeste Volcánico: Glencoe y Oban",
        "lema": "El día más espectacular (y exigente)",
        "resumen": "Glencoe, el valle más dramático de Escocia, y si hay energía, Oban al atardecer. Paisajes de película: la A82 bordea el Loch Lomond de camino.",
        "conduccion": "~5 h total (con Oban) · ~3 h 30 solo Glencoe",
        "paradas": ["Blairgowrie Holiday Park", "Glencoe Visitor Centre", "Oban", "Blairgowrie Holiday Park"],
        "detalle": [
            "08:30 — Salida (2h30 hasta Glencoe). La A82 bordea el Loch Lomond: el lago se ve de forma natural.",
            "11:00 — Glencoe Visitor Centre: exposición, casa turf & creel y café. Opcional: desvío a Glen Etive (single track salvaje).",
            "14:30 — Si hay fuerzas, Oban (45 min): McCaig's Tower y atardecer. La vuelta a la base serán ~3h.",
            "21:30 — Llegada a la base.",
            "💡 Si el cansancio aprieta, vuelve directo de Glencoe (~3h) y te saltas Oban.",
        ],
    },
    {
        "dia": 6, "fecha": "23/08 · Domingo", "titulo": "Retorno seguro: Loch Lomond y aeropuerto",
        "lema": "Despedida con naturaleza, sin estrés",
        "resumen": "Check-out, paseo por Luss a orillas del Loch Lomond, comida tranquila y llegada al aeropuerto con 3h de margen para el vuelo de las 18:15.",
        "conduccion": "~2 h 30 min total",
        "paradas": ["Blairgowrie Holiday Park", "Luss", "Glasgow Airport"],
        "detalle": [
            "09:30 — Check-out y salida de la base.",
            "11:15 — Llegada a Luss (1h45 por la A82).",
            "11:15–14:45 — Paseo por las orillas del lago, fotos en el mirador y comida tranquila.",
            "14:45 — Salida hacia el aeropuerto (25 min por la A82).",
            "15:20 — Llegada a Glasgow: repostar, devolver el coche, controles.",
            "18:15 — Vuelo a Alicante. ✈️",
        ],
    },
]

def sitio(nombre: str) -> dict:
    return SITIOS[nombre]

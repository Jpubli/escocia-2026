# 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia 2026 — Ruta de 6 días

Web interactiva con el plan de viaje a Escocia (18–23 agosto 2026): una pestaña por día con
mapa de la ruta, paradas numeradas, horarios, precios y enlace directo a Google Maps.

- **Base:** Blairgowrie Holiday Park (Perthshire)
- **Llegada:** Glasgow Airport, 18/08 a las 9:00
- **Salida:** Glasgow Airport, 23/08 a las 18:15 (Alicante)

## Estructura

- `app.py` — aplicación Streamlit
- `data.py` — datos de sitios, días y enlaces de Google Maps
- `rutas.json` — geometrías de ruta (OSRM) por día
- `build_routes.py` — regenera `rutas.json` vía OSRM (fallback: línea recta)

## Ejecutar en local

```bash
python -m venv venv
venv/bin/python -m pip install -r requirements.txt
venv/bin/python -m streamlit run app.py
```

## Deploy en Streamlit Community Cloud

1. Sube este repo a GitHub (público).
2. Entra en https://share.streamlit.io y conecta tu cuenta de GitHub.
3. **New app** → repo `escocia-2026` → **Main file path:** `app.py` → **Deploy**.

Fuentes de horarios/precios: Historic Environment Scotland, Scottish Canals, National Trust for
Scotland (verificadas en agosto 2026). El plan original se elaboró con Gemini.

# -*- coding: utf-8 -*-
"""Escocia 2026 — Ruta de 6 días. App Streamlit con mapa interactivo por día."""
import json
import os

import folium
import streamlit as st
from streamlit_folium import st_folium

import data

st.set_page_config(page_title="Escocia 2026 · Ruta", page_icon="🗺️", layout="wide")

# ---------------------------------------------------------------- rutas
_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_DIR, "rutas.json")) as f:
    RUTAS = json.load(f)

# ---------------------------------------------------------------- estilo
st.markdown(
    """
    <style>
    .block-container {padding-top: 1.6rem;}
    .dia-header {border-left: 5px solid #1f6feb; padding-left: 12px; margin-bottom: 4px;}
    .dia-header h2 {margin: 0; font-size: 1.7rem;}
    .dia-lema {color: #586069; font-size: 1.02rem; margin-bottom: 10px;}
    .tarjeta {
        border: 1px solid #d0d7de; border-left: 4px solid #1f6feb;
        border-radius: 8px; padding: 10px 14px; margin: 6px 0;
        background: #f6f8fa;
    }
    .tarjeta .cat {font-size: 0.78rem; color: #57606a; text-transform: uppercase; letter-spacing: .4px;}
    .tarjeta .nom {font-size: 1.08rem; font-weight: 700; margin: 1px 0;}
    .tarjeta .rating {color: #e3b341; font-weight: 600;}
    .tarjeta .hor {font-size: 0.9rem; color: #1a7f37; font-weight: 600;}
    .tarjeta .pre {font-size: 0.9rem; color: #8250df; font-weight: 600;}
    .tarjeta .desc {font-size: 0.92rem; color: #24292f; margin-top: 4px;}
    .tarjeta .qv {font-size: 0.9rem; color: #24292f; margin: 3px 0 0 0; padding-left: 4px;}
    .tarjeta .qv li {margin: 1px 0;}
    .nota {background:#fff8c5; border:1px solid #eedc82; border-radius:6px; padding:8px 12px; font-size:0.9rem;}
    .timeline {font-size:0.95rem;}
    .timeline .t {color:#1f6feb; font-weight:700;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown("## 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia 2026")
    st.caption("18 – 23 agosto · 6 días en coche")
    opciones = {f"Día {d['dia']} · {d['fecha'][:5]} — {d['titulo']}": d for d in data.DIAS}
    eleccion = st.radio("Elige el día", list(opciones.keys()))
    dia = opciones[eleccion]
    st.divider()
    st.markdown("**Datos del viaje**")
    st.markdown("- ✈️ **Llegada:** Glasgow, 18/08, 09:00")
    st.markdown("- 🏕️ **Base:** Blairgowrie Holiday Park")
    st.markdown("- ✈️ **Vuelta:** 23/08, 18:15 (Alicante)")
    st.divider()
    st.caption("Plan acordado con Gemini · Horarios y precios verificados (ago 2026) · Rutas de Google Maps")

# ---------------------------------------------------------------- header día
st.markdown(
    f"<div class='dia-header'><h2>Día {dia['dia']} · {dia['fecha']} — {dia['titulo']}</h2></div>",
    unsafe_allow_html=True,
)
st.markdown(f"<div class='dia-lema'>{dia['lema']}</div>", unsafe_allow_html=True)
st.markdown(dia["resumen"])

c1, c2, c3 = st.columns(3)
c1.metric("🚗 Conducción", dia["conduccion"])
c2.metric("📍 Paradas", len(dia["paradas"]))
km = RUTAS[str(dia["dia"])].get("distance_km")
c3.metric("📏 Ruta OSRM", f"{km} km" if km else "—")

if dia.get("nota_extra"):
    st.markdown(f"<div class='nota'>💡 {dia['nota_extra']}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------- mapa
st.subheader("🗺️ Mapa de la ruta")
st.link_button("Abrir ruta en Google Maps", data.MAPS[dia["dia"]], type="primary")

def hacer_mapa(dia_idx):
    ruta = RUTAS[str(dia_idx)]
    geom = ruta["geometry"]  # [[lon, lat], ...]
    paradas = dia["paradas"]

    centro = [sum(p[1] for p in geom) / len(geom), sum(p[0] for p in geom) / len(geom)]
    m = folium.Map(location=centro, zoom_start=8, tiles="OpenStreetMap",
                   control_scale=True)

    # ruta: contorno blanco + línea azul
    folium.PolyLine(geom, color="#ffffff", weight=7, opacity=0.9).add_to(m)
    folium.PolyLine(geom, color="#1f6feb", weight=4, opacity=0.95).add_to(m)

    # paradas numeradas
    for i, nombre in enumerate(paradas, start=1):
        s = data.SITIOS[nombre]
        es_base = nombre == "Blairgowrie Holiday Park"
        color = "#e8590c" if es_base else "#1f6feb"
        icon = folium.DivIcon(
            html=(
                f"<div style='background:{color};color:#fff;border:2px solid #fff;"
                f"border-radius:50%;width:26px;height:26px;display:flex;align-items:center;"
                f"justify-content:center;font-weight:700;font-size:13px;"
                f"box-shadow:0 1px 4px rgba(0,0,0,.4)'>{'🏠' if es_base else i}</div>"
            )
        )
        folium.Marker([s["lat"], s["lon"]], icon=icon, tooltip=nombre,
                      popup=f"<b>{i}. {nombre}</b>").add_to(m)

    # ajustar vista al bbox de la ruta
    lats = [p[1] for p in geom]
    lons = [p[0] for p in geom]
    m.fit_bounds([[min(lats), min(lons)], [max(lats), max(lons)]], padding=(30, 30))
    return m

st_folium(hacer_mapa(dia["dia"]), width="100%", height=520)

# ---------------------------------------------------------------- timeline
st.subheader("🕐 Plan del día")
timeline = "".join(
    f"<div class='timeline'><span class='t'>{linea.split(' — ')[0]}</span> — "
    f"{linea.split(' — ', 1)[1] if ' — ' in linea else linea}</div>"
    for linea in dia["detalle"]
)
st.markdown(timeline, unsafe_allow_html=True)

# ---------------------------------------------------------------- paradas
st.subheader("📍 Paradas y sitios")
for i, nombre in enumerate(dia["paradas"], start=1):
    s = data.SITIOS[nombre]
    rating = f"<span class='rating'>★ {s['rating']}</span>" if s["rating"] else ""
    qv = "<ul class='qv'>" + "".join(f"<li>{q}</li>" for q in s["que_ver"]) + "</ul>"
    nota = f"<div class='nota'>💡 {s['nota']}</div>" if s.get("nota") else ""
    st.markdown(
        f"<div class='tarjeta'>"
        f"<div class='cat'>{s['categoria']} {rating}</div>"
        f"<div class='nom'>{i}. {nombre}</div>"
        f"<div class='hor'>🕘 {s['horario']} &nbsp;·&nbsp; <span class='pre'>💷 {s['precio']}</span></div>"
        f"<div class='desc'>{s['descripcion']}</div>"
        f"<div class='qv'><b>Qué ver:</b>{qv}</div>"
        f"{nota}"
        f"</div>",
        unsafe_allow_html=True,
    )

st.divider()
st.caption(
    "Plan original elaborado con Gemini (conversación del 12/08/2026) y enriquecido con horarios "
    "oficiales de Historic Environment Scotland, Scottish Canals y National Trust for Scotland. "
    "Los horarios pueden cambiar: compruébalos antes de cada visita."
)

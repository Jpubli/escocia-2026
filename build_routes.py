# -*- coding: utf-8 -*-
"""Calcula la geometría de cada ruta diaria con OSRM y la guarda en rutas.json.
Fallback: línea recta entre paradas si OSRM falla."""
import json
import time
import urllib.request

import data

ORDEN = {
    1: ["Glasgow Airport", "The Falkirk Wheel", "The Kelpies", "Stirling Castle", "Doune Castle", "Blairgowrie Holiday Park"],
    2: ["Blairgowrie Holiday Park", "Edinburgh Castle", "Blairgowrie Holiday Park"],
    3: ["Blairgowrie Holiday Park", "Inverness", "Urquhart Castle", "Blairgowrie Holiday Park"],
    4: ["Blairgowrie Holiday Park", "St Andrews Cathedral", "Blairgowrie Holiday Park"],
    5: ["Blairgowrie Holiday Park", "Glencoe Visitor Centre", "Oban", "Blairgowrie Holiday Park"],
    6: ["Blairgowrie Holiday Park", "Luss", "Glasgow Airport"],
}


def osrm_route(waypoints):
    coords = ";".join(f"{data.SITIOS[w]['lon']},{data.SITIOS[w]['lat']}" for w in waypoints)
    url = (f"https://router.project-osrm.org/route/v1/driving/{coords}"
           f"?overview=full&geometries=geojson")
    req = urllib.request.Request(url, headers={"User-Agent": "escocia-2026/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.loads(r.read().decode())
    if body.get("code") != "Ok" or not body.get("routes"):
        raise RuntimeError(f"OSRM code: {body.get('code')}")
    route = body["routes"][0]
    return route["geometry"]["coordinates"], route["distance"], route["duration"]


result = {}
ok = 0
for dia, waypoints in ORDEN.items():
    try:
        geom, dist_m, dur_s = osrm_route(waypoints)
        result[str(dia)] = {
            "geometry": geom,  # lista de [lon, lat]
            "distance_km": round(dist_m / 1000, 1),
            "duration_min": round(dur_s / 60),
            "source": "osrm",
        }
        ok += 1
        print(f"Día {dia}: OK · {result[str(dia)]['distance_km']} km · {result[str(dia)]['duration_min']} min")
    except Exception as e:
        print(f"Día {dia}: FALLBACK línea recta ({e})")
        geom = [[data.SITIOS[w]["lon"], data.SITIOS[w]["lat"]] for w in waypoints]
        result[str(dia)] = {"geometry": geom, "distance_km": None, "duration_min": None, "source": "straight"}
    time.sleep(1)

with open("rutas.json", "w") as f:
    json.dump(result, f)
print(f"\n{ok}/6 rutas con geometría real. Guardado en rutas.json")

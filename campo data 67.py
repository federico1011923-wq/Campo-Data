import streamlit as st

# ====================== DATOS ======================
datos = {
    "Buenos Aires": {
        "region": "Región Pampeana / Núcleo",
        "cultivos": ["Soja", "Maíz", "Trigo", "Girasol", "Cebada"],
        "costos": "USD 280 – 520 / ha",
        "costos_detalle": "Soja 1ª ≈ 300-320 USD/ha • Maíz ≈ 500-550 USD/ha • Trigo ≈ 350 USD/ha",
        "rendimiento": "Soja: 28-35 qq/ha • Maíz: 70-90 qq/ha • Trigo: 35-45 qq/ha (zona núcleo más alta)",
        "clima": "Templado húmedo. Precipitaciones 800-1100 mm/año. Veranos cálidos e inviernos suaves. Bastante soleado en verano."
    },
    "Córdoba": {
        "region": "Región Pampeana / Centro",
        "cultivos": ["Soja", "Maíz", "Trigo", "Maní", "Sorgo"],
        "costos": "USD 270 – 530 / ha",
        "costos_detalle": "Similar a zona núcleo. Maní tiene costos específicos más altos en algunas zonas.",
        "rendimiento": "Soja: 25-32 qq/ha • Maíz: 65-85 qq/ha • Maní: muy importante a nivel nacional",
        "clima": "Templado a subtropical seco hacia el oeste. Precipitaciones 600-900 mm. Veranos calurosos, inviernos fríos con heladas."
    },
    "Santa Fe": {
        "region": "Región Pampeana / Núcleo Norte",
        "cultivos": ["Soja", "Maíz", "Trigo", "Girasol"],
        "costos": "USD 280 – 540 / ha",
        "costos_detalle": "Zona de altos rendimientos. Costos de insumos y arrendamiento elevados.",
        "rendimiento": "Soja: 30-38 qq/ha • Maíz: 75-95 qq/ha (de los más altos del país)",
        "clima": "Templado húmedo. Lluvias 900-1100 mm. Veranos calurosos y húmedos. Buena disponibilidad hídrica."
    },
    "Entre Ríos": {
        "region": "Mesopotamia / Pampeana",
        "cultivos": ["Soja", "Maíz", "Trigo", "Arroz", "Cítricos"],
        "costos": "USD 260 – 500 / ha",
        "costos_detalle": "Arroz tiene costos de riego importantes.",
        "rendimiento": "Soja y maíz buenos. Arroz: zona importante del país.",
        "clima": "Templado húmedo a subtropical. Precipitaciones 1000-1300 mm. Bastante lluvioso."
    },
    "La Pampa": {
        "region": "Región Pampeana / Semiárida",
        "cultivos": ["Trigo", "Girasol", "Maíz", "Soja", "Cebada"],
        "costos": "USD 250 – 480 / ha",
        "costos_detalle": "Costos algo menores por menor intensidad de insumos en zonas marginales.",
        "rendimiento": "Más variables según zona este/oeste. Trigo y girasol destacados.",
        "clima": "Templado semiárido. Precipitaciones 400-700 mm. Muy soleado, inviernos fríos con heladas."
    },
    "Mendoza": {
        "region": "Cuyo",
        "cultivos": ["Vid (uva)", "Olivo", "Frutales", "Hortalizas"],
        "costos": "USD 800 – 2500+ / ha",
        "costos_detalle": "Viticultura de alto valor. Costos de riego y mano de obra elevados.",
        "rendimiento": "Uva de alta calidad (Malbec, etc.). Orientada a vinos de exportación.",
        "clima": "Árido continental. Precipitaciones 200-300 mm. Extremadamente soleado. Dependiente de riego."
    },
    "San Juan": {
        "region": "Cuyo",
        "cultivos": ["Vid", "Olivo", "Tomate", "Cebolla", "Frutales"],
        "costos": "USD 700 – 2200 / ha",
        "costos_detalle": "Similar a Mendoza, fuerte dependencia del riego.",
        "rendimiento": "Vid y hortalizas de alto valor. Importante en uva de mesa y pasas.",
        "clima": "Árido. Precipitaciones < 200 mm. Muy soleado y seco."
    },
    "Tucumán": {
        "region": "NOA",
        "cultivos": ["Caña de azúcar", "Limón", "Soja", "Maíz", "Arándanos"],
        "costos": "USD 400 – 1200 / ha",
        "costos_detalle": "Caña y limón son cultivos intensivos.",
        "rendimiento": "Principal productor de limón del país. Caña muy relevante.",
        "clima": "Subtropical. Precipitaciones 900-1400 mm. Veranos calurosos y húmedos."
    },
    "Salta": {
        "region": "NOA",
        "cultivos": ["Soja", "Maíz", "Poroto", "Tabaco", "Caña", "Cítricos"],
        "costos": "USD 280 – 600 / ha",
        "costos_detalle": "Zonas de secano y riego. Poroto destacado.",
        "rendimiento": "Soja y maíz en expansión. Importante en legumbres.",
        "clima": "Subtropical a árido según zona. Valles más secos, yungas muy lluviosas."
    },
    "Jujuy": {
        "region": "NOA",
        "cultivos": ["Caña de azúcar", "Tabaco", "Quinoa", "Hortalizas", "Cítricos"],
        "costos": "USD 350 – 900 / ha",
        "costos_detalle": "Caña y tabaco predominan en los valles.",
        "rendimiento": "Caña importante. Agricultura de altura en algunas zonas.",
        "clima": "Muy variado: subtropical en yungas, árido en la puna."
    },
    "Misiones": {
        "region": "NEA / Mesopotamia",
        "cultivos": ["Yerba mate", "Té", "Tabaco", "Mandioca", "Cítricos"],
        "costos": "USD 400 – 1000 / ha",
        "costos_detalle": "Yerba mate y té son cultivos perennes.",
        "rendimiento": "Principal productor de yerba mate junto a Corrientes.",
        "clima": "Subtropical húmedo. Precipitaciones 1600-2000+ mm. Muy lluvioso y húmedo."
    },
    "Corrientes": {
        "region": "NEA / Mesopotamia",
        "cultivos": ["Arroz", "Yerba mate", "Cítricos", "Soja", "Maíz"],
        "costos": "USD 300 – 700 / ha",
        "costos_detalle": "Arroz requiere riego/inundación.",
        "rendimiento": "Uno de los principales productores de arroz del país.",
        "clima": "Subtropical húmedo. Precipitaciones 1200-1600 mm."
    },
    "Chaco": {
        "region": "NEA",
        "cultivos": ["Algodón", "Soja", "Maíz", "Girasol", "Sorgo"],
        "costos": "USD 250 – 480 / ha",
        "costos_detalle": "Algodón tiene costos específicos de cosecha.",
        "rendimiento": "Históricamente algodonero. Soja y maíz en expansión.",
        "clima": "Subtropical. Precipitaciones 800-1200 mm. Veranos muy calurosos."
    },
    "Formosa": {
        "region": "NEA",
        "cultivos": ["Algodón", "Soja", "Maíz", "Arroz", "Banano"],
        "costos": "USD 240 – 450 / ha",
        "costos_detalle": "Agricultura más extensiva en algunas zonas.",
        "rendimiento": "Producción en crecimiento, especialmente granos.",
        "clima": "Subtropical cálido. Precipitaciones 1000-1400 mm."
    },
    "Santiago del Estero": {
        "region": "NOA / Chaco seco",
        "cultivos": ["Soja", "Maíz", "Algodón", "Poroto", "Girasol"],
        "costos": "USD 230 – 450 / ha",
        "costos_detalle": "Zonas de secano con costos relativamente bajos.",
        "rendimiento": "Soja y maíz importantes. Expansión agrícola notable.",
        "clima": "Subtropical seco a semiárido. Precipitaciones 500-800 mm. Muy soleado."
    },
    "Catamarca": {
        "region": "NOA / Cuyo norte",
        "cultivos": ["Olivo", "Vid", "Nogal", "Hortalizas", "Jojoa"],
        "costos": "USD 500 – 1500 / ha",
        "costos_detalle": "Cultivos de riego de alto valor.",
        "rendimiento": "Olivo y vid destacados.",
        "clima": "Árido. Precipitaciones muy bajas. Extremadamente soleado."
    },
    "La Rioja": {
        "region": "Cuyo",
        "cultivos": ["Vid", "Olivo", "Jojoa", "Nogal", "Hortalizas"],
        "costos": "USD 500 – 1600 / ha",
        "costos_detalle": "Viticultura y olivo con riego.",
        "rendimiento": "Vinos y aceitunas de calidad.",
        "clima": "Árido. Muy poca lluvia (<200 mm). Muy soleado y seco."
    },
    "San Luis": {
        "region": "Cuyo / Pampeana",
        "cultivos": ["Maíz", "Soja", "Girasol", "Maní", "Trigo"],
        "costos": "USD 260 – 500 / ha",
        "costos_detalle": "Zona de transición. Costos intermedios.",
        "rendimiento": "Maíz y soja buenos en el este. Maní presente.",
        "clima": "Templado semiárido. Precipitaciones 500-700 mm. Soleado."
    },
    "Neuquén": {
        "region": "Patagonia Norte",
        "cultivos": ["Frutales (pera, manzana)", "Vid", "Hortalizas"],
        "costos": "USD 600 – 1800 / ha",
        "costos_detalle": "Fruticultura de riego de alto valor.",
        "rendimiento": "Alto Valle: peras y manzanas de exportación.",
        "clima": "Templado frío a árido. Precipitaciones bajas en el este."
    },
    "Río Negro": {
        "region": "Patagonia Norte",
        "cultivos": ["Pera", "Manzana", "Vid", "Hortalizas", "Cebolla"],
        "costos": "USD 700 – 2000 / ha",
        "costos_detalle": "Fruticultura intensiva del Alto Valle.",
        "rendimiento": "Principal productor de peras y manzanas del país.",
        "clima": "Árido a semiárido. Precipitaciones bajas. Muy soleado. Inviernos fríos."
    },
    "Chubut": {
        "region": "Patagonia",
        "cultivos": ["Frutales", "Hortalizas", "Forrajeras", "Cereza"],
        "costos": "USD 500 – 1500 / ha",
        "costos_detalle": "Producción limitada y de nicho.",
        "rendimiento": "Producción menor, orientada a calidad (cerezas).",
        "clima": "Árido a frío. Vientos fuertes. Muy soleado en el este."
    },
    "Santa Cruz": {
        "region": "Patagonia Sur",
        "cultivos": ["Forrajeras", "Hortalizas de invernadero"],
        "costos": "Variables (producción limitada)",
        "costos_detalle": "Agricultura muy restringida por el clima.",
        "rendimiento": "Bajo volumen. Principalmente ganadería ovina.",
        "clima": "Frío y seco. Vientos intensos. Veranos cortos y frescos."
    },
    "Tierra del Fuego": {
        "region": "Patagonia Austral",
        "cultivos": ["Hortalizas de invernadero", "Forrajeras"],
        "costos": "Altos (condiciones extremas)",
        "costos_detalle": "Producción muy limitada y costosa.",
        "rendimiento": "Muy bajo.",
        "clima": "Subantártico. Frío, húmedo y ventoso. Poco soleado."
    },
    "Ciudad de Buenos Aires": {
        "region": "CABA",
        "cultivos": ["Huertas urbanas"],
        "costos": "No aplicable a escala comercial",
        "costos_detalle": "No es una provincia agrícola.",
        "rendimiento": "Producción simbólica / comunitaria.",
        "clima": "Templado húmedo. Precipitaciones ≈ 1100-1200 mm."
    }
}

# ====================== INTERFAZ ======================
st.set_page_config(
    page_title="Mapa de Cultivos de Argentina",
    page_icon="🇦🇷",
    layout="wide"
)

st.title("🇦🇷 Mapa de Cultivos de Argentina")
st.markdown("Seleccioná una provincia para ver **cultivos principales**, **costos de producción**, **rendimientos** y **clima**.")

# Sidebar con selector
st.sidebar.header("📍 Provincias")
provincia = st.sidebar.selectbox(
    "Elegí una provincia:",
    options=sorted(datos.keys()),
    index=0
)

# También se puede hacer con botones (opcional)
# st.sidebar.write("O hacé clic:")
# for p in sorted(datos.keys()):
#     if st.sidebar.button(p, use_container_width=True):
#         provincia = p

d = datos[provincia]

# Contenido principal
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader(f"📍 {provincia}")
    st.caption(d["region"])

    st.markdown("### 🌾 Cultivos principales")
    st.write(" • ".join(d["cultivos"]))

    st.markdown("### 💰 Costos de producción (aprox.)")
    st.metric(label="Rango estimado", value=d["costos"])
    st.caption(d["costos_detalle"])

with col2:
    st.markdown("### 📈 Rendimiento / tasa de producción promedio")
    st.info(d["rendimiento"])

    st.markdown("### 🌤️ Clima promedio")
    st.success(d["clima"])

st.divider()
st.caption(
    "* Datos ilustrativos y aproximados basados en promedios regionales y campañas recientes. "
    "Los costos varían según zona, tecnología y año. Fuentes orientativas: SAGYP, BCR, INTA."
)

# ====================== BONUS: Tabla completa ======================
with st.expander("📊 Ver tabla comparativa de todas las provincias"):
    import pandas as pd
    filas = []
    for nombre, info in datos.items():
        filas.append({
            "Provincia": nombre,
            "Región": info["region"],
            "Cultivos principales": ", ".join(info["cultivos"][:3]) + ("..." if len(info["cultivos"]) > 3 else ""),
            "Costos (USD/ha)": info["costos"]
        })
    df = pd.DataFrame(filas)
    st.dataframe(df, use_container_width=True, hide_index=True)
import streamlit as st
import numpy as np

st.title(
    page_title="Proyecto 2 – Densidad de una Esfera",
    layout="centered"
)

st.title("⚙️ Proyecto 2: Densidad de una Esfera")
st.write("Cálculo de la densidad y su incertidumbre usando propagación de errores.")

st.divider()

st.header("📥 Datos experimentales")

m = st.number_input(
    "Masa m (g)",
    min_value=0.0,
    value=125.0,
    step=0.1
)

Dm = st.number_input(
    "Incertidumbre de la masa Δm (g)",
    min_value=0.0,
    value=0.1,
    step=0.01
)

r = st.number_input(
    "Radio r (cm)",
    min_value=0.0,
    value=2.15,
    step=0.01
)

Dr = st.number_input(
    "Incertidumbre del radio Δr (cm)",
    min_value=0.0,
    value=0.01,
    step=0.001
)

st.divider()

if st.button("📊 Calcular densidad"):
    pi = np.pi

    # Densidad
    rho = 3 * m / (4 * pi * r**3)

    # Derivadas parciales
    drho_dm = 3 / (4 * pi * r**3)
    drho_dr = -9 * m / (4 * pi * r**4)

    # Propagación de incertidumbre
    Drho = np.sqrt((drho_dm * Dm)**2 + (drho_dr * Dr)**2)

    # Contribuciones
    contrib_m = abs(drho_dm * Dm)
    contrib_r = abs(drho_dr * Dr)

    st.header("📐 Resultados")

    st.write(f"**Densidad:** ρ = **{rho:.3f} g/cm³**")
    st.write(f"**Incertidumbre:** Δρ = **{Drho:.3f} g/cm³**")

    st.success(f"Resultado final: ρ = ({rho:.2f} ± {Drho:.2f}) g/cm³")

    st.divider()

    st.subheader("🔍 Análisis de contribuciones al error")

    st.write(f"Contribución de la masa: **{contrib_m:.4f} g/cm³**")
    st.write(f"Contribución del radio: **{contrib_r:.4f} g/cm³**")

    if contrib_r > contrib_m:
        st.warning("⚠️ El radio domina la incertidumbre total.")
    else:
        st.info("ℹ️ La masa domina la incertidumbre total.")
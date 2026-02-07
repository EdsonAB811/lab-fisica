import streamlit as st
import numpy as np

st.set_page_config(layout="centered")

st.title("⚙️ Proyecto 2 – Densidad de una Esfera")
st.write(
    "Cálculo de la densidad usando propagación de incertidumbres "
    "con análisis estadístico del radio."
)

st.divider()

# =========================
# DATOS DE ENTRADA
# =========================

st.header("📥 Datos experimentales")

st.subheader("🔵 Mediciones del radio (cm)")
radios_texto = st.text_input(
    "Ingresa las mediciones separadas por coma",
    value="2.50, 2.52, 2.51, 2.49, 2.50"
)

Delta_r_instr = st.number_input(
    "Incertidumbre instrumental del radio Δr_instr (cm)",
    min_value=0.0,
    value=0.01,
    step=0.001
)

st.subheader("⚖️ Masa de la esfera")

m = st.number_input(
    "Masa m (g)",
    min_value=0.0,
    value=125.0,
    step=0.1
)

Delta_m = st.number_input(
    "Incertidumbre de la masa Δm (g)",
    min_value=0.0,
    value=0.1,
    step=0.01
)

st.divider()

# =========================
# CÁLCULOS
# =========================

if st.button("📊 Calcular densidad"):

    try:
        # Convertir radios a lista de floats
        radios = [float(r.strip()) for r in radios_texto.split(",")]
        n = len(radios)

        if n < 2:
            st.error("⚠️ Ingresa al menos dos mediciones del radio.")
            st.stop()

        # Promedio del radio
        r_prom = np.mean(radios)

        # Desviación estándar muestral
        sigma_r = np.std(radios, ddof=1)

        # Incertidumbre estadística
        Delta_r_estad = sigma_r / np.sqrt(n)

        # Incertidumbre total del radio
        Delta_r = np.sqrt(Delta_r_instr**2 + Delta_r_estad**2)

        # =========================
        # DENSIDAD
        # =========================
        pi = np.pi
        rho = 3 * m / (4 * pi * r_prom**3)

        # Derivadas parciales
        drho_dm = 3 / (4 * pi * r_prom**3)
        drho_dr = -9 * m / (4 * pi * r_prom**4)

        # Propagación de incertidumbre
        Delta_rho = np.sqrt(
            (drho_dm * Delta_m)**2 +
            (drho_dr * Delta_r)**2
        )

        # Contribuciones
        contrib_m = abs(drho_dm * Delta_m)
        contrib_r = abs(drho_dr * Delta_r)

        # =========================
        # RESULTADOS
        # =========================

        st.header("📐 Resultados")

        st.write(f"**Radio promedio:** {r_prom:.4f} cm")
        st.write(f"**Incertidumbre estadística del radio:** {Delta_r_estad:.4f} cm")
        st.write(f"**Incertidumbre total del radio:** {Delta_r:.4f} cm")

        st.divider()

        st.write(f"**Densidad:** ρ = **{rho:.3f} g/cm³**")
        st.write(f"**Incertidumbre:** Δρ = **{Delta_rho:.3f} g/cm³**")

        st.success(
            f"Resultado final:\n\n"
            f"ρ = ({rho:.2f} ± {Delta_rho:.2f}) g/cm³"
        )

        st.divider()

        st.subheader("🔍 Análisis de contribuciones")

        st.write(f"Contribución de la masa: **{contrib_m:.4f} g/cm³**")
        st.write(f"Contribución del radio: **{contrib_r:.4f} g/cm³**")

        if contrib_r > contrib_m:
            st.warning("⚠️ La incertidumbre del radio domina el error total.")
        else:
            st.info("ℹ️ La incertidumbre de la masa domina el error total.")

    except ValueError:
        st.error("❌ Revisa el formato de las mediciones del radio.")


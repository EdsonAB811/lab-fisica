import streamlit as st

# título de la página
st.title("Mi Primera App en Streamlit 🎉")

# Subtítulo
st.subheader("¡Bienvenido a mi primera aplicación interactiva!")

# texto
st.write(
    """
    Streamlit es una biblioteca increíble para crear aplicaciones web interactivas con Python. 
    Esta es una demo simple para mostrar algunas características básicas.
    """
)

# Varios inputs
nombre = st.text_input("¿Cómo te llamas?", "")
if nombre:
    st.write(f"¡Hola, {nombre}! 🎈")


edad = st.slider("¿Cuál es tu edad?", 0, 100, 18)
st.write(f"Tienes {edad} años. ¡Fantástico!")


gusta_streamlit = st.checkbox("¿Te gusta Streamlit?")
if gusta_streamlit:
    st.write("¡A mí también me encanta! 😍")


st.write("Gracias por probar mi primera app. ¡Espero que te haya gustado!")

st.title("Longitud del Péndulo")

st.markdown("Ingrese los datos medidos:")

# Entrada de datos
L = st.number_input(
    "Longitud del péndulo L (en metros)",
    min_value=0.0,
    value=0.50,
    step=0.01,
    format="%.3f"
)

Delta_L_instr = st.number_input(
    "Resolución de la cinta métrica ΔL (en metros)",
    min_value=0.0,
    value=0.001,
    step=0.0001,
    format="%.4f"
)

# Cálculo de la incertidumbre total
Delta_L_total = Delta_L_instr

st.markdown("---")
st.subheader("Resultado")

st.latex(
    rf"L = ({L:.3f} \pm {Delta_L_total:.4f}) \, \text{{m}}"
)

import numpy as np

st.title("Tiempos medidos (10 oscilaciones)")

st.markdown("Ingrese los tiempos medidos para **10 oscilaciones**:")

# Entrada de tiempos como texto
tiempos_texto = st.text_input(
    "Tiempos (en segundos, separados por comas)",
    value="14.25, 14.18, 14.32, 14.21, 14.28"
)

# Resolución del cronómetro
Delta_t_instr = st.number_input(
    "Resolución del cronómetro Δt (s)",
    min_value=0.0,
    value=0.01,
    step=0.001,
    format="%.3f"
)

# Conversión del texto a array
try:
    t_10_oscilaciones = np.array(
        [float(t) for t in tiempos_texto.split(",")]
    )
    n = len(t_10_oscilaciones)

    st.markdown("---")
    st.subheader("Datos ingresados")

    st.write(f"Número de mediciones: **{n}**")
    st.write("Tiempos de 10 oscilaciones (s):")
    st.write(t_10_oscilaciones)

    st.write(f"Resolución del cronómetro: ±{Delta_t_instr} s")

except ValueError:
    st.error("⚠️ Por favor ingrese solo números separados por comas.")

st.markdown("---")
st.header("Análisis estadístico")

# Promedio
t_promedio = np.mean(t_10_oscilaciones)

# Desviación estándar muestral
sigma = np.std(t_10_oscilaciones, ddof=1)

st.latex(
    rf"\bar{{t}} = {t_promedio:.4f}\ \text{{s}}"
)

st.latex(
    rf"\sigma = {sigma:.4f}\ \text{{s}}"
)

st.markdown("---")
st.header("Análisis de incertidumbres")

# Incertidumbre estadística (Tipo A)
Delta_t_estad = sigma / np.sqrt(n)

# Incertidumbre total (combinación en cuadratura)
Delta_t_total = np.sqrt(Delta_t_instr**2 + Delta_t_estad**2)

st.subheader("Incertidumbres")

st.latex(
    rf"\Delta t_{{\text{{estad}}}} = {Delta_t_estad:.4f}\ \text{{s}}"
)

st.latex(
    rf"\Delta t_{{\text{{instr}}}} = {Delta_t_instr:.4f}\ \text{{s}}"
)

st.latex(
    rf"\Delta t_{{\text{{total}}}} = {Delta_t_total:.4f}\ \text{{s}}"
)

# Análisis de contribuciones
contrib_estad = (Delta_t_estad**2 / Delta_t_total**2) * 100
contrib_instr = (Delta_t_instr**2 / Delta_t_total**2) * 100

st.subheader("Contribución al error total")

st.write(f"📊 Estadística (Tipo A): **{contrib_estad:.1f}%**")
st.write(f"⏱️ Instrumental (Tipo B): **{contrib_instr:.1f}%**")

st.markdown("---")
st.header("Periodo de oscilación")

# Periodo promedio y su incertidumbre
T_promedio = t_promedio / 10
Delta_T = Delta_t_total / 10

st.latex(
    rf"T = ({T_promedio:.3f} \pm {Delta_T:.3f})\ \text{{s}}"
)

import pandas as pd

st.markdown("---")
st.header("Tabla 1. Mediciones experimentales")

# Crear números de medición
numeros_medicion = np.arange(1, n + 1)

# Construir la tabla
tabla_datos = pd.DataFrame({
    "Medición": numeros_medicion,
    "Tiempo 10 oscilaciones (s)": t_10_oscilaciones
})

# Mostrar tabla
st.dataframe(tabla_datos, use_container_width=True)

st.markdown("### Estadísticos")

st.latex(
    rf"\bar{{t}} = {t_promedio:.4f}\ \text{{s}}"
)

st.latex(
    rf"\sigma = {sigma:.4f}\ \text{{s}}"
)

import matplotlib.pyplot as plt
import numpy as np

st.markdown("---")
st.header("Figura 1. Mediciones del tiempo")

# Crear números de medición
numeros_medicion = np.arange(1, n + 1)

# Crear figura
fig, ax = plt.subplots()

# Puntos experimentales
ax.plot(
    numeros_medicion,
    t_10_oscilaciones,
    'ro',
    markersize=8,
    label='Mediciones individuales'
)

# Línea del promedio
ax.axhline(
    y=t_promedio,
    color='blue',
    linestyle='--',
    linewidth=2,
    label=fr'Promedio: {t_promedio:.2f} s'
)

# Banda de incertidumbre
ax.axhspan(
    t_promedio - Delta_t_total,
    t_promedio + Delta_t_total,
    alpha=0.2,
    color='blue',
    label=fr'Incertidumbre: ±{Delta_t_total:.3f} s'
)

# Etiquetas y estilo
ax.set_xlabel('Número de medición')
ax.set_ylabel('Tiempo de 10 oscilaciones (s)')
ax.set_title('Mediciones del tiempo de oscilación')
ax.legend()
ax.grid(True, alpha=0.3)

# Mostrar en Streamlit
st.pyplot(fig)




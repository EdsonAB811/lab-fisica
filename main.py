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


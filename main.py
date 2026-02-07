import streamlit as st

st.set_page_config(
    page_title="Laboratorio de Física",
    layout="centered"
)

inicio = st.Page(
    "pages/inicio.py",
    title="Inicio",
    icon=":material/home:"
)

pendulo = st.Page(
    "pages/pendulo.py",
    title="Péndulo",
    icon=":material/timer:"
)

esfera = st.Page(
    "pages/esfera.py",
    title="Esfera",
    icon=":material/circle:"
)

pg = st.navigation(
    [inicio, pendulo, esfera]
)

pg.run()







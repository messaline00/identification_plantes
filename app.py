import streamlit as st

st.set_page_config(
    page_title="Reconnaisance plantes",
    page_icon="",
    layout="wide"
)

st.title("Reconnaissance des plantes et des maladies")

st.markdown("""
## Présentation du projet

Ce projet a pour objectif de :

- Identifier le taxon d'une plante à partir d'une photo 
- Identifier l'état sanaitaire d'une plante à partir d'une photo

Nous avons comparé plusieurs approches :

- Machine Learning
- CNN
- Transfer Learning
""")
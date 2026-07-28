import streamlit as st
from PIL import Image
import time

from utils.predict import (
    predict_taxon,
    predict_disease,
    get_health_status
)

st.set_page_config(
    page_title="Prédiction",
    page_icon="🌿",
    layout="wide"
)

st.title("Identification d'une plante")

st.markdown(
"""
Chargez une image d'une feuille afin :

- d'identifier **l'espèce** de la plante
- de déterminer si elle est **saine** ou **malade**
"""
)

uploaded_file = st.file_uploader(
    "Choisissez une image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Image importée",
        width=350
    )

if st.button("🔍 Lancer la prédiction"):

    with st.spinner("Analyse de l'image en cours..."):

        start = time.time()

        taxon, score_taxon, top5_taxons = predict_taxon(image)

        maladie, score_maladie, top5_maladies = predict_disease(image)

        end = time.time()

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("🌿 Espèce détectée")

    st.success(taxon)

    st.metric(
        "Confiance",
        f"{score_taxon*100:.2f}%"
    )

with col2:

    st.subheader("🦠 Diagnostic")

    if get_health_status(maladie):

        st.success(maladie)

    else:

        st.error(maladie)

    st.metric(
        "Confiance",
        f"{score_maladie*100:.2f}%"
    )

st.info(
    f"Temps de prédiction : {end-start:.2f} seconde(s)"
)
st.subheader("Top 5 - Taxons")

for classe, prob in top5_taxons:

    st.write(
        f"**{classe}** : {prob*100:.2f}%"
    )

    st.progress(prob)

st.subheader("Top 5 - Maladies")

for classe, prob in top5_maladies:

    st.write(
        f"**{classe}** : {prob*100:.2f}%"
    )

    st.progress(prob)

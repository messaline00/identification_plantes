import streamlit as st
from PIL import Image
import time
import pandas as pd
from utils.gradcam import (
    generate_resnet_gradcam,
    generate_efficientnet_gradcam
)
from utils.predict import (
    predict_taxon,
    predict_disease,
    get_health_status,
    get_disease_name
)

st.set_page_config(
    page_title="Prédiction",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 Identification d'une plante")

st.markdown("""
Chargez une image d'une feuille afin de :

- identifier **l'espèce** de la plante
- déterminer si elle est **saine** ou **malade**
""")

# -----------------------------
# Initialisation de la session
# -----------------------------

if "prediction" not in st.session_state:
    st.session_state.prediction = None

# -----------------------------
# Upload image
# -----------------------------

uploaded_file = st.file_uploader(
    "Choisissez une image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Image importée",
        width=350
    )

    if st.button("Lancer la prédiction"):

        with st.spinner("Analyse de l'image en cours..."):

            start = time.time()

            taxon, score_taxon, top5_taxons = predict_taxon(image)

            maladie, score_maladie, top5_maladies = predict_disease(image)

            end = time.time()

            st.session_state.prediction = {
                "image": image,
                "taxon": taxon,
                "score_taxon": score_taxon,
                "top5_taxons": top5_taxons,
                "maladie": maladie,
                "score_maladie": score_maladie,
                "top5_maladies": top5_maladies,
                "temps": end - start
            }

# -----------------------------
# Affichage des résultats
# -----------------------------

if st.session_state.prediction is not None:

    pred = st.session_state.prediction

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🌿 Espèce détectée")

        st.success(pred["taxon"])

        st.metric(
            "Confiance",
            f"{pred['score_taxon']*100:.2f}%"
        )

    with col2:

        st.subheader("Diagnostic")

        maladie_nom = get_disease_name(pred["maladie"])

        if get_health_status(pred["maladie"]):

            st.success("🟢 Plante saine")

            st.write(
                "Aucun symptôme de maladie détecté."
            )

        else:

            st.error("🔴 Plante malade")

            st.write(
                f"**Maladie détectée : {maladie_nom}**"
            )

        st.metric(
            "Confiance",
            f"{pred['score_maladie']*100:.2f}%"
        )

    st.info(
        f"⏱ Temps de prédiction : {pred['temps']:.2f} seconde(s)"
    )

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("Top 5 - Taxons")

        df_taxons = pd.DataFrame(
            pred["top5_taxons"],
            columns=["Taxon", "Probabilité"]
        )

        df_taxons["Probabilité"] = (
            df_taxons["Probabilité"] * 100
        ).round(2).astype(str) + " %"

        st.dataframe(
            df_taxons,
            use_container_width=True,
            hide_index=True
        )

    with col4:

        st.subheader("Top 5 - Maladies")

        df_maladies = pd.DataFrame(
            pred["top5_maladies"],
            columns=["Maladie", "Probabilité"]
        )

        df_maladies["Probabilité"] = (
            df_maladies["Probabilité"] * 100
        ).round(2).astype(str) + " %"

        st.dataframe(
            df_maladies,
            use_container_width=True,
            hide_index=True
        )
    st.divider()

    st.subheader("Interprétation des modèles")

    col_grad1, col_grad2 = st.columns(2)


    with col_grad1:

        st.markdown(
            "### ResNet50 - Identification de l'espèce"
        )

        with st.spinner("Calcul Grad-CAM ResNet50..."):

            gradcam_resnet = generate_resnet_gradcam(
                pred["image"]
            )

        st.image(
            gradcam_resnet,
            caption="Zones utilisées pour identifier l'espèce",
            use_container_width=True
        )


    with col_grad2:

        st.markdown(
            "### EfficientNet-B3 - Diagnostic maladie"
        )

        with st.spinner("Calcul Grad-CAM EfficientNet..."):

            gradcam_eff = generate_efficientnet_gradcam(
                pred["image"]
            )

        st.image(
            gradcam_eff,
            caption="Zones utilisées pour identifier l'état sanitaire de la plante",
            use_container_width=True)
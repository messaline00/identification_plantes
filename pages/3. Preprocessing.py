import streamlit as st
import pandas as pd
from pathlib import Path
import pandas as pd
import plotly.express as px

from theme import (
    inject_css,
    chapter_banner,
    info_box,
    warning_box,
    success_box,
    kpi_row,
    white_card,
)


# =====================================================
# THÈME
# =====================================================

inject_css()

chapter_banner(
    "03",
    "Prétraitement des données",
    "")


st.markdown("""
Avant l'entraînement, les données ont été préparées afin de garantir une
évaluation fiable des modèles et d'éviter les fuites de données.
""")

# ─────────────────────────────────────────────
st.subheader("1. Splits train / validation / test")


st.markdown("""
Les images ont été regroupées par **familles de clones** à l'aide du **pHash**.
Les images visuellement très proches sont ainsi conservées dans le même
sous-ensemble.
""")

kpi_row(
    [
        {
            "value": "70 %",
            "label": "ENTRAÎNEMENT",
            "sub": "",
        },
        {
            "value": "15 %",
            "label": "VALIDATION",
            "sub": "",
        },
        {
            "value": "15 %",
            "label": "TEST",
            "sub": "",
        },
    ]
)


info_box(
    "Le regroupement par familles permet d'éviter qu'une même image "
    "ou un quasi-doublon soit présent dans plusieurs sous-ensembles."
)
# ─────────────────────────────────────────────
st.subheader("2. Gestion du déséquilibre des classes")

st.markdown("""
Le déséquilibre entre les classes est pris en compte grâce aux **class weights**.

Les poids sont calculés **uniquement à partir du jeu d'entraînement** afin
d'éviter toute fuite d'information.
""")

col1, col2 = st.columns(2)

with col1:
    st.metric("Déséquilibre TAXONS", "12×")

with col2:
    st.metric("Déséquilibre MALADIES", "2,7×")

# ─────────────────────────────────────────────
st.subheader("3. Contrôle anti-fuite")

st.markdown("""
Un **contre-audit pHash** a été réalisé après le découpage sur un échantillon
de 2 000 images par sous-ensemble.

Seulement **1 à 4 paires résiduelles** ont été détectées selon la base,
soit environ **0,0001 %** des comparaisons.
""")
st.image(
        "images/Prétraitement/PHash.png",
        caption=" Exemple de famille de clones identifiée par pHash",
        use_container_width=True
    )
success_box("La séparation des jeux de données est considérée comme effective.")

# ─────────────────────────────────────────────
st.header("4. Contrôle des labels")

st.markdown("""
La comparaison des deux bases a révélé **19 cas de label noise** :
des images quasi identiques correspondant à une même espèce étaient associées
à des maladies différentes dans le dataset source.

Ces 19 cas (**≈ 0,02 % du corpus**) ont été conservés afin de ne pas modifier
manuellement les annotations d'origine.
""")

# ─────────────────────────────────────────────
st.divider()

success_box(
    "<div style='line-height:1.8;'>"
    "<b>✓ Vérifications effectuées</b><br><br>"
    "✅ Splits stratifiés anti-fuite<br>"
    "✅ Class weights calculés uniquement sur le train<br>"
    "✅ Cohérence des étiquettes vérifiée<br><br>"
    "<b>Bases prêtes pour la modélisation :</b> 96 165 images"
    "</div>"
)
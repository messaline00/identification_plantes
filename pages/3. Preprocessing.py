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
st.markdown("""
Processus de prétraitement des données :

1. Nettoyage et cohérence : Vérification des étiquettes pour garantir la qualité des entrées.
2. Partitionnement des données (Splits) : Séparation rigoureuse en jeux d'entraînement, de validation et de test.
3. Équilibrage : Calcul des poids de classe (class weights) sur le jeu d'entraînement pour compenser le déséquilibre.
4. Augmentation de données : Application de transformations aléatoires (rotations, flips, luminosité) pour limiter le surapprentissage.
5. Normalisation : Redimensionnement scalaire des pixels [0, 1] pour stabiliser l'apprentissage du modèle.
6. Redimensionnement du format des images.
""")


# ─────────────────────────────────────────────

st.subheader("1. Vérification de la cohérence des étiquettes")

st.markdown("""
Avant toute manipulation, une étape de nettoyage a été réalisée pour garantir l'intégrité des annotations :

Validation des labels : Vérification de la correspondance entre les noms des dossiers et le dictionnaire des classes (14 espèces, 38 pathologies au total).
Standardisation : Correction des éventuelles erreurs de syntaxe ou de casse dans les métadonnées.
Élimination des erreurs : Suppression des échantillons mal étiquetés ou corrompus pour éviter d'introduire du bruit lors de l'apprentissage.
""")



st.subheader("2. Splits train / validation / test")
st.markdown("""
Nous avons implémenté la méthode **GroupShuffleSplit**. Les images ont été regroupées par **familles de clones** à l'aide du **pHash**.
Les images visuellement très proches sont ainsi conservées dans le même
sous-ensemble.
""")
st.image(
        "images/Prétraitement/PHash.png",
        caption=" Exemple de famille de clones identifiée par pHash",
        use_container_width=True
    )
df_sources = pd.DataFrame(
        {
            "Base": [
                "TAXONS",
                "MALADIES",
            ],

            "Nombre de Familles (NdF)": [
                "94 356",
                "94 375",
            ],

            "Différence : 96 165 - NdF": [
                "1809",
                "1790",
               
            ],
        }
    )

st.dataframe(df_sources, hide_index=True, use_container_width=True) 

info_box(
    "Le regroupement par <b>familles</b> - <b>group_id</b> - permet d'éviter la présence d'une même image ou d'un quasi-doublon"
    " au sein de différents sous-ensembles (TRAIN-VAL-TEST)."
)

info_box(
    "La comparaison des deux bases a révélé 19 cas (1809-1790 = 19) de <b>LABEL NOISE</b>"
    " - <b>anomalie sémantique</b> - où des images quasi identiques correspondant à une même espèce étaient associées à des maladies différentes"
    "dans le dataset source. Ces 19 cas (≈ 0,02 % du corpus) ont été conservés afin de ne pas modifier manuellement"
    "les annotations d'origine."
)
info_box(
    "Le <b>contrôle anti-fuite</b> par <b>contre-audit pHash</b> permet de considérer " 
    " la séparation des jeux de données comme fiable.")

kpi_row(
    [
        {
            "value": "70 %",
            "label": "ENTRAÎNEMENT",
            "sub": "67 377 / 67 339 images",
        },
        {
            "value": "15 %",
            "label": "VALIDATION",
            "sub": "14 370 / 14 402 images",
        },
        {
            "value": "15 %",
            "label": "TEST",
            "sub": "14 418 / 14 424 images",
        },
    ]
)
st.write("")
st.write("")
# ─────────────────────────────────────────────
st.subheader("3. Gestion du déséquilibre des classes")
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.metric("Déséquilibre TAXONS", "12×")

with col2:
    st.metric("Déséquilibre MALADIES", "2,7×")

st.markdown("""
Le déséquilibre entre les classes est traité par l'application de poids de classe (**class weights**).

**Mise en œuvre** : Contrairement au rééchantillonnage (**oversampling/undersampling**) qui modifie les données en amont, les poids de classe interviennent directement lors de la phase d'entraînement. Ils permettent de pénaliser davantage les erreurs commises sur les classes minoritaires au sein de la fonction de coût (**loss function**).

**Calcul** : Les poids sont calculés **uniquement à partir du jeu d'entraînement** afin d'éviter toute fuite d'information (**data leakage**). Cette approche assure que le modèle ne dispose d'aucune information sur la distribution des données de validation ou de test.

""")


# ─────────────────────────────────────────────
st.subheader("4. Augmentation des données (Data Augmentation)")

st.markdown("""
Afin d'améliorer la capacité de généralisation du modèle et de limiter le risque de surapprentissage (**overfitting**), une stratégie d'augmentation de données a été mise en place.

**Méthode** : Ces transformations sont appliquées **uniquement sur le jeu d'entraînement** de manière dynamique (**on-the-fly**) lors de chaque époque. Cela permet au modèle de voir des variantes différentes d'une même image à chaque passage."""
)
st.markdown("""
Cette étape est cruciale pour diversifier les exemples des classes minoritaires et rendre le modèle plus robuste face aux données réelles du terrain.

""")


#─────────────────────────────────────────────
st.subheader("5. Normalisation des données")

st.markdown("""
La normalisation est une étape indispensable pour faciliter la convergence du modèle lors de l'entraînement.

**Méthode** : Les valeurs des pixels, initialement comprises entre 0 et 255 (format RGB), ont été ramenées dans un intervalle de [0, 1] par un redimensionnement scalaire (division par 255).

**Objectif** : Cette opération permet d'uniformiser la distribution des données d'entrée, ce qui stabilise le calcul des gradients et accélère l'apprentissage du réseau de neurones. Contrairement à l'augmentation, cette transformation est appliquée de manière identique à **l'ensemble des données** (entraînement, validation et test).
""")

#─────────────────────────────────────────────
st.subheader("6. Redimensionnement (Resize) ")

st.markdown("""
Toutes les images ont été uniformisées au format 256 x 256 pixels pour correspondre à la couche d'entrée du réseau de neurones - 224 x 224 - et assurer une cohérence dimensionnelle lors du calcul en batch. 
""")
# ─────────────────────────────────────────────
st.divider()

success_box(
    "<div style='line-height:1.8;'>"
    "<b>✓ Vérifications effectuées</b><br><br>"
    "✅ Cohérence des étiquettes vérifiée – pour éviter le principe du 'Garbage In, Garbage Out'<br>"
    "✅ Splits stratifiés anti-fuite<br>"
    "✅ Les class weights et l'augmentation sont effectués uniquement sur le jeu d'entraînement<br>"
    "✅ Normalisation et redimensionnement appliqués de manière identique à l'ensemble des données<br><br>"
    "</div>"
    "<b>Le complet des deux bases du projet prête pour la modélisation </b>"
    "</div>"
)
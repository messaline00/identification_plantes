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
    hypo_row
)



# =====================================================
# CONCLUSION
# =====================================================

st.header("Conclusion")



# =====================================================
# HYPOTHÈSES
# =====================================================

st.subheader("Bilan des hypothèses")


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

hypo_row(
    [
        {
            "title": "H1 · CNN optimisé — CONFIRMÉE",
            "body": """
            Le <b>transfer learning</b> surpasse le CNN entraîné from scratch
            ainsi que les modèles de Machine Learning classique sur les deux tâches.
            <br><br>
            <b>TAXONS :</b> +4,17 points<br>
            95,60 % → 99,77 %
            <br><br>
            <b>MALADIES :</b> +3,45 points<br>
            95,77 % → 99,22 %
            """,
        },
        {
            "title": "H2 · Morphologie — PARTIELLEMENT CONFIRMÉE",
            "body": """
            Les caractéristiques morphologiques apportent une information
            discriminante pour l'identification des espèces.
            <br><br>
            <b>ResNet50 :</b> 99,77 % d'accuracy<br>
            <b>XGBoost + HOG :</b> 85,9 % d'accuracy
            <br><br>
            En conditions réelles, <b>4/4 espèces connues</b> ont été correctement
            identifiées, mais la détection des cas hors périmètre reste imparfaite.
            """,
        },
    ]
)

# =====================================================
# CE QUE LE PROJET A MONTRÉ
# =====================================================

st.subheader("Ce que le projet a montré")

kpi_row(
    [
        {
            "value": "85,9 %",
            "label": "MACHINE LEARNING",
            "sub": "XGBoost · TAXONS",
        },
        {
            "value": "95,6 %",
            "label": "CNN BASELINE",
            "sub": "TAXONS",
        },
        {
            "value": "99,77 %",
            "label": "TRANSFER LEARNING",
            "sub": "ResNet50 · TAXONS",
        },
    ]
)

st.markdown("""
La comparaison met en évidence une progression nette des performances :
les modèles de Machine Learning classique sont dépassés par le CNN de
référence, puis par les architectures pré-entraînées.

Le transfer learning permet ainsi d'atteindre les meilleures performances
sur les deux tâches, avec des F1-scores supérieurs à 98 %.
""")


st.divider()


# =====================================================
# LIMITES
# =====================================================

st.subheader("Limites identifiées")

col1, col2 = st.columns(2)

with col1:
    info_box(
        """
        ⚠️ Conditions d'acquisition

        Les données d'entraînement et de test sont relativement standardisées.
        Les performances obtenues ne garantissent donc pas la même robustesse
        sur des photographies de terrain.
        """
    )

with col2:
    info_box(
        """
        ⚠️ Détection de l'inconnu

        Un modèle peut produire une prédiction incorrecte avec une confiance
        élevée. Le simple seuil de confiance utilisé dans l'application ne
        garantit donc pas la détection des cas hors périmètre.
        """
    )

col1, col2 = st.columns(2)

with col1:
    info_box(
        """
        ⚠️ Interprétabilité

        Les analyses Grad-CAM montrent que certaines prédictions peuvent
        s'appuyer ponctuellement sur des régions qui ne correspondent pas
        directement aux caractéristiques recherchées.
        """
    )

with col2:
    info_box(
        """
        ⚠️ Confusions résiduelles

        Certaines classes visuellement proches restent difficiles à distinguer,
        notamment pour certaines espèces et maladies.
        """
    )


st.divider()


# =====================================================
# PERSPECTIVES
# =====================================================

st.subheader("Perspectives")

st.markdown("""
Les principales pistes d'amélioration concernent :

• **La validation terrain** — tester les modèles sur un ensemble beaucoup plus
large d'images provenant de conditions d'acquisition et de sources variées.

• **La détection hors distribution** — remplacer le simple seuil de confiance
par une méthode plus robuste pour identifier les images ne correspondant pas
aux classes apprises.

• **L'optimisation du déploiement** — étudier la distillation de connaissances,
la quantification ou la compression des modèles afin de réduire leur coût
computationnel.
""")


st.divider()


success_box(
    """
    <b>Bilan final</b><br><br>
    Identifier une plante et détecter une maladie à partir d'une image est
    réalisable avec une très bonne précision sur les classes connues.
    <br><br>
    L'enjeu suivant n'est plus seulement d'améliorer les scores sur des données
    contrôlées, mais de garantir la robustesse du modèle face à la diversité
    des situations rencontrées sur le terrain.
    """
)
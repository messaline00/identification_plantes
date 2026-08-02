import streamlit as st

from theme import (
    inject_css,
    chapter_banner,
    success_box,
    hypo_row,
    info_box
)

# =====================================================
# CONCLUSION
# =====================================================

inject_css()

chapter_banner(
    "07",
    "Conclusion",
    ""
)

# =====================================================
# HYPOTHÈSES
# =====================================================

st.subheader("Bilan des hypothèses")

hypo_row(
    [
        {
            "title": "H1 · CNN optimisé — CONFIRMÉE",
            "body": """
            Le <b>transfer learning</b> surpasse le CNN Baseline
            ainsi que les modèles de Machine Learning sur les deux tâches de classification.
            <br><br>
            <b>TAXONS :</b> +14,67 points<br>
            85,1 % → 95,60 % → 99,77 %
            <br><br>
            <b>MALADIES :</b> +18,27 points<br>
            81,4 % → 95,80 % → 99,67 %
            """,
        },
        {
            "title": "H2 · Morphologie — PARTIELLEMENT CONFIRMÉE",
            "body": """
            Hypothèse validée sur les données de test.

            Le modèle exploite principalement la morphologie, mais aussi parfois le contexte de l'image.

            Les espèces hors du domaine d'apprentissage restent une limite importante.

            Une forte confiance ne garantit pas qu'une prédiction soit correcte.
            """
            
        },
    ]
)

st.divider()

# =====================================================
# LIMITES
# =====================================================

st.subheader("Limites identifiées")

limites = [
    (
        "### Conditions d'acquisition\n\n"
        "Les modèles ont été entraînés et évalués sur des images prises dans des conditions relativement standardisées (fond, cadrage, luminosité).\n\n"
        "Leur capacité de généralisation à des photographies de terrain reste donc limitée."
    ),
    (
        "### Détection de l'inconnu\n\n"
        "Une espèce ou une maladie absente du jeu d'entraînement peut être classée comme une classe connue avec une confiance élevée.\n\n"
        "Le seuil de confiance utilisé ne permet donc pas, à lui seul, de détecter les cas hors périmètre."
    ),
    (
        "### Interprétabilité\n\n"
        "Les cartes Grad-CAM montrent que le modèle s'appuie parfois sur des éléments du fond de l'image en plus des caractéristiques de la feuille.\n\n"
        "Ces résultats doivent donc être interprétés avec prudence."
    ),
    (
        "### Confusions entre classes\n\n"
        "Certaines espèces ou maladies présentant des caractéristiques visuelles proches restent difficiles à distinguer.\n\n"
        "Ces similarités peuvent conduire à des erreurs de classification."
    ),
]

for i in range(0, len(limites), 2):

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown(limites[i])

    with col2:
        with st.container(border=True):
            st.markdown(limites[i + 1])

st.divider()

# =====================================================
# PERSPECTIVES
# =====================================================

st.subheader("Perspectives")

st.markdown(
    """
Les principales pistes d'amélioration concernent :

• **La validation terrain** — tester les modèles sur un ensemble beaucoup plus
large d'images provenant de conditions d'acquisition et de sources variées.

• **La détection hors distribution** — remplacer le simple seuil de confiance
par une méthode plus robuste pour identifier les images ne correspondant pas
aux classes apprises.

• **Diversification des données** — enrichir le jeu d'entraînement avec davantage
d'espèces, de maladies et d'images prises dans des conditions réelles.
"""
)

st.divider()

st.success(
    """
Ce projet montre qu'il est possible d'identifier une plante et de détecter une maladie foliaire à partir d'une simple image lorsque l'espèce appartient au domaine d'apprentissage du modèle.
La principale difficulté n'est plus la performance sur le jeu de test, mais la capacité du modèle à reconnaître ses propres limites lorsqu'il est confronté à des situations nouvelles.
"""
)


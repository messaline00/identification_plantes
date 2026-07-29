import streamlit as st
import pandas as pd

from theme import (
    inject_css,
    chapter_banner,
    info_box,
    warning_box,
    success_box,
    kpi_row,
)

# =====================================================
# THÈME
# =====================================================

inject_css()

chapter_banner(
    "02",
    "Exploration des données",
    "")

# =====================================================
# MENU LATERAL
# =====================================================

st.sidebar.title("Exploration des données")

pages = [
    "Construction des bases",
    "Base TAXONS",
    "Base MALADIES"
]

page = st.sidebar.radio(
    "Choisir une section",
    pages
)


# =====================================================
# CONSTRUCTION DES BASES DE DONNÉES
# =====================================================

# =====================================================
# CONSTRUCTION DES BASES
# =====================================================

if page == pages[0]:

    st.header("Construction des bases de données")

    info_box(
        """
        Six bases publiques ont été étudiées afin de constituer un corpus de
        référence pour la classification des <b>taxons</b> et des
        <b>maladies</b>.

        Après analyse de leur qualité, de leur contenu et des doublons,
        <b>deux bases ont été retenues</b> afin de constituer
        un corpus homogène.
        """
    )


    # =====================================================
    # SÉLECTION DES BASES
    # =====================================================

    st.subheader("Sélection des bases de données")

    df_sources = pd.DataFrame(
        {
            "Base": [
                "New Plant Diseases",
                "PlantVillage",
                "Plant Disease",
                "V2 Plant Seedlings",
                "Open Images",
                "COCO",
            ],

            "Volume": [
                "87 867",
                "54 305",
                "54 305",
                "5 539",
                "~9 M",
                "~330 K",
            ],

            "Classes": [
                38,
                38,
                38,
                12,
                49,
                1,
            ],

            "Décision": [
                "✅ Retenue",
                "✅ Retenue",
                "❌ Doublon",
                "❌ Trop peu d'images",
                "❌ Images inadaptées",
                "❌ Images inadaptées",
            ],
        }
    )


    st.dataframe(
        df_sources,
        hide_index=True,
        use_container_width=True,
    )


    warning_box(
        """
        Une partie de la base <b>New Plant Diseases</b> contient des images très
        proches visuellement, compatibles avec la présence d'images issues
        d'une augmentation de données (<i>data augmentation</i>).
        """
    )


    st.divider()


    # =====================================================
    # ANALYSE DU CORPUS
    # =====================================================

    st.subheader("Analyse du corpus après déduplication")


    st.write(
        """
        L'ensemble des statistiques a été calculé **après suppression des
        doublons** afin de caractériser un corpus représentatif de la diversité
        réelle des images.
        """
    )


    kpi_row(
        [
            {
                "value": "96 165",
                "label": "IMAGES",
                "sub": "corpus final",
            },

            {
                "value": "256 × 256",
                "label": "RÉSOLUTION",
                "sub": "résolution unique",
            },

            {
                "value": "100 %",
                "label": "IMAGES CARRÉES",
                "sub": "format homogène",
            },
        ]
    )


    st.divider()


    # =====================================================
    # BASES GÉNÉRÉES
    # =====================================================
    st.subheader("Bases de données générées")

    col1, col2 = st.columns(2)

    with col1:
        info_box(
            """
            🌿 Base TAXONS
            • 14 espèces végétales
            • Identification de l'espèce
            • Classification taxonomique
            """
        )

    with col2:
        info_box(
            """
            🍃 Base MALADIES
            • 38 classes
            • États sains inclus
            • Diagnostic phytosanitaire
            """
        )


    st.write(
        """
        Les deux bases partagent exactement les **mêmes images**, mais
        disposent d'un **étiquetage différent** selon la tâche de
        classification (taxons ou maladies).
        """
    )
# =====================================================
# BASE TAXONS
# =====================================================

elif page == pages[1]:

    st.header("Base TAXONS")

    info_box(
        """
        Cette base contient 14 espèces végétales et permet
        l'identification automatique du taxon à partir d'une image.
        """
    )


# =====================================================
# BASE MALADIES
# =====================================================

elif page == pages[2]:

    st.header("Base MALADIES")

    info_box(
        """
        Cette base contient 38 classes correspondant aux différents
        états sanitaires des plantes, incluant les classes saines.
        """
    )
import streamlit as st
import pandas as pd

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
    "02",
    "Exploration des données",
    "")

# =====================================================
# MENU LATERAL
# =====================================================

st.sidebar.title("Exploration des données")

pages = [
    "Construction des bases",
    "Analyse des bases"]
  

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

    st.header("Base TAXONS / Base MALADIES")

    info_box(
        """
        
        🌿 <b>Base TAXONS</b> : identification de l'espèce végétale.<br>
        🍃 <b>Base MALADIES</b> : identification de l'état phytosanitaire
        de la feuille.
        """
    )


    # =====================================================
    # COMPARAISON DES BASES
    # =====================================================

    st.subheader("Comparaison des deux bases de données")


    col1, sep, col2 = st.columns([1, 0.03, 1])


    with col1:

        st.markdown("### 🌿 Base TAXONS")

        st.markdown(
            """
            **Objectif**  
            Reconnaître l'espèce végétale.

            **Nombre de classes**  
            14 taxons.

            **Difficulté principale**  
            Déséquilibre important entre espèces.

            **Classe majoritaire**  
            Tomate : 25 814 images

            **Classe minoritaire**  
            Courge : 2 170 images

            **Ratio important**  
            12 ×
            """
        )

        st.image(
            "images/Exploration/distribution_taxons.png",
            caption="Distribution des classes TAXONS",
            use_container_width=True
        )
    with sep:

        st.markdown(
            """
            <div style="
                height: 850px;
                border-left: 1px solid #DCDAE8;
                margin: auto;
            ">
            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown("### 🍃 Base MALADIES")

        st.markdown(
            """
            **Objectif**  
            Identifier l'état sanitaire de la plante

            **Nombre de classes**  
            38 classes

            **Difficulté principale**  
            Variabilité importante des symptômes visibles

            **Classe majoritaire**  
            Orange — citrus greening : 5 507 images

            **Classe minoritaire**  
            Maïs — cercospora : 2 052 images

            **Ratio modéré**  
            2,7 ×
            """
        )

        st.image(
            "images/Exploration/distribution_maladies.png",
            caption="Distribution des classes MALADIES",
            use_container_width=True
        )

    # =====================================================
    # ANALYSE COMPLÉMENTAIRE
    # =====================================================

    st.divider()


    st.subheader("Segmentation HSV")


    st.markdown(
        """
        Dans les approches classiques de vision par ordinateur, une segmentation
        HSV permet d'isoler l'objet d'intérêt.

        Pour notre corpus, elle n'est pas nécessaire :
        
        - fond uniforme et fort contraste avec la feuille 
        - risque de supprimer les symptômes colorés (jaune, brun, noir)
        - les CNN extraient directement les caractéristiques utiles depuis les images RGB.
        """
    )

    st.image(
                "images/Exploration/HSV.png",
                caption="Exemple de segmentation HSV",
                use_container_width=True
            )

    st.subheader("Conclusion de l'analyse exploratoire")

    success_box(
        """
        ✅ Corpus dédupliqué et homogène<br>
        ✅ Aucune segmentation nécessaire<br>
        ✅ Prétraitement limité au redimensionnement, à la normalisation
        et à la gestion du déséquilibre des classes.
        """
    )

    

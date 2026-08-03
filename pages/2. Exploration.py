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

    df_sources2 = pd.DataFrame(
        {
            "Niveau": [
                "1",
                "2",
            ],

            "Méthode": [
                "Hash MD5",
                "Perceptual Hash (pHash)",
            ],

            "Critère": [
                "Doublons exacts (fichiers binaires identiques)",
                "Quasi-doublons (distance de Hamming ≤ 2)",
            ],

        }
    )
    st.dataframe(df_sources2, use_container_width=True, hide_index=True)

    kpi_row(
        [
            {
                "value": "142 172",
                "label": "CORPUS INITIAL",
                "sub": "images brutes",
            },

            {
                "value": "- 45 866",
                "label": "DOUBLONS MD5",
                "sub": "hash binaire",
            },

            {
                "value": "- 141",
                "label": "QUASI-DOUBLONS",
                "sub": "pHash visuel",
            },
            {
                 "value": "96 165",
                "label": "BASE FINALE",
                "sub": "images uniques",
            },
        ]
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
                "value": "100 %",
                "label": "IMAGES CARRÉES",
                "sub": "format homogène JPG",
            },

            {
                "value": "256×256",
                "label": "PIXELS",
                "sub": "résolution unique",
            },

            {
                "value": "RGB",
                "label": "MODE COULEUR",
                "sub": "3 canaux",
            },


        ]
    )


    st.divider()

    st.subheader("Distribution de l'intensité lumineuse")

    st.markdown(
    """
    La luminosité moyenne des images a été calculée afin de vérifier
    l'homogénéité globale des conditions d'acquisition.

    La distribution montre que la majorité des images présentent une exposition
    correcte, avec très peu d'images extrêmement sombres ou très lumineuses.
    """
    )

    st.image(
        "images/Exploration/luminosite.png",
        caption="Distribution de la luminosité moyenne des images",
        use_container_width=True
    )

    kpi_row(
        [
            {
                "value": "18",
                "label": "MINIMUM",
                "sub": "image la plus sombre",
            },
            {
                "value": "119",
                "label": "MOYENNE",
                "sub": "intensité moyenne",
            },
            {
                "value": "244",
                "label": "MAXIMUM",
                "sub": "image la plus claire",
            },
        ]
    )


    st.divider()

    st.subheader("Exemples d'images du corpus")

    st.markdown(
    """
    Quelques exemples illustrant la diversité des espèces et des états sanitaires
    présents dans le corpus.
    """
    )

    st.image(
    "images/conditions.png",
    use_container_width=True,
    caption="Exemples d'images utilisées dans le corpus."
)

    st.markdown(
        """
        Une dominante verte homogène - cohérente avec des images de feuilles.
        Toutes les images ont été prises en conditions de laboratoire. 
        """
        )

    # cols = st.columns(4)

    # # images = [
    # #     ("images/Exploration/ex1.jpg", "Tomate saine"),
    # #     ("images/Exploration/ex2.jpg", "Pommier - Rouille"),
    # #     ("images/Exploration/ex3.jpg", "Maïs - Cercospora"),
    # #     ("images/Exploration/ex4.jpg", "Pêcher sain"),
    # # ]

    # for col, (img, cap) in zip(cols, images):
    #     with col:
    #         st.image(img, caption=cap, use_container_width=True)


    # =====================================================
    # BASES GÉNÉRÉES
    # =====================================================
   
# =====================================================
# BASE TAXONS
# =====================================================

elif page == pages[1]:

    st.subheader("Bases de données générées")
    
        # col1, col2 = st.columns(2)
    
        # with col1:
        #     info_box(
        #         """
        #         🌿 Base TAXONS
        #         • 14 espèces végétales
        #         • Identification de l'espèce
        #         • Classification taxonomique
        #         """
        #     )
    
        # with col2:
        #     info_box(
        #         """
        #         🍃 Base MALADIES
        #         • 38 classes
        #         • États sains inclus
        #         • Diagnostic phytosanitaire
        #         """
        #     )
    
    
    st.write(
            """
            Les deux bases partagent exactement les **mêmes images**, mais
            disposent d'un **étiquetage différent** selon la tâche de
            classification (taxons ou maladies).
            """
    )

    st.header("Base TAXONS / Base MALADIES")

    info_box(
        """
        
        🌿 <b>Base TAXONS</b> : identification de l'espèce végétale.<br>
        🦠 <b>Base MALADIES</b> : identification de l'état phytosanitaire
        de la feuille.
        """
    )


    # =====================================================
    # COMPARAISON DES BASES
    # =====================================================

    st.subheader("Comparaison des deux bases de données")


    col1, sep, col2 = st.columns([1, 0.03, 1])


    with col1:

        st.markdown("### 🌿 Base_TAXONS")
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

        st.markdown("### 🦠 Base_MALADIES")

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


    # st.subheader("Segmentation HSV")


    # st.markdown(
    #     """
    #     Dans les approches classiques de vision par ordinateur, une segmentation
    #     HSV permet d'isoler l'objet d'intérêt.

    #     Pour notre corpus, elle n'est pas nécessaire :
        
    #     - fond uniforme et fort contraste avec la feuille 
    #     - risque de supprimer les symptômes colorés (jaune, brun, noir)
    #     - les CNN extraient directement les caractéristiques utiles depuis les images RGB.
    #     """
    # )

    # st.image(
    #             "images/Exploration/HSV.png",
    #             caption="Exemple de segmentation HSV",
    #             use_container_width=True
    #         )


    # st.divider()


    st.subheader("Conclusion de l'analyse exploratoire")



    success_box(
        """
        ✅ Corpus dédupliqué et homogène 256x256 sans correction de luminosité ni de couleur nécessaire.<br>
        ✅ Une segmentation HSV explorée mais écartée<br>
        ✅ Prétraitement limité à la répartition stricte des splits, au redimensionnement, à la normalisation et à la gestion du déséquilibre des classes.
        
        ✅ Corpus dédupliqué et homogène<br>
        ✅ Aucune segmentation nécessaire<br>
        ✅ Prétraitement limité à la séparation des splits, au redimensionnement, à la normalisation
        et à la gestion du déséquilibre des classes.
        """
    )

    

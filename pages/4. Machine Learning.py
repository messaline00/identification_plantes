import streamlit as st
import pandas as pd
from pathlib import Path
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
    "04",
    "Machine Learning",
    "Comparaison des modèles sur TAXONS et MALADIES",
)


# =====================================================
# INTRODUCTION
# =====================================================


# =====================================================
# ONGLETS
# =====================================================

tab1, tab2, tab3 = st.tabs([
    "Protocole",
    "Résultats",
    "Conclusion",
])


# =====================================================
# 1. PROTOCOLE
# =====================================================

with tab1:



    st.markdown("""
    L'objectif est de comparer plusieurs modèles de **Machine Learning**
    sur deux représentations identiques des images, afin d'évaluer l'influence
    du modèle et de la représentation sur les performances.
    """)

    st.divider()

    st.subheader("Représentations utilisées")



    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="
                text-align: center;
                padding: 0.8rem;
                line-height: 1.8;
            ">
                <h4 style="
                    margin-bottom: 1rem;
                    color: #2AA99C;
                ">Pixels bruts</h4>
                <p>32 × 32 pixels</p>
                <p>vecteur aplati</p>
                <p>3 072 variables</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="
                text-align: center;
                padding: 0.8rem;
                line-height: 1.8;
            ">
                <h4 style="
                    margin-bottom: 1rem;
                    color: #2AA99C;
                ">HOG</h4>
                <p>Histogram of Oriented Gradients</p>
                <p>Contours et gradients</p>
                <p>1 764 variables</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("Modèles évalués")

    kpi_row(
        [
            {
                "value": "4",
                "label": "MODÈLES",
                "sub": "utilisés",
            },
            {
                "value": "2",
                "label": "TÂCHES",
                "sub": "espèces · maladies",
            },
            {
                "value": "2",
                "label": "REPRÉSENTATIONS",
                "sub": "pixels · HOG",
            },
        ]
    )

    # Espace entre les KPI et les modèles
    st.markdown("<div style='height: 30px'></div>", unsafe_allow_html=True)

    cols = st.columns(4)

    models = [
        ("01", "Régression\nlogistique"),
        ("02", "SGD\nhinge loss"),
        ("03", "Random\nForest"),
        ("04", "XGBoost"),
    ]

    for col, (num, name) in zip(cols, models):
        with col:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid rgba(128,128,128,0.25);
                    border-radius: 12px;
                    padding: 18px 12px;
                    text-align: center;
                    min-height: 105px;
                ">
                    <div style="
                        font-size: 13px;
                        opacity: 0.55;
                        margin-bottom: 10px;
                    ">{num}</div>
                    <div style="
                        font-size: 16px;
                        font-weight: 600;
                        line-height: 1.25;
                    ">{name.replace(chr(10), '<br>')}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )



# =====================================================
# ONGLET RESULTATS
# =====================================================

with tab2:

    st.header("Résultats")

    # =====================================================
    # COMPARAISON DES MODÈLES — ACCURACY TEST
    # =====================================================

    st.subheader("Comparaison des modèles — Accuracy test")

    df_accuracy = pd.DataFrame({
        "Modèle": [
            "Régression logistique", "Régression logistique",
            "SGD / SVM", "SGD / SVM",
            "Random Forest", "Random Forest",
            "XGBoost", "XGBoost",

            "Régression logistique", "Régression logistique",
            "SGD / SVM", "SGD / SVM",
            "Random Forest", "Random Forest",
            "XGBoost", "XGBoost"
        ],

        "Représentation": [
            "Pixels", "HOG",
            "Pixels", "HOG",
            "Pixels", "HOG",
            "Pixels", "HOG",

            "Pixels", "HOG",
            "Pixels", "HOG",
            "Pixels", "HOG",
            "Pixels", "HOG"
        ],

        "Base": [
            "TAXONS", "TAXONS",
            "TAXONS", "TAXONS",
            "TAXONS", "TAXONS",
            "TAXONS", "TAXONS",

            "MALADIES", "MALADIES",
            "MALADIES", "MALADIES",
            "MALADIES", "MALADIES",
            "MALADIES", "MALADIES"
        ],

        "Accuracy": [
            26.4, 50.2,
            59.4, 63.5,
            69.9, 68.1,
            85.1, 83.9,

            31.0, 28.8,
            54.6, 56.8,
            66.1, 57.9,
            81.4, 74.3
        ]
    })


    # =====================================================
    # GRAPHIQUES
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        df_taxons = df_accuracy[
            df_accuracy["Base"] == "TAXONS"
        ]

        fig_taxons = px.bar(
            df_taxons,
            x="Modèle",
            y="Accuracy",
            color="Représentation",
            barmode="group",
            text="Accuracy",
            title="🌿 TAXONS"
        )

        fig_taxons.update_traces(
            texttemplate="%{y:.0f}%",
            textposition="outside"
        )

        fig_taxons.update_layout(
            yaxis_title="Accuracy test (%)",
            xaxis_title=None,
            yaxis_range=[0, 100],
            legend_title=None
        )

        st.plotly_chart(
            fig_taxons,
            use_container_width=True
        )


    with col2:

        df_maladies = df_accuracy[
            df_accuracy["Base"] == "MALADIES"
        ]

        fig_maladies = px.bar(
            df_maladies,
            x="Modèle",
            y="Accuracy",
            color="Représentation",
            barmode="group",
            text="Accuracy",
            title="🦠 MALADIES"
        )

        fig_maladies.update_traces(
            texttemplate="%{y:.0f}%",
            textposition="outside"
        )

        fig_maladies.update_layout(
            yaxis_title="Accuracy test (%)",
            xaxis_title=None,
            yaxis_range=[0, 100],
            legend_title=None
        )

        st.plotly_chart(
            fig_maladies,
            use_container_width=True
        )


    # =====================================================
    # INTERPRÉTATION
    # =====================================================

    with st.container(border=True):

        st.markdown(
            """
            **XGBoost obtient les meilleures performances sur les deux bases.**

            - 🌿 **TAXONS : 85,1 %** avec pixels bruts
            - 🦠 **MALADIES : 81,4 %** avec les pixels bruts

            Les modèles linéaires (**régression logistique** et **SGD/SVM**) restent
            nettement en retrait, tandis que **Random Forest** améliore les performances
            mais reste inférieur à XGBoost.
            """
        )
    

    # =====================================================
    # GÉNÉRALISATION
    # =====================================================

    st.divider()

    st.subheader("⚠️ Généralisation — Train vs Test")


    # =====================================================
    # TAXONS
    # =====================================================

    st.markdown("### 🌿 TAXONS")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("#### Random Forest")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Pixels — Test", "71 %")
            st.caption("Train : 🔴 ≈ 100 %")

        with c2:
            st.metric("HOG — Test", "70 %")
            st.caption("Train : 🔴 ≈ 100 %")


    with col2:

        st.markdown("#### XGBoost")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Pixels — Test", "86 %")
            st.caption("Train : 🔴 ≈ 100 %")

        with c2:
            st.metric("HOG — Test", "86 %")
            st.caption("Train : 🔴 ≈ 100 %")


    # =====================================================
    # MALADIES
    # =====================================================

    st.markdown("### 🦠 MALADIES")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("#### Random Forest")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Pixels — Test", "67 %")
            st.caption("Train : 🔴 ≈ 100 %")

        with c2:
            st.metric("HOG — Test", "66 %")
            st.caption("Train : 🔴 ≈ 100 %")


    with col2:

        st.markdown("#### XGBoost")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Pixels — Test", "82 %")
            st.caption("Train : 🔴 ≈ 100 %")

        with c2:
            st.metric("HOG — Test", "76 %")
            st.caption("Train : 🔴 ≈ 100 %")


    # =====================================================
    # ANALYSE DU SURAPPRENTISSAGE
    # =====================================================

    st.markdown(
        "<div style='height: 20px;'></div>",
        unsafe_allow_html=True
    )

    warning_box(
        """
        **Les performances d'entraînement sont proches de 100 %, mais diminuent
        nettement sur les données de test.**

        Le phénomène est particulièrement marqué pour **Random Forest** :
        l'écart atteint **28 points sur TAXONS** et **33 points sur MALADIES**.

        Ces écarts mettent en évidence un **surapprentissage**, plus important
        pour Random Forest.
        """
    )



# =====================================================
# 3. ANALYSE DES MODÈLES
# =====================================================

with tab3:

    st.header("Conclusion — Machine Learning")


    # =====================================================
    # 1. IMPACT HOG VS PIXELS
    # =====================================================

    st.subheader("Impact de la représentation — HOG vs Pixels")

    with st.container(border=True):

    
        st.markdown(
            """
            **L'efficacité de HOG dépend de la tâche.**

            🌿 **TAXONS :** les **pixels bruts** obtiennent un léger avantage sur HOG
            (**85,1 % vs 83,9 %**), même si les deux représentations offrent des
            performances élevées pour distinguer les espèces.

            🦠 **MALADIES :** les **pixels bruts** sont nettement meilleurs
            (**81,4 % vs 74,3 %**), car HOG préserve moins bien les informations de
            **couleur** et de **texture** caractéristiques des symptômes.

            **HOG reste une représentation pertinente pour la morphologie des feuilles,
            mais les pixels bruts sont plus adaptés, en particulier pour la détection des maladies.**
            """
        )


    # =====================================================
    # 2. MEILLEUR MODÈLE — XGBOOST
    # =====================================================

    st.divider()

    st.subheader("XGBoost — Meilleur modèle classique")

    info_box(
        """
        **XGBoost obtient les meilleures performances parmi les modèles
        de Machine Learning.**
        """
    )


    # -----------------------------------------------------
    # TAXONS
    # -----------------------------------------------------

    st.markdown("### 🌿 Classification des taxons")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("F1-score", "83.9 %")
        st.caption("XGBoost — HOG")

    with col2:
        st.metric("F1-score", "85,1 %")
        st.caption("XGBoost — Pixels bruts")


    # -----------------------------------------------------
    # MALADIES
    # -----------------------------------------------------

    st.markdown("### 🦠 Classification des maladies")

    col1, col2 = st.columns(2)

    
    with col1:
        st.metric("F1-score", "73,3 %")
        st.caption("XGBoost — HOG")

    with col2:
            st.metric("F1-score", "81,4 %")
            st.caption("XGBoost — Pixels bruts")


    # =====================================================
    # 3. CONCLUSION
    # =====================================================

    st.divider()


    success_box(
        """
        Les modèles classiques restent limités par la **représentation des images** :
        l'aplatissement des pixels perd la structure spatiale, tandis que HOG perd
        une partie de l'information chromatique.

        **XGBoost atteint 85,1 % sur TAXONS et 81,4 % sur MALADIES**, mais présente
        également un écart important entre les performances d'entraînement et de test.

        Ces limites justifient l'utilisation de **réseaux de neurones convolutifs (CNN)**,
        capables d'exploiter directement la structure spatiale, la couleur et la texture
        des images.
        """
    )






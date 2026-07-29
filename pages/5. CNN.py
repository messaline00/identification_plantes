import streamlit as st
import pandas as pd
from pathlib import Path
import pandas as pd
import plotly.express as px

st.title("Réseaux de neurones convolutifs (CNN)")

tab_baseline, tab_tl, tab_conclusion = st.tabs(
    ["CNN Baseline", "Transfer Learning", "Conclusion"]
)
# =====================================================
# CNN BASELINE
# =====================================================
with tab_baseline:

    st.header("CNN Baseline")

    st.info(
        """
        Un **CNN** a été entraîné indépedamment pour les tâches de
        **classification des taxons** et des **maladies** afin de servir de
        modèle de référence (*baseline*).

        L'objectif est d'obtenir une architecture légère et rapide, qui sera
        ensuite comparée aux modèles de **Transfer Learning**.
        """
    )

    st.subheader("Méthodologie — Architecture et paramètres")

    df_baseline = pd.DataFrame({
        "Paramètre": [
            "Taille des images",
            "Rescaling",
            "Architecture",
            "Global Pooling",
            "Couche Dense",
            "Dropout",
            "Sortie",
            "Optimiseur",
            "Fonction de perte",
            "EarlyStopping",
            "Nombre d'époques max",
            "Nombre de paramètres"
        ],
        "Valeur": [
            "96 × 96",
            "1/255",
            "3 blocs Conv2D + MaxPooling (32, 64, 128 filtres)",
            "GlobalAveragePooling2D",
            "128 neurones",
            "0.3",
            "Softmax",
            "Adam",
            "SparseCategoricalCrossentropy",
            "Patience = 3 (restauration des meilleurs poids)",
            "15",
            "~112 000"
        ]
    })

    st.dataframe(
        df_baseline,
        use_container_width=True,
        hide_index=True
    )

    st.write(
        """
        Le même réseau est entraîné séparément sur les jeux de données
        **Taxons** et **Maladies**
        """
    )


# =====================================================
# TRANSFER LEARNING
# =====================================================
with tab_tl:

    st.header("Transfer Learning")

    st.info(
    """
    Trois architectures de **Transfer Learning** pré-entraînées sur **ImageNet** ont été évaluées
    pour la classification des **taxons** et des **maladies** des plantes :

    - **ResNet50**
    - **DenseNet121**
    - **EfficientNet-B3**

    Chaque modèle suit la même méthodologie : apprentissage par transfert, puis
    **fine-tuning** des dernières couches afin de les adapter aux images végétales.
    """
)

    
    
    st.subheader("Méthodologie — Paramètres du Transfer Learning")

    df_transfer = pd.DataFrame({
        "Paramètre": [
            "Taille des images",
            "Batch size",
            "Nombre d'époques",
            "Optimiseur",
            "Learning rate",
            "Fonction de perte",
            "Scheduler",
            "Patience scheduler"
        ],
        "ResNet50": [
            "224 × 224",
            "32",
            "10",
            "Adam",
            "0.001",
            "CrossEntropyLoss pondérée",
            "ReduceLROnPlateau",
            "3"
        ],
        "DenseNet121": [
            "224 × 224",
            "32",
            "10",
            "Adam",
            "0.001",
            "CrossEntropyLoss pondérée",
            "ReduceLROnPlateau",
            "3"
        ],
        "EfficientNet-B3": [
            "300 × 300",
            "32",
            "10",
            "Adam",
            "0.001",
            "CrossEntropyLoss pondérée",
            "ReduceLROnPlateau",
            "3"
        ]
    })

    st.dataframe(df_transfer, use_container_width=True, hide_index=True)

    st.write("""
    Après une première phase où seul le classifieur est entraîné, les dernières couches
    de chaque architecture sont dégelées afin d'adapter les représentations aux images de plantes.
    """)

    st.subheader("Méthodologie — Paramètres du Fine-Tuning")

    df_finetuning = pd.DataFrame({
        "Paramètre": [
            "Couche remplacée",
            "Couches dégelées",
            "Optimiseur",
            "Taux d'apprentissage",
            "Scheduler",
            "Nombre d'époques"
        ],
        "ResNet50": [
            "fc",
            "layer4",
            "Adam",
            "0.00001",
            "ReduceLROnPlateau",
            "5"
        ],
        "DenseNet121": [
            "classifier",
            "denseblock4 + norm5",
            "Adam",
            "0.00001",
            "ReduceLROnPlateau",
            "5"
        ],
        "EfficientNet-B3": [
            "classifier",
            "features.6 + features.7 + classifier",
            "Adam",
            "0.00001",
            "ReduceLROnPlateau",
            "5"
        ]
    })

    st.dataframe(df_finetuning, use_container_width=True, hide_index=True)

        # =====================================================
    # RESULTATS
    # =====================================================

    st.divider()

    st.subheader("Résultats")

    if "show_results" not in st.session_state:
        st.session_state.show_results = False

    if st.button("Afficher / Masquer les résultats"):
        st.session_state.show_results = not st.session_state.show_results


    if st.session_state.show_results:

        # ==========================
        # TAXONS
        # ==========================

        st.subheader("Classification des taxons")

        df_taxons = pd.DataFrame({
            "Architecture": [
                "ResNet50",
                "EfficientNet-B3",
                "DenseNet121"
            ],
            "Accuracy Test (%)": [
                99.77,
                99.62,
                99.56
            ],
            "F1-score Test (%)": [
                99.77,
                99.67,
                99.61
            ]
        })


        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Meilleur modèle",
                value="ResNet50"
            )

        with col2:
            st.metric(
                label="Accuracy Test",
                value="99.77 %"
            )


        fig_taxons = px.bar(
            df_taxons,
            x="Architecture",
            y="Accuracy Test (%)",
            text="Accuracy Test (%)",
            title="Accuracy Test - Classification des taxons",
        )

        fig_taxons.update_traces(
            marker_color="#8FBC8F",
            textposition="outside"
        )

        fig_taxons.update_layout(
            yaxis_range=[95,100],
            yaxis_title="Accuracy (%)",
            xaxis_title="",
            showlegend=False,
            height=450
        )

        st.plotly_chart(
            fig_taxons,
            use_container_width=True
        )


        st.success(
            "ResNet50 obtient les meilleures performances pour "
            "l'identification des taxons avec une Accuracy Test de 99,77 %."
        )


        st.divider()


        # ==========================
        # MALADIES
        # ==========================

        st.subheader("Classification des maladies")


        df_maladies = pd.DataFrame({
            "Architecture": [
                "EfficientNet-B3",
                "ResNet50",
                "DenseNet121"
            ],
            "Accuracy Test (%)": [
                99.22,
                99.08,
                98.78
            ],
            "F1-score Test (%)": [
                99.15,
                98.99,
                98.68
            ]
        })


        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Meilleur modèle",
                value="EfficientNet-B3"
            )

        with col2:
            st.metric(
                label="Accuracy Test",
                value="99.22 %"
            )


        fig_maladies = px.bar(
            df_maladies,
            x="Architecture",
            y="Accuracy Test (%)",
            text="Accuracy Test (%)",
            title="Accuracy Test - Classification des maladies",
        )


        fig_maladies.update_traces(
            marker_color="#8FBC8F",  # vert clair
            textposition="outside"
        )


        fig_maladies.update_layout(
            yaxis_range=[95,100],
            yaxis_title="Accuracy (%)",
            xaxis_title="",
            showlegend=False,
            height=450
        )


        st.plotly_chart(
            fig_maladies,
            use_container_width=True
        )


        st.success(
            "EfficientNet-B3 obtient les meilleures performances pour "
            "l'identification des maladies avec une Accuracy Test de 99,22 %."
        )


# =====================================================
# CONCLUSION
# =====================================================

# =====================================================
# CONCLUSION
# =====================================================

with tab_conclusion:

    st.header("Conclusion")

    st.info(
        """
        • Le CNN Baseline améliore l'Accuracy de près de **10 points**
        par rapport à XGBoost. 

        • Les modèles de Transfer Learning apportent un gain supplémentaire,
        atteignant des Accuracy supérieures à **99 %**.
        """
    )



    st.divider()

    # =====================================================
    # TAXONS
    # =====================================================

    st.subheader("🌿 Classification des taxons")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy", "85.90 %")
        st.caption("XGBoost")

    with col2:
        st.metric("Accuracy", "95.60 %")
        st.caption("CNN Baseline")

    with col3:
        st.markdown(
            "<h1 style='text-align:center;color:green;'>99.77 %</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='text-align:center;'><b>ResNet50 ✅</b></p>",
            unsafe_allow_html=True
        )

    st.divider()

    # =====================================================
    # MALADIES
    # =====================================================

    st.subheader("🍃 Classification des maladies")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy", "82.40 %")
        st.caption("XGBoost")

    with col2:
        st.metric("Accuracy", "95.77 %")
        st.caption("CNN Baseline")

    with col3:
        st.markdown(
            "<h1 style='text-align:center;color:green;'>99.22 %</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='text-align:center;'><b>EfficientNet-B3 ✅</b></p>",
            unsafe_allow_html=True
        )

    st.divider()

    st.success(
        """
        **Modèles retenus pour la phase de prédiction**

        Les meilleurs compromis entre précision et capacité de généralisation sont :

        ✅ **ResNet50** pour la **classification des taxons**

        ✅ **EfficientNet-B3** pour la **classification des maladies**

        Ces deux modèles sont ceux intégrés dans l'application pour réaliser
        les prédictions sur de nouvelles images.
        """
    )
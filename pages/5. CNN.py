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


    # =====================================================
    # RESULTATS
    # =====================================================

    st.divider()

    st.subheader("Résultats")

    if "show_results_baseline" not in st.session_state:
        st.session_state.show_results_baseline = False

    if st.button("Afficher / Masquer les résultats", key="baseline_results"):
        st.session_state.show_results_baseline = (
            not st.session_state.show_results_baseline
        )

    if st.session_state.show_results_baseline:

        # =====================================================
        # TAXONS
        # =====================================================

        st.subheader("Classification des taxons")

        col1, col2= st.columns(2)

        with col1:
            st.metric("Accuracy Test", "95,60 %")

        with col2:
            st.metric("F1-macro", "95,70 %")

    

        st.success(
            """
            Le CNN Baseline atteint une **Accuracy de 95,60 %** sur le jeu de test,
            avec un **F1-macro de 95,7 %**. Toutes les classes obtiennent un
            F1-score supérieur à **0,93**, y compris les classes rares
            (*blueberry*, *raspberry* et *squash*), ce qui constitue une nette
            amélioration par rapport aux modèles de Machine Learning.
            """
        )

        with st.expander("Analyse approfondie du CNN Baseline"):

            tab1, tab2 = st.tabs(
                [
                    "Courbes d'entraînement",
                    "Matrice de confusion"
                ]
            )

            # ==========================================
            # COURBES
            # ==========================================

            with tab1:

                st.write(
                    "Évolution de l'Accuracy et de la Loss au cours de l'entraînement."
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.image(
                        "images/CNN/baseline_taxons_accuracy.png",
                        caption="Accuracy (train / validation)",
                        use_container_width=True
                    )

                with col2:
                    st.image(
                        "images/CNN/baseline_taxons_loss.png",
                        caption="Loss (train / validation)",
                        use_container_width=True
                    )

            # ==========================================
            # MATRICE DE CONFUSION
            # ==========================================

            with tab2:

                st.image(
                    "images/CNN/baseline_taxons_confusion_matrix.png",
                    caption="Matrice de confusion - CNN Baseline (Taxons)",
                    use_container_width=True
                )

        st.divider()

        # =====================================================
        # MALADIES
        # =====================================================

        st.subheader("🍃 Classification des maladies")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Accuracy Test", "95,77 %")

        with col2:
            st.metric("F1-macro", "95,60 %")



        st.success(
            """
            Le CNN Baseline atteint une **Accuracy de 95,77 %** sur le jeu de test,
            avec un **F1-macro de 95,6 %**. Les performances les plus faibles
            concernent certaines maladies de la tomate (*target_spot*,
            *early_blight* et *late_blight*).
            """
        )

        with st.expander("Analyse approfondie du CNN Baseline"):

            tab1, tab2 = st.tabs(
                [
                    "Courbes d'entraînement",
                    "Matrice de confusion"
                ]
            )

            # ==========================================
            # COURBES
            # ==========================================

            with tab1:

                st.write(
                    "Évolution de l'Accuracy et de la Loss au cours de l'entraînement."
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.image(
                        "images/CNN/baseline_maladies_accuracy.png",
                        caption="Accuracy (train / validation)",
                        use_container_width=True
                    )

                with col2:
                    st.image(
                        "images/CNN/baseline_maladies_loss.png",
                        caption="Loss (train / validation)",
                        use_container_width=True
                    )

            # ==========================================
            # MATRICE DE CONFUSION
            # ==========================================

            with tab2:

                st.image(
                    "images/CNN/baseline_maladies_confusion_matrix.png",
                    caption="Matrice de confusion - CNN Baseline (Maladies)",
                    use_container_width=True
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



        # =====================================================
        # ANALYSE DETAILLEE
        # =====================================================

        with st.expander("Analyse approfondie du modèle ResNet50"):

            tab1, tab2, tab3 = st.tabs(
                [
                    "Courbes d'entraînement",
                    "Matrice de confusion",
                    "Grad-CAM"
                ]
            )

            # =====================================================
            # COURBES
            # =====================================================

            with tab1:

                st.write(
                    "Évolution de l'Accuracy et de la Loss au cours de l'entraînement."
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.image(
                        "images/CNN/resnet50_accuracy.png",
                        caption="Accuracy (train / validation)",
                        use_container_width=True
                    )

                with col2:
                    st.image(
                        "images/CNN/resnet50_loss.png",
                        caption="Loss (train / validation)",
                        use_container_width=True
                    )

            # =====================================================
            # MATRICE DE CONFUSION
            # =====================================================

            with tab2:

                st.write(
                    "Matrice de confusion obtenue sur le jeu de test."
                )

                st.image(
                    "images/CNN/resnet50_confusion_matrix.png",
                    caption="Matrice de confusion - ResNet50",
                    use_container_width=True
                )

            # =====================================================
            # GRAD-CAM
            # =====================================================

            with tab3:

                st.write(
                    """
                    Les cartes **Grad-CAM** mettent en évidence les régions de l'image
                    ayant le plus contribué à la décision du modèle.
                    """
                )

                st.image(
                    "images/CNN/resnet50_gradcam.png",
                    caption="Exemples de visualisations Grad-CAM obtenues avec ResNet50",
                    use_container_width=True
                )

                


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
        # ANALYSE DETAILLEE
        # =====================================================

        with st.expander("Analyse approfondie du modèle EfficientNet-B3"):

            tab1, tab2, tab3 = st.tabs(
                [
                    "Courbes d'entraînement",
                    "Matrice de confusion",
                    "Grad-CAM"
                ]
            )

            # =====================================================
            # COURBES
            # =====================================================

            with tab1:

                st.write(
                    "Évolution de l'Accuracy et de la Loss au cours de l'entraînement."
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.image(
                        "images/CNN/efficientnet_accuracy.png",
                        caption="Accuracy (train / validation)",
                        use_container_width=True
                    )

                with col2:
                    st.image(
                        "images/CNN/efficientnet_loss.png",
                        caption="Loss (train / validation)",
                        use_container_width=True
                    )

            # =====================================================
            # MATRICE DE CONFUSION
            # =====================================================

            with tab2:

                st.write(
                    "Matrice de confusion obtenue sur le jeu de test."
                )

                st.image(
                    "images/CNN/efficientnet_confusion_matrix.png",
                    caption="Matrice de confusion - EfficientNet-B3",
                    use_container_width=True
                )

            # =====================================================
            # GRAD-CAM
            # =====================================================

            with tab3:

                st.write(
                    """
                    Les cartes **Grad-CAM** mettent en évidence les régions de l'image
                    ayant le plus contribué à la décision du modèle.
                    """
                )

                st.image(
                    "images/CNN/efficientnet_gradcam.png",
                    caption="Exemples de visualisations Grad-CAM obtenues avec EfficientNet-B3",
                    use_container_width=True
                )



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
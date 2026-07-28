import streamlit as st
import pandas as pd
from pathlib import Path
import pandas as pd

st.title("Réseaux de neurones convolutifs (CNN)")

tab_baseline, tab_tl = st.tabs(["CNN Baseline", "Transfer Learning"])

# =====================================================
# CNN BASELINE
# =====================================================
with tab_baseline:

    st.header("CNN Baseline")

    st.write("À compléter...")

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
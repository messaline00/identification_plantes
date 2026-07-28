import torch
import torch.nn as nn
import streamlit as st
from torchvision import models
import json
import joblib

#Import ResNet
@st.cache_resource
def load_resnet_model():

    with open("models/ResNet50/resnet50_config.json", "r") as f:
        config = json.load(f)

    num_classes = config["num_classes"]

    model = models.resnet50(weights=None)

    model.fc = nn.Linear(
        model.fc.in_features,
        num_classes
    )

    model.load_state_dict(
        torch.load(
            "models/ResNet50/resnet50_taxons_finetuned.pth",
            map_location="cpu"
        )
    )

    model.eval()

    return model

#Import EfficientNet
@st.cache_resource
def load_efficientnet_model():

    with open("models/EfficientNet_B3_maladies/efficientnet_b3_config.json", "r") as f:
        config = json.load(f)

    num_classes = config["num_classes"]

    model = models.efficientnet_b3(weights=None)

    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features,
        num_classes
    )

    model.load_state_dict(
        torch.load(
            "models/EfficientNet_B3_maladies/efficientnet_b3_finetuned.pth",
            map_location="cpu"
        )
    )

    model.eval()

    return model

@st.cache_resource
def load_resnet_label_encoder():

    return joblib.load(
        "models/ResNet50/resnet50_label_encoder.pkl"
    )

@st.cache_resource
def load_eff_label_encoder():

    return joblib.load(
        "models/EfficientNet_B3_maladies/efficientnet_b3_label_encoder.pkl"
    )
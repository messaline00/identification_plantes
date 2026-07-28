import numpy as np

import torch

from PIL import Image

from torchvision.transforms.functional import to_pil_image

from pytorch_grad_cam import GradCAM

from pytorch_grad_cam.utils.image import show_cam_on_image

from utils.load_models import (
    load_resnet_model,
    load_efficientnet_model
)

from utils.preprocessing import (
    preprocess_resnet,
    preprocess_efficientnet
)

def generate_resnet_gradcam(image):

    """
    Génère une visualisation Grad-CAM avec ResNet50.
    """

    model = load_resnet_model()

    model.eval()

    # Prétraitement identique à la prédiction
    input_tensor = preprocess_resnet(image)

    # Couche cible ResNet50
    target_layers = [
        model.layer4[-1]
    ]

    cam = GradCAM(
        model=model,
        target_layers=target_layers
    )

    grayscale_cam = cam(
        input_tensor=input_tensor
    )[0]

    # Image originale en RGB entre 0 et 1
    rgb_img = np.array(
        image.resize((224, 224))
    ).astype(np.float32) / 255.0


    visualization = show_cam_on_image(
        rgb_img,
        grayscale_cam,
        use_rgb=True
    )

    return Image.fromarray(
        visualization
    )

def generate_efficientnet_gradcam(image):

    """
    Génère une visualisation Grad-CAM avec EfficientNet-B3.
    Utilisé pour la classification des maladies.
    """

    model = load_efficientnet_model()

    model.eval()

    # Prétraitement identique à l'entraînement EfficientNet
    input_tensor = preprocess_efficientnet(image)

    # Dernière couche convolutionnelle EfficientNet-B3
    target_layers = [
        model.features[-1]
    ]

    cam = GradCAM(
        model=model,
        target_layers=target_layers
    )

    grayscale_cam = cam(
        input_tensor=input_tensor
    )[0]


    # EfficientNet utilise une image 300x300
    rgb_img = np.array(
        image.resize((300, 300))
    ).astype(np.float32) / 255.0


    visualization = show_cam_on_image(
        rgb_img,
        grayscale_cam,
        use_rgb=True
    )


    return Image.fromarray(
        visualization
    )
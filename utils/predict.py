import torch

from utils.load_models import (
    load_resnet_model,
    load_efficientnet_model,
    load_resnet_label_encoder,
    load_eff_label_encoder,
)

from utils.preprocessing import (
    preprocess_resnet,
    preprocess_efficientnet,
)

# Chargement des modèles
resnet_model = load_resnet_model()
efficientnet_model = load_efficientnet_model()

# Chargement des LabelEncoder
resnet_encoder = load_resnet_label_encoder()
eff_encoder = load_eff_label_encoder()


def format_label(label):
    """
    Transforme un label du type :
    tomato___late_blight
    en :
    Tomato - Late Blight
    """

    return (
        label.replace("___", " - ")
             .replace("_", " ")
             .title()
    )
def get_disease_name(disease_label):
    """
    Extrait uniquement le nom de la maladie.

    Exemple :
    Tomato - Late Blight -> Late Blight
    Apple - Healthy -> Healthy
    """

    if " - " in disease_label:
        return disease_label.split(" - ", 1)[1]

    return disease_label


def get_health_status(disease_label):
    """
    Retourne True si la plante est saine.
    """
    return "Healthy" in disease_label


def predict_taxon(image):
    """
    Prédit le taxon de la plante.

    Retour :
        label : str
        confidence : float
        top5 : list[(classe, probabilité)]
    """

    image = preprocess_resnet(image)

    with torch.no_grad():

        outputs = resnet_model(image)

        probabilities = torch.softmax(outputs, dim=1)

        predicted = torch.argmax(probabilities, dim=1).item()

        confidence = probabilities[0, predicted].item()

        label = format_label(
            resnet_encoder.inverse_transform([predicted])[0]
        )

        top5_prob, top5_idx = torch.topk(probabilities, k=5)

        top5 = []

        for prob, idx in zip(top5_prob[0], top5_idx[0]):

            classe = format_label(
                resnet_encoder.inverse_transform([idx.item()])[0]
            )

            top5.append(
                (
                    classe,
                    prob.item()
                )
            )

    return label, confidence, top5


def predict_disease(image):
    """
    Prédit la maladie de la plante.

    Retour :
        label : str
        confidence : float
        top5 : list[(classe, probabilité)]
    """

    image = preprocess_efficientnet(image)

    with torch.no_grad():

        outputs = efficientnet_model(image)

        probabilities = torch.softmax(outputs, dim=1)

        predicted = torch.argmax(probabilities, dim=1).item()

        confidence = probabilities[0, predicted].item()

        label = format_label(
            eff_encoder.inverse_transform([predicted])[0]
        )

        top5_prob, top5_idx = torch.topk(probabilities, k=5)

        top5 = []

        for prob, idx in zip(top5_prob[0], top5_idx[0]):

            classe = format_label(
                eff_encoder.inverse_transform([idx.item()])[0]
            )

            top5.append(
                (
                    classe,
                    prob.item()
                )
            )

    return label, confidence, top5
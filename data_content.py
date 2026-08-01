# Toutes les données chiffrees viennent des rapports :
# - rapport_plantes_Liora (Exploration & Pretraitement)
# - rapport_plantes_Modelisation_Liora (Modelisation)

TEAM = "Messaline Alarcon · Paul El Forzli · Ghislain Kouadio Bi · Bronislaw Podhajski"

TEAM_MEMBERS = [
    {"prenom": "Messaline", "nom": "Alarcon", "photo": None},
    {"prenom": "Paul", "nom": "El Forzli", "photo": None},
    {"prenom": "Ghislain", "nom": "Kouadio Bi", "photo": "assets/team_ghislain.jpg"},
    {"prenom": "Bronislaw", "nom": "Podhajski", "photo": None},
]

# --- Corpus ---
CORPUS_INITIAL = 142172
DOUBLONS_MD5 = 45866
QUASI_DOUBLONS = 141
CORPUS_FINAL = 96165

# --- TAXONS : distribution connue precisement (tomato et squash cites dans le rapport) ---
TAXONS_TOP_CLASS = {"name": "tomato", "fr": "Tomate", "count": 25814, "pct": 26.8}
TAXONS_RARE_CLASS = {"name": "squash", "fr": "Courge", "count": 2170}
TAXONS_RATIO = 12
TAXONS_N_CLASSES = 14

TAXONS_TABLE = [
    ("apple", "Pommier", "Malus domestica", "Espèce"),
    ("blueberry", "Myrtille", "Vaccinium corymbosum", "Espèce"),
    ("cherry_including_sour", "Cerisier (doux et acide)", "Prunus avium / Prunus cerasus", "Genre (Prunus)"),
    ("grape", "Vigne", "Vitis vinifera", "Espèce"),
    ("maize", "Maïs", "Zea mays", "Espèce"),
    ("orange", "Oranger", "Citrus × sinensis", "Espèce (hybride)"),
    ("peach", "Pêcher", "Prunus persica", "Espèce"),
    ("pepper_bell", "Poivron", "Capsicum annuum", "Espèce"),
    ("potato", "Pomme de terre", "Solanum tuberosum", "Espèce"),
    ("raspberry", "Framboisier", "Rubus idaeus", "Espèce"),
    ("soybean", "Soja", "Glycine max", "Espèce"),
    ("squash", "Courge", "Cucurbita spp.", "Genre (Cucurbita)"),
    ("strawberry", "Fraisier", "Fragaria × ananassa", "Espèce (hybride)"),
    ("tomato", "Tomate", "Solanum lycopersicum", "Espèce"),
]

# --- MALADIES ---
MALADIES_N_CLASSES = 38
MALADIES_TOP_CLASS = {"name": "orange___haunglongbing", "fr": "Oranger - Huanglongbing", "count": 5507}
MALADIES_RARE_CLASS = {"name": "maize___cercospora", "fr": "Maïs - Cercosporiose", "count": 2052}
MALADIES_RATIO = 2.7
MALADIES_SAIN_PCT = 31.5
MALADIES_MALADE_PCT = 68.5
MALADIES_SAIN_N = 30308
MALADIES_MALADE_N = 65857
MALADIES_N_ESPECES = 14
MALADIES_N_FONGIQUE = 17

# --- Qualite / audit ---
RESOLUTION = "256 × 256"
LUMINOSITE_MOYENNE = 123
RGB_DOMINANT = "R 122 · G 128 · B 108"
PCT_JPG = 99.999
PCT_RGB = 99.999
IMAGES_PETITES_N = 10352
IMAGES_PETITES_PCT = 10.8

# --- Contre-audit / label noise ---
CONTRE_AUDIT_COMPARISONS = "~4 millions"
CONTRE_AUDIT_TAUX = "~0,0001 %"
LABEL_NOISE_TAXONS_FAMILLES = 94355
LABEL_NOISE_MALADIES_FAMILLES = 94374
LABEL_NOISE_DELTA = 19

# --- Splits ---
SPLIT_TRAIN_PCT, SPLIT_VAL_PCT, SPLIT_TEST_PCT = 70, 15, 15
TAXONS_SPLIT = {"train": 67377, "val": 14370, "test": 14418}
MALADIES_SPLIT = {"train": 67339, "val": 14402, "test": 14424}

# --- Machine Learning (accuracy test, %) ---
ML_RESULTS = {
    "taxons": {
        "Régression logistique": {"pixels": 37.3, "hog": 53.4},
        "SGD (hinge) ≈ SVM": {"pixels": 63.1, "hog": 68.0},
        "Random Forest": {"pixels": 71.4, "hog": 69.8},
        "XGBoost": {"pixels": 85.7, "hog": 85.9},
    },
    "maladies": {
        "Régression logistique": {"pixels": 33.6, "hog": 31.5},
        "SGD (hinge) ≈ SVM": {"pixels": 55.2, "hog": 59.8},
        "Random Forest": {"pixels": 67.4, "hog": 59.9},
        "XGBoost": {"pixels": 82.4, "hog": 75.5},
    },
}
ML_BEST = "XGBoost"

# --- CNN Baseline (from scratch) ---
CNN_BASELINE = {
    "taxons": {"acc_test": 95.60, "f1_test": 95.6, "n_params": 111566},
    "maladies": {"acc_test": 95.77, "f1_test": 95.8, "n_params": 114662},
}

# --- CNN Optimise (transfer learning) ---
CNN_OPT = {
    "taxons": {
        "ResNet50": {"acc_train": 99.89, "acc_val": 99.74, "acc_test": 99.77, "f1_test": 99.77},
        "EfficientNet-B3": {"acc_train": 99.69, "acc_val": 99.61, "acc_test": 99.62, "f1_test": 99.67},
        "DenseNet121": {"acc_train": 99.62, "acc_val": 99.52, "acc_test": 99.56, "f1_test": 99.61},
    },
    "maladies": {
        "ResNet50": {"acc_train": 99.66, "acc_val": 99.21, "acc_test": 99.08, "f1_test": 98.99},
        "EfficientNet-B3": {"acc_train": 99.47, "acc_val": 99.13, "acc_test": 99.22, "f1_test": 99.15},
        "DenseNet121": {"acc_train": 99.45, "acc_val": 99.99, "acc_test": 98.78, "f1_test": 98.68},
    },
}
CNN_OPT_BEST_TAXONS = "ResNet50"
CNN_OPT_BEST_MALADIES = "EfficientNet-B3"

# --- Hypotheses (version courante : 2 retenues) ---
HYPOTHESES = [
    {
            "id": "H1",
            "titre": "CNN optimisé",
            "enonce": "Le CNN optimisé par transfer learning obtient de meilleures performances que les autres modèles pour l'identification du taxon et le diagnostic de la maladie.",
            "verdict": "confirmee",
            "verdict_label": "Confirmée",
            "constat": (
                "+4,17 points sur TAXONS (95,60 % → 99,77 % avec ResNet50) et +3,45 points sur "
                "MALADIES (95,77 % → 99,22 % avec EfficientNet-B3) par rapport au CNN baseline — "
                "l'écart est encore plus net face au Machine Learning classique, plafonné à 85,9 % "
                "et 82,4 %. La convergence est aussi plus rapide : dès la phase tête gelée, les "
                "modèles pré-entraînés dépassent déjà 97 % d'accuracy, là où le baseline part de "
                "41 % et met 15 epochs à converger."
            ),
        },
    {
        "id": "H2",
        "titre": "Morphologie",
        "enonce": "Les caractéristiques visuelles des feuilles permettent d'identifier automatiquement l'espèce avec une précision élevée.",
        "verdict": "partielle",
        "verdict_label": "Partiellement confirmée",
        "constat": (
            "L'identification de l'espèce fonctionne très bien sur les données du projet "
            "(jusqu'à 99,77 % d'accuracy) ; un descripteur de forme pur (HOG) obtient déjà "
            "85,9 % en Machine Learning, un indice cohérent avec l'hypothèse. Le volet "
            "« conditions non contrôlées » a été testé en direct sur 6 photos de terrain à "
            "vérité terrain connue : les 4 photos d'espèces réellement présentes dans les 14 "
            "classes ont toutes été correctement identifiées par le taxon (4/4), avec un "
            "diagnostic correct dans 3 cas sur 4. Sur les 2 photos volontairement hors "
            "périmètre, le résultat le plus instructif : le modèle a signalé son incertitude "
            "sur l'une (39,6 %, alerte affichée) mais a répondu avec une confiance trompeuse "
            "sur l'autre (96,5 %, aucune alerte déclenchée). Un indice globalement favorable, "
            "donc, mais un échantillon encore trop restreint (n=6) pour valider l'hypothèse "
            "dans son ensemble."
        ),
    }
    
]















# --- Comparaison globale ---
GLOBAL_COMPARISON = [
    {"famille": "Machine Learning", "modele": "XGBoost", "taxons": 83.9, "maladies": 81.4},
    {"famille": "CNN baseline", "modele": "From scratch", "taxons": 95.6, "maladies": 95.8},
    {"famille": "CNN optimisé", "modele": "ResNet50 (TAXONS) · EfficientNet-B3 (MALADIES)", "taxons": 99.77, "maladies": 99.15},
]

# --- Limites (section 5.5 du rapport modelisation) ---
LIMITES = [
    ("Interprétabilité", "Certains modèles (DenseNet121 en tête) s'appuient ponctuellement sur des régions extérieures à la feuille."),
    ("Confusions entre classes proches", "tomato/potato pour TAXONS, paires de maladies du maïs ou de la tomate pour MALADIES."),
    ("Qualité d'image", "Luminosité forte, feuille pliée, feuillage dense reviennent dans les erreurs de tous les modèles."),
    ("Conditions d'acquisition contrôlées", "Fond neutre, éclairage stable pour l'entraînement et l'évaluation systématique ; deux démonstrations en conditions de terrain (9 photos au total) donnent un premier indice favorable sur les espèces connues, mais restent anecdotiques."),
    ("Fiabilité de l'alerte de confiance", "Le seuil d'alerte (< 60 %) ne détecte pas systématiquement les cas hors périmètre : sur 2 photos volontairement hors des 14 classes testées en démonstration, l'alerte s'est déclenchée sur une seule des deux — l'autre a reçu une réponse fausse à 96,5 % de confiance, sans avertissement."),
    ("Coût de déploiement", "Un paramètre, c'est une valeur numérique apprise par le réseau pendant l'entraînement ; plus il y en a, plus le modèle est gros et lent à faire tourner. Les CNN optimisés en ont 8 à 25 millions (ResNet50, DenseNet121, EfficientNet-B3), contre ~112 000 pour le baseline — 100 à 200 fois moins. En pratique : le baseline tiendrait dans une appli smartphone sans connexion ; les CNN optimisés ont besoin d'un serveur, comme dans cette démonstration."),
    ("Périmètre du Machine Learning testé", "Le SVM à noyau (SVC) n'a pas été mené à terme."),
]

PERSPECTIVES = (
    "Les démonstrations donnent un premier aperçu encourageant sur les espèces connues (4/4 "
    "taxons corrects), mais révèlent que l'alerte de confiance ne détecte pas systématiquement "
    "les cas hors périmètre (1 cas sur 2 raté sans avertissement) : fiabiliser cette alerte "
    "(détection d'anomalie plus robuste qu'un simple seuil) et élargir les tests à un "
    "échantillon large et systématique sont deux pistes prioritaires ; explorer une "
    "distillation des CNN optimisés pour un déploiement mobile."
)

# --- Synthese finale (page Conclusion) ---
SYNTHESE_FINALE = [
    "Le Machine Learning classique plafonne loin des besoins du projet (85,9 % / 82,4 % "
    "d'accuracy au mieux), pénalisé par la perte de structure spatiale et, pour HOG, de "
    "l'information colorimétrique.",
    "Un CNN baseline compact (~112 000 paramètres), sans aucun pré-entraînement, suffit déjà "
    "à dépasser tous les modèles de Machine Learning de 10 à 13 points.",
    "Le transfer learning referme la quasi-totalité de l'écart restant : jusqu'à 99,77 % de "
    "F1 test, contre 95,6-95,8 % pour le baseline.",
    "H1 confirmée : le CNN optimisé surpasse toutes les autres approches, sur les deux tâches.",
    "H2 partiellement confirmée : la morphologie suffit très bien sur les espèces connues "
    "(4/4 en démonstration), mais la vigilance du système face à l'inconnu reste imparfaite "
    "(1 cas sur 2 détecté).",
]

CLOSING = (
    "Le projet répond concrètement à la question posée en introduction : à partir d'une "
    "seule photo, identifier une plante et détecter une maladie avec une fiabilité élevée "
    "est possible, sur les cas que le modèle connaît. La marche suivante consiste à étendre "
    "cette fiabilité au terrain, dans toute sa variabilité."
)
DEMO_TEST_6 = [
    {"n": 1, "sujet": "Maïs (sain)", "attendu": "Espèce connue", "taxon_pred": "Maize", "taxon_conf": 98.38,
     "taxon_ok": True, "diag_pred": "Maize - Healthy", "diag_conf": 98.96, "diag_ok": True},
    {"n": 2, "sujet": "Tomate (jeune plant)", "attendu": "Espèce connue", "taxon_pred": "Tomato", "taxon_conf": 85.99,
     "taxon_ok": True, "diag_pred": "Pepper Bell - Healthy", "diag_conf": 57.61, "diag_ok": False},
    {"n": 3, "sujet": "Tomate — mildiou", "attendu": "Espèce + maladie connues", "taxon_pred": "Tomato", "taxon_conf": 96.86,
     "taxon_ok": True, "diag_pred": "Tomato - Late Blight", "diag_conf": 78.74, "diag_ok": True},
    {"n": 4, "sujet": "Maïs — taches brunes", "attendu": "Espèce + maladie connues", "taxon_pred": "Maize", "taxon_conf": 100.0,
     "taxon_ok": True, "diag_pred": "Maize - Northern Leaf Blight", "diag_conf": 92.41, "diag_ok": True},
    {"n": 5, "sujet": "Poivre (Piper) — hors périmètre", "attendu": "Hors des 14 classes", "taxon_pred": "Strawberry", "taxon_conf": 39.60,
     "taxon_ok": None, "diag_pred": "Pepper Bell - Healthy", "diag_conf": 93.42, "diag_ok": False},
    {"n": 6, "sujet": "Concombre — hors périmètre", "attendu": "Hors des 14 classes", "taxon_pred": "Strawberry", "taxon_conf": 96.52,
     "taxon_ok": None, "diag_pred": "Tomato - Healthy", "diag_conf": 45.85, "diag_ok": None},
]
# ok=True : correct | ok=False : incorrect avec confiance (pas d'alerte) | ok=None : cas hors perimetre (pas de bonne reponse possible, on juge la calibration)

import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

st.title("Modèles de Machine Learning")

st.sidebar.title("Modèles de Machine Learning")
pages=["Objectifs et prétraitements", "Régression Linéaire", "SGD Classifier", "Random Forest", "XG Boost"]
page=st.sidebar.radio("Choisir un modèle", pages)


######### OBJECTIFS ET PRETRAITEMENTS
if page == pages[0]:
  st.markdown("L'objectif de cette partie est d'évaluer la capacité de chaque modèle à classifier les images de plantes selon deux problématiques : (1) classification des taxons, à savoir l’identification de l’espèce représentée sur l’image, et (2) classification des maladies, à savoir l’identification de l’état de santé de la plante et le diagnostic de sa maladie. ")
  st.markdown("Nous utilisons deux types de représentation informatique des images pour comparer les performances du modèle sur ces deux représentations. ")
  st.markdown("""
    * les pixels bruts (raw pixels), qui conservent directement l'information colorimétrique de l'image pixel par pixel ;
    * les descripteurs HOG (Histogram of Oriented Gradients), qui décrivent les contours et les structures locales de l'image.
    """)
  st.subheader("Prétraitement des données")
  st.markdown("Le prétraitement réalisé est le suivant :")
  st.markdown("""
        * Redimensionnement des images en 32 × 32 pixels, 
        * Conversion en format RGB, 
        * Transformation en tableau de pixels, 
        * Aplatissement du tableau pour obtenir un vecteur de 3072 variables (32 × 32 × 3)
    """)

######### REGRESSION LINEAIRE ####################################################
if page == pages[1]:
  st.header("Régression linéaire")


######### SGD CLASSIFIER ####################################################
if page == pages[2]:
  st.header("SGD Classifier")
  onglet1, onglet2, onglet3, onglet4 = st.tabs(["Généralités", "Taxons", "Maladies", "Conclusion"])

  with onglet1:
    st.subheader("Hyperparamètres")
    st.markdown("Une évaluation des hyperparamètres par **GridSearch** a été effectuée pour rechercher les meilleures valeurs des paramètres alpha (coefficient de régularisation) et tol (tolérance de convergence) sur la base taxons avec les données sous forme de pixels bruts. Les paramètres retenus pour le modèle SGD Classifier sont les suivants :")
    st.code("""
    model = SGDClassifier(loss='hinge', 
      alpha=1e-4,
      max_iter=1000,
      tol=1e-3,
      class_weight='balanced',
      random_state=42,
      n_jobs=-1)""", language = 'python')

  with onglet2:
    st.write("Sur les base des taxons")
    resultats = pd.DataFrame({
      "Accuracy\nTrain": [0.678, 0.704],
      "Accuracy\nValidation": [0.634, 0.689],
      "Accuracy\nTest": [0.631, 0.680],
      "F1-score\nTrain": [0.646, 0.664],
      "F1-score\nValidation": [0.596, 0.643],
      "F1-score\nTest": [0.594, 0.635]}, index=["Pixels", "HOG"])
    st.table(resultats)
    st.markdown("Les résultats montrent que le SGD Classifier est plus efficace sur le set HOG que ce soit en termes d’accuracy que de score F1 ; ils montrent également que **le set HOG minimise le surapprentissage**. En effet, le score d’**accuracy atteint 70,4% sur le set HOG** contre 67,8% sur le set pixels bruts, et le **surapprentissage passe de 4,7 points à 2,4 points**. Le F1-score, qui nous intéresse particulièrement étant donné que les classes sont déséquilibrées, s’élève à 66,4% sur le jeu d’entraînement et 63,5% sur le jeu de test. ")
    st.markdown("Dans les deux cas, **la classe apple est la moins bien identifiée** (0,23 de recall et 0,31 de F1 sur le jeu pixels, et 0,19 de recall et 0,31 de F1 sur le jeu HOG), dans le sens où le modèle ne parvient pas à la reconnaître. Les classes les mieux reconnues sur le pixels bruts sont les grape (0,79 de F1), maize (0,88 de F1) et orange (0,83 de F1). Les mieux reconnues sur le HOG sont les mêmes avec des F1 respectifs de 0,87, 0,87 et 0,91. Certaines classes sont plutôt bien prédites (bonne accuracy) mais sont aussi sur-prédites ; c’est le cas de tomato pour les deux jeux de données, de pepper_bell pour les données pixel et de potato pour les données HOG. ")
    with st.expander("Diagnostic du sur-apprentissage"):
      st.image(BASE_DIR / "images" / "ML_SGD" / "taxons_overfitting.png", width = 500)
    with st.expander("Matrice de confusion"):
      st.image(BASE_DIR / "images" / "ML_SGD" / "taxons_confusion.png", width = 500)

  with onglet3:
    st.write("Sur les base des maladies")
    resultats = pd.DataFrame({
      "Accuracy\nTrain": [0.655, 0.650],
      "Accuracy\nValidation": [0.551, 0.597],
      "Accuracy\nTest": [0.552, 0.598],
      "F1-score\nTrain": [0.655, 0.628],
      "F1-score\nValidation": [0.543, 0.568],
      "F1-score\nTest": [0.546, 0.568]}, index=["Pixels", "HOG"])
    st.table(resultats)
    st.markdown("Les résultats sur les images de maladies sont plus mitigés. Les accuracy sur l’ensemble d’entraînement sont meilleures sur les données pixels bruts, mais le surapprentissage est tel qu’elles sont meilleures pour le test avec les HOG. En effet, **le surapprentissage représente plus de 10 points sur le set pixels bruts**, avec une accuracy passant de 65,5% à 55,2% et un F1 passant de 65,5% à 54,6%. Il est réduit de moitié sur le set HOG, passant de 65% à 59,8% pour l’accuracy, et de 62,8% à 56,8% pour le F1. Ce surapprentissage reste néanmoins trop significatif pour que le modèle soit satisfaisant.")    
    st.markdown("De même que précédemment, certaines classes sont bien identifiées sur les deux jeux de données, d’autres ne sont pas reconnues, et d’autres au contraire sont sur-prédites.")
    with st.expander("Diagnostic du sur-apprentissage"):
      st.image(BASE_DIR / "images" / "ML_SGD" / "maladies_overfitting.png", width = 500)
    with st.expander("Matrice de confusion"):
      st.image(BASE_DIR / "images" / "ML_SGD" / "maladies_confusion.png", width = 500)

  with onglet4:
    st.markdown("Les résultats obtenus par le SGD Classifier sont assez satisfaisants, notamment sur le set de données HOG qui permet d’obtenir une accuracy 68% et un F1 de 63,5% sur la classification des quatorze taxons. Les scores sont un peu moins élevés en ce qui concerne la classification des trente-huit maladies. Sur ce deuxième exercice, le surapprentissage devient significatif. Si certaines classes sont très bien identifiées, il en demeure qui ne sont pas reconnues (notamment la classe apple) et d’autres qui sont sur-prédites (potato et tomato sur le jeu HOG). Les résultats ne sont pas assez bons pour que le modèle soit fiable sur des cas d’application réels. Il convient alors de chercher de meilleures performances, soit dans un autre modèle de Machine Learning, soit dans du Deep Learning. ")

######### RANDOM FOREST ####################################################
if page == pages[3]:
  st.header("Random Forest")

######### XG BOOST ####################################################
if page == pages[4]:
  st.header("XG Boost")

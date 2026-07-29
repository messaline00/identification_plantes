import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

st.title("Modèles de Machine Learning")

st.sidebar.title("Modèles de Machine Learning")
pages=["--- Objectifs et prétraitements", "📈 Régression Logistique", "⚡ SGD Classifier", "🌳 Random Forest", "🚀 XG Boost", "--- Conclusion"]
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

######### REGRESSION LOGISTIQUE ####################################################
if page == pages[1]:
  st.header("📈 Régression logistique")
  onglet2, onglet3, onglet4 = st.tabs(["Taxons", "Maladies", "Conclusion"])

  with onglet2:
    st.write("Sur les bases des taxons")
    resultats = pd.DataFrame({
      "Accuracy\nTest": [0.373, 0.534],
      "F1-macro\nTest": [0.264, 0.502],
      "F1-weighted\nTest": [0.342, 0.538]}, index=["Pixels", "HOG + classifieur linéaire équilibré"])
    st.table(resultats)
    st.markdown("Le baseline fondée sur les pixels bruts, atteint une accuracy test de 0,3730 et un F1-macro de 0,2638. Ces résultats montrent qu’un classifieur linéaire simple, appliqué directement à des images aplaties, reste limité pour discriminer correctement les taxons végétaux.")
    st.markdown("En revanche, le modèle fondé sur les descripteurs HOG et le classifieur linéaire équilibré obtient une accuracy test de 0,5340 et un F1-macro de 0,5015. Le gain observé est particulièrement important : +0,1610 en accuracy ; +0,2377 en F1-macro ; +0,1955 en F1-weighted.Ces résultats montrent que la représentation HOG capte beaucoup mieux les structures locales pertinentes de la feuille (contours, formes, gradients) que les pixels bruts seuls.")
    st.image(BASE_DIR / "images" / "ML_LR" / "taxons_scores.png", width = 500)
    with st.expander("Matrices de confusion"):
      st.markdown("**Matrice de confusion basée sur les pixels**")
      st.image(BASE_DIR / "images" / "ML_LR" / "taxons_pix_confusion.png", width = 500)
      st.markdown("**Matrice de confusion basée sur HOG + équilibrage**")
      st.image(BASE_DIR / "images" / "ML_LR" / "taxons_hog_confusion.png", width = 500)

  with onglet3:
    st.write("Sur les bases des maladies")
    st.markdown("Nous avons analysé 4 bases différentes : les images en format pixel ou HOG, et avec ou sans équilibrage des classes.")
    resultats = pd.DataFrame({
      "Accuracy\nTest": [0.343, 0.336, 0.327, 0.315],
      "F1-macro\nTest": [0.307, 0.310, 0.289, 0.288],
      "F1-weighted\nTest": [0.319, 0.321, 0.310, 0.308]}, 
      index=["Pixels no-balanced", "Pixels balanced", "HOG no-balanced", "HOG balanced"])
    st.table(resultats)
    st.subheader("Formats pixels bruts, balanced et no-balanced")
    st.markdown("L’ablation montre un effet classique du rééquilibrage des classes. La version no-balanced obtient une accuracy légèrement meilleure (0,3425 vs 0,3359), tandis que la version balanced améliore légèrement le F1-macro (0,3097 vs 0,3069) ainsi que le F1-weighted (0,3209 vs 0,3187). Ce résultat suggère que class_weight=balanced aide le modèle à mieux prendre en compte les classes minoritaires, mais que l’effet reste limité. Le principal facteur de faiblesse semble donc être moins le déséquilibre des classes que la représentation trop simple des images en pixels bruts.")
    st.image(BASE_DIR / "images" / "ML_LR" / "maladies_pix_scores.png", width = 500)
    with st.expander("Matrices de confusion"):
      st.markdown("**Matrice de confusion no-balance**")
      st.image(BASE_DIR / "images" / "ML_LR" / "maladies_pix_confusion.png", width = 500)
      st.markdown("**Matrice de confusion balanced**")
      st.image(BASE_DIR / "images" / "ML_LR" / "maladies_pix_bal.png", width = 500)
    st.subheader("Formats HOG, balanced et no-balanced")
    st.markdown("À l'issue de notre étude d'ablation, les résultats obtenus avec les descripteurs HOG se révèlent inférieurs à ceux obtenus sur les pixels bruts. L'accuracy chute d'environ 2 points (0,3425 → 0,3265 en version non équilibrée).")
    st.image(BASE_DIR / "images" / "ML_LR" / "maladies_hog_scores.png", width = 500)
    with st.expander("Matrices de confusion"):
      st.markdown("**Matrice de confusion no-balance**")
      st.image(BASE_DIR / "images" / "ML_LR" / "maladies_hog_confusion.png", width = 500)
      st.markdown("**Matrice de confusion balanced**")
      st.image(BASE_DIR / "images" / "ML_LR" / "maladies_hog_bal_confusion.png", width = 500)

  with onglet4:
    st.markdown("Cette étude d'ablation apporte la preuve formelle que l'extraction manuelle de caractéristiques (Feature Engineering) classiques comme le HOG est inadaptée au diagnostic des maladies végétales. Pour dépasser le plafond de verre des ~34% d'accuracy, il est indispensable de faire appel à des algorithmes capables de : (1) prendre en compte l'espace colorimétrique (RGB), et (2) apprendre automatiquement des filtres extracteurs de textures fines et de lésions.")

######### SGD CLASSIFIER ####################################################
if page == pages[2]:
  st.header("⚡ SGD Classifier")
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
    st.write("Sur les bases des taxons")
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
    st.write("Sur les bases des maladies")
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
  st.header("🌳 Random Forest")
  onglet1, onglet2, onglet3, onglet4 = st.tabs(["Généralités", "Taxons", "Maladies", "Conclusion"])

  with onglet1:
    st.subheader("Hyperparamètres")
    st.markdown("Une recherche d’hyperparamètres (**GridSearchCV**) avec une validation croisée en 3 plis a été utilisée afin de sélectionner la meilleure configuration du modèle. Le critère d’optimisation choisi est le F1-score weighted, permettant de prendre en compte un éventuel déséquilibre entre les classes.")
    st.markdown("Les paramètres testés sont le nombre d'arbres (n_estimators 50 et 100), la profondeur maximale des arbres (max_depth 10 et 20), et le nombre de variables utilisées à chaque séparation (max_features : sqrt). Les paramètres retenus sont :")
    st.code("""
    model = RandomForest(n_estimators = 100, 
        max_depth = 20,
        max_features = sqrt,
        class_weight='balanced',
        random_state=42)""", language = 'python')

  with onglet2:
    st.write("Sur les bases des taxons")
    resultats = pd.DataFrame({
      "Accuracy\nTrain": [0.998, 0.999],
      "Accuracy\nValidation": [0.717, 0.702],
      "Accuracy\nTest": [0.714, 0.698],
      "F1-score\nTrain": [0.998, 0.999],
      "F1-score\nValidation": [0.704, 0.681],
      "F1-score\nTest": [0.699, 0.680]}, index=["Pixels", "HOG"])
    st.table(resultats)
    st.markdown("Les résultats montrent que le modèle **Random Forest utilisant les pixels bruts** obtient de meilleures performances que celui utilisant les descripteurs HOG. Sur l’ensemble de test, l’approche par pixels atteint une **accuracy de 71,4 %** et un **F1-score weighted de 69,9 %**, contre 69,8 % d’accuracy et 68,0 % de F1-score pour les caractéristiques HOG.")
    st.markdown("On remarque également un **écart important entre les performances sur l’entraînement et celles obtenues sur la validation/test**. Les deux modèles obtiennent des scores proches de 100 % sur l’ensemble d’entraînement (accuracy et F1 autour de 0,997–0,999), alors que les performances chutent à environ 70 % sur les données non vues. Cela indique une tendance au **sur-apprentissage** (overfitting) : le modèle apprend très bien les exemples d’entraînement mais généralise moins efficacement sur de nouvelles images.")
    with st.expander("Matrices de confusion"):
      st.image(BASE_DIR / "images" / "ML_RF" / "taxons_confusion_pix.png", width = 500)
      st.image(BASE_DIR / "images" / "ML_RF" / "taxons_confusion_hog.png", width = 500)
      st.markdown("Les résultats montrent qu’avec les pixels, plusieurs classes sont mieux reconnues qu’avec les HOG, notamment blueberry (F1 = 0,74 contre 0,09 pour HOG), raspberry (0,68 contre 0,54), strawberry (0,77 contre 0,56) et pepper_bell (0,26 contre 0,49 reste toutefois faible). À l’inverse, les caractéristiques HOG obtiennent de meilleurs résultats pour certaines classes.Par exemple, grape atteint un F1-score de 0,89 avec HOG contre 0,80 avec les pixels, et maize atteint 0,93 contre 0,88. La classe blueberry est particulièrement mal reconnue avec un recall de seulement 0,05, indiquant que le modèle identifie très peu d’images de cette catégorie.")
      st.markdown("Pour les deux approches, certaines classes restent difficiles à classifier. La classe tomato, très représentée dans le jeu de test, possède un rappel élevé (0,90 avec pixels et 0,95 avec HOG) mais une précision plus faible, ce qui indique que le modèle prédit parfois cette classe à tort pour d’autres espèces. À l’inverse, la classe pepper_bell est difficilement détectée avec les pixels (recall = 0,16), probablement à cause de similarités visuelles avec d’autres classes.")

  with onglet3:
    st.write("Sur les bases des maladies")
    resultats = pd.DataFrame({
      "Accuracy\nTrain": [1.000, 0.996],
      "Accuracy\nValidation": [0.671, 0.595],
      "Accuracy\nTest": [0.674, 0.599],
      "F1-score\nTrain": [1.000, 0.996],
      "F1-score\nValidation": [0.658, 0.578],
      "F1-score\nTest": [0.661, 0.579]}, index=["Pixels", "HOG"])
    st.table(resultats)
    st.markdown("L'écart important entre les performances d'entraînement et celles observées sur validation/test met en évidence un **surapprentissage important**. Le modèle apprend très précisément les exemples d'entraînement mais présente une généralisation plus limitée sur de nouvelles images.")
    st.markdown("Les résultats montrent que la représentation basée sur les **pixels bruts obtient de meilleures performances** que la représentation HOG pour la classification des maladies végétales. Le modèle utilisant les pixels atteint une accuracy de 67,44 % sur l'ensemble de test, contre seulement 59,90 % pour le modèle utilisant les caractéristiques HOG. Le même comportement est observé avec le F1-score pondéré, où les pixels obtiennent 66,10 % contre 57,98 % pour HOG.")
    with st.expander("Matrices de confusion"):
      st.image(BASE_DIR / "images" / "ML_RF" / "maladies_confusion_pix.png", width = 500)
      st.image(BASE_DIR / "images" / "ML_RF" / "maladies_confusion_hog.png", width = 500)
      st.markdown("La classe blueberry_healthy atteint un F1-score de 0,74 avec les pixels contre 0,29 avec HOG, et apple_healthy obtient 0,62 contre 0,29.  Les performances pour la classe maize_cercospora_leaf_spot_gray_leaf_spot est meilleure avec HOG (F1 = 0,75 contre 0,68 avec les pixels) et  grape_healthy (0,77 contre 0,71) On observe également que certaines classes restent difficiles à reconnaître avec les deux méthodes. Par exemple, pepper_bell_healthy obtient un faible F1-score avec les pixels (0,33) et potato_late_blight reste également difficile (0,47 avec pixels et 0,37 avec HOG).")

  with onglet4:
    st.markdown("Les résultats obtenus avec Random Forest montrent que ce modèle permet des performances limitées. Les scores obtenus sur l’ensemble de test restent autour de 70 % pour les espèces et 67 % pour les maladies, ce qui indique que le modèle parvient à apprendre certaines caractéristiques visuelles, mais qu’il rencontre des difficultés pour distinguer des classes présentant des similitudes importantes. De plus, l’écart important entre les performances d’entraînement et celles de validation/test met en évidence un sur-apprentissage, limitant la capacité de généralisation du modèle. La comparaison entre les pixels bruts et les descripteurs HOG montre également que le choix des caractéristiques influence les résultats.  Les performances Random Forest restent insuffisantes pour une classification fiable d’images végétales.")


######### XG BOOST ####################################################
if page == pages[4]:
  st.header("🚀 XG Boost")
  onglet2, onglet3, onglet4 = st.tabs(["Taxons", "Maladies", "Conclusion"])

  with onglet2:
    st.write("Sur les bases des taxons")
    resultats = pd.DataFrame({
      "Accuracy": [0.857, 0.859],
      "F1-macro": [0.851, 0.839],
      "Ecart train/val": ['13,8 pt', '13,8 pt']}, index=["Pixels", "HOG"])
    st.table(resultats)
    st.markdown("Sur les pixels bruts (32×32, aplatis), XGBoost atteint **85,7 %** d'accuracy et un F1 macro de **0,851** sur le test, pondération des classes (sample_weight) appliquée pour compenser le déséquilibre 12×. **pepper_bell** reste la classe la plus difficile (F1 0,69), suivie d'**apple** (0,77) et **potato** (0,79) ; à l'inverse, **maize** (0,95), **grape** (0,94) et **orange** (0,93) sont les mieux reconnues. La matrice de confusion confirme une diagonale dominante partout, avec une légère tendance de confusion vers **tomato**, la classe la plus fréquente du jeu d'entraînement.")
    st.markdown("Sur les features HOG, XGBoost atteint 85,9 % d'accuracy et un F1 macro de 0,839 — accuracy quasi identique aux pixels bruts (85,7 %), mais F1 macro légèrement en retrait (0,839 contre 0,851). HOG n'est donc pas strictement meilleur : il redistribue la performance différemment selon les classes plutôt que d'améliorer uniformément. **pepper_bell** progresse nettement (F1 0,69 → 0,81) — cohérent avec HOG, qui capte la forme des feuilles plutôt que leur couleur. À l'inverse, **blueberry** (0,86 → 0,71) et **raspberry** (0,81 → 0,76) reculent sensiblement : ces baies se distinguent probablement davantage par la couleur que par la forme, un signal que HOG jette précisément en travaillant sur l\'image en niveaux de gris. La matrice de confusion confirme une diagonale dominante partout, sans confusion isolée qui domine le reste.")
    with st.expander("Courbes d'apprentissage"):
      st.markdown("**Courbe d'apprentissage sur les pixels bruts**")
      st.image(BASE_DIR / "images" / "ML_XGB" / "taxons_pix_courbes.png", width = 500)
      st.markdown("Le train atteint une accuracy quasi parfaite (**0,99**) et une loss proche de 0 (**0,09**) après **300** arbres — comportement attendu pour XGBoost, chaque arbre corrigeant mécaniquement les erreurs du précédent. La validation plafonne nettement plus bas (accuracy **0,86**, loss **0,45**) mais continue de progresser légèrement jusqu'au dernier arbre, sans jamais se stabiliser complètement ni se dégrader : pas de signe de surapprentissage brutal, seulement l'écart structurel habituel entre train et validation pour ce type de modèle sur des pixels bruts sans structure spatiale exploitée.")
      st.markdown("**Courbe d'apprentissage sur les HOG**")
      st.image(BASE_DIR / "images" / "ML_XGB" / "taxons_hog_courbes.png", width = 500)
      st.markdown("Le train atteint une accuracy quasi parfaite (99,7 %) et une loss proche de 0 (0,068) après 300 arbres. La validation plafonne à 85,9 % d'accuracy et 0,45 de loss, en légère progression continue jusqu'au dernier arbre, sans dégradation. L'écart train/validation (13,8 points) est quasiment identique à celui observé sur les pixels bruts (13,8 points également) — malgré ses 1 764 dimensions contre 64, HOG ne réduit ni n'aggrave ce schéma structurel : même comportement d'écart de généralisation, sans signe de dégradation active de la validation.")
    with st.expander("Matrices de confusion"):
      st.markdown("**Matrice de confusion sur les pixels bruts**")
      st.image(BASE_DIR / "images" / "ML_XGB" / "taxons_pix_confusion.png", width = 500)
      st.markdown("**Matrice de confusion sur les HOG**")
      st.image(BASE_DIR / "images" / "ML_XGB" / "taxons_hog_confusion.png", width = 500)
      
  with onglet3:
    st.write("Sur les bases des maladies")
    resultats = pd.DataFrame({
      "Accuracy": [0.824, 0.755],
      "F1-macro": [0.814, 0.743],
      "Ecart train/val": ['17,5 pt', '24,4 pt']}, index=["Pixels", "HOG"])
    st.table(resultats)
    st.markdown("Sur les pixels bruts (32×32, aplatis), XGBoost atteint **82,4 %** d'accuracy et un F1 macro de **0,814** sur les 38 classes, pondération appliquée pour compenser le déséquilibre. Les classes les mieux reconnues sont concentrées chez **maize** (common_rust et healthy à 0,99) et **orange___haunglongbing_citrus_greening** (0,94, la classe la plus fournie du test). À l'inverse, la faiblesse se concentre nettement sur les maladies de **tomato** — early_blight et septoria_leaf_spot (F1 ≈ 0,63), late_blight (0,67), target_spot (0,69) — ainsi que **potato___late_blight** (précision 0,58). Cette concentration des erreurs au sein d'une même espèce, plutôt qu'un éparpillement aléatoire, est cohérente avec une réelle similarité visuelle entre plusieurs maladies foliaires (taches, brûlures) que 32×32 pixels bruts peinent à distinguer. La matrice de confusion confirme une diagonale dominante partout, sans paire de confusion isolée qui domine le reste.")
    st.markdown("Sur les features HOG, XGBoost atteint 75,5 % d'accuracy et un F1 macro de 0,743 — nettement en retrait par rapport aux pixels bruts sur cette même base (82,4 % / 0,814, soit -6,9 et -7,1 points). C'est un recul bien plus marqué que celui observé sur TAXONS (F1 macro -1,2 point seulement), un signal clair que HOG pénalise MALADIES spécifiquement. L'explication la plus probable tient à la nature même de la tâche : contrairement à TAXONS, où il faut distinguer des espèces aux formes de feuilles différentes, MALADIES doit repérer des symptômes qui se manifestent presque toujours par un changement de **couleur ou de texture de surface** (jaunissement, taches, brunissement) sur une feuille dont la forme reste identique entre l'état sain et malade. HOG travaille en niveaux de gris et jette précisément ce signal. Le sous-groupe tomato, déjà le plus faible sous pixels bruts, s'effondre encore davantage : septoria_leaf_spot (0,63 → 0,42), target_spot (0,69 → 0,51), late_blight (0,67 → 0,54), leaf_mold (0,77 → 0,62). À l'inverse, les classes déjà fortes et morphologiquement bien identifiables restent solides (maize, orange___haunglongbing_citrus_greening, soybean___healthy).")
    with st.expander("Courbes d'apprentissage"):
      st.markdown("**Courbe d'apprentissage sur les pixels bruts**")
      st.image(BASE_DIR / "images" / "ML_XGB" / "maladies_pix_courbes.png", width = 500)
      st.markdown("Le train atteint un ajustement parfait (merror = 0, mlogloss ≈ 0,014) dès l'arbre environ **225 **— mémorisation complète des 67 000+ images d'entraînement, sur les 38 classes. La validation continue de progresser légèrement jusqu'au dernier arbre sans jamais se dégrader, mais plafonne à **82,5** % d'accuracy et 0,58 de loss : un écart train/validation d'environ 17,5 points, plus marqué que celui observé sur TAXONS (~13 points). Cohérent avec la granularité plus fine de la tâche (38 classes contre 14) : plus de place pour que le modèle capture des détails propres au train qui ne se généralisent pas à l'identique. Même lecture que pour TAXONS — écart de généralisation, pas de dégradation active de la validation — probablement la limite intrinsèque des pixels bruts face à un nombre de classes élevé et visuellement proches, plus qu'un problème de réglage.")
      st.markdown("**Courbe d'apprentissage sur les HOG**")
      st.image(BASE_DIR / "images" / "ML_XGB" / "maladies_hog_courbes.png", width = 500)
      st.markdown("Le train atteint un ajustement parfait (accuracy ≈ 100 %, loss ≈ 0,02) dès l'arbre ~100. La validation plafonne à 75,6 % d'accuracy et 0,81 de loss, en légère progression continue jusqu'au dernier arbre, sans dégradation — l'écart train/validation atteint 24,4 points, le plus large des quatre combinaisons testées (contre 13,8 points pour Pixels et HOG sur TAXONS, et 17,5 points pour Pixels sur MALADIES). Ce n'est pas un excès de mémorisation différent des trois autres runs — le train touche déjà 100 % partout, XGBoost a systématiquement la capacité de tout apprendre par cœur quel que soit le jeu de features. L'écart plus large ici vient du plafond de validation plus bas (75,6 % contre 82,5-85,9 % ailleurs), cohérent avec la lecture déjà posée sur la matrice de confusion : HOG retire précisément le signal couleur dont MALADIES a le plus besoin, ce qui limite ce que le modèle peut extraire, sans que ça change sa capacité à mémoriser le train.")
    with st.expander("Matrices de confusion"):
      st.markdown("**Matrice de confusion sur les pixels bruts**")
      st.image(BASE_DIR / "images" / "ML_XGB" / "maladies_pix_confusion.png", width = 500)
      st.markdown("**Matrice de confusion sur les HOG**")
      st.image(BASE_DIR / "images" / "ML_XGB" / "maladies_hog_confusion.png", width = 500)

  with onglet4:
    st.markdown("Les pixels bruts l'emportent sur les deux bases en F1 macro — de justesse sur TAXONS (-1,2 point pour HOG), nettement sur MALADIES (-7,1 points, et l'écart train/validation le plus large des quatre combinaisons). HOG encode la forme des contours à partir d'une image en niveaux de gris : il jette la couleur, information secondaire pour distinguer des espèces aux silhouettes différentes (TAXONS), mais souvent le signal principal des symptômes de maladie (jaunissement, taches, brunissement) sur une feuille dont la forme ne change pas (MALADIES). Ce projet confirme que la couleur porte plus d'information utile que la forme pour détecter des maladies.")


######### CONCLUSIONS ####################################################
if page == pages[5]:
  st.header("Conclusion sur les modèles de Machine Learning")
  st.markdown("**Accuracy sur le test par modèle**")
  st.image(BASE_DIR / "images" / "ML_SGD" / "ccl.png", width = 500)
  st.markdown("\n**Conclusion**")
  st.markdown("Même le meilleur modèle testé (XGBoost) plafonne à 85,9 % d'accuracy sur TAXONS et 82,4% sur MALADIES — loin derrière les CNN présentés dans la suite de ce rapport. Trois causesconvergent : (1) l'aplatissement en vecteur détruit la structure spatiale 2D de l'image, que ni les pixels bruts ni HOG ne peuvent restituer à un modèle qui n'a aucune notion de voisinage ; (2) HOG, en niveaux de gris, est structurellement aveugle à la couleur — précisément le signal le plus informatif pour MALADIES ; (3) les modèles à base d'arbres (Random Forest, XGBoost) mémorisent quasi parfaitement le train (jusqu'à 99,9 % d'accuracy) tout en généralisant nettement moins bien, un surapprentissage que la seule pondération de classes ne suffit pas à corriger. Ces résultats motivent le passage aux réseaux de neurones convolutifs, seuls capables d'exploiter directement la structure spatiale et colorimétrique de l'image.")
  with st.expander("Tous les scores sur les taxons"):
    st.image(BASE_DIR / "images" / "ML_SGD" / "ccl_tab_taxons.png", width = 500)
  with st.expander("Tous les scores sur les maladies"):
    st.image(BASE_DIR / "images" / "ML_SGD" / "ccl_tab_maladies.png", width = 500)
  

# Identification de plantes et détection des maladies

## Présentation

Ce projet vise à développer un système de **classification d’images végétales** capable de :

* identifier l’espèce d’une plante ;
* détecter une maladie à partir d’une photographie de feuille.

Trois approches sont comparées :

1. **Machine Learning classique** : Régression Logistique, SGD, Random Forest et XGBoost ;
2. **CNN baseline** de référence ;
3. **CNN avec transfer learning** : ResNet50, EfficientNet-B3 et DenseNet121.

Les expériences sont réalisées sur deux bases : **TAXONS** et **MALADIES**, constituées à partir d’un corpus commun de 96 165 images.

## Données et protocole

Les modèles de Machine Learning utilisent deux représentations : **pixels bruts** et **HOG** (*Histogram of Oriented Gradients*).

Les différents modèles utilisent des **splits train/validation/test communs**, construits selon un protocole anti-fuite regroupant les images et leurs quasi-doublons.

Les performances sont évaluées principalement avec l’**accuracy** et le **F1-score** sur le jeu de test.

## Résultats principaux

| Approche                           |     TAXONS |   MALADIES |
| ---------------------------------- | ---------: | ---------: |
| Machine Learning — meilleur modèle |  83,9 % F1 |  81,4 % F1 |
| CNN baseline                       |  95,6 % F1 |  95,8 % F1 |
| CNN optimisé — meilleur modèle     | 99,77 % F1 | 99,15 % F1 |

Le **CNN baseline** dépasse nettement les modèles de Machine Learning classique. Le **transfer learning** permet d’obtenir les meilleures performances, avec **ResNet50** sur TAXONS et **EfficientNet-B3** sur MALADIES.

## Organisation

Le dépôt contient les **notebooks d’expérimentation** correspondant aux différents modèles, ainsi que les éléments nécessaires à la démonstration de l’application.

Les notebooks présentent le prétraitement, l’entraînement, l’évaluation et l’analyse des résultats de chaque approche.

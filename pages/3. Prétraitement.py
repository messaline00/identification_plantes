import pandas as pd
import streamlit as st

import streamlit as st
import pandas as pd
from pathlib import Path
import pandas as pd
import plotly.express as px

from theme import (
    inject_css,
    chapter_banner,
    info_box,
    warning_box,
    success_box,
    kpi_row,
    white_card,
)


inject_css()

chapter_banner(
    "03",
    "Prétraitement des données",
    "")


st.markdown("""
Avant l'entraînement, les données ont été préparées afin de garantir une
évaluation fiable des modèles et d'éviter les fuites de données.
""")

st.markdown("""
<style>
.pipeline-table{
    width:100%;
    border-collapse:collapse;
    font-size:15px;
    border-radius:12px;
    overflow:hidden;
    box-shadow:0 2px 8px rgba(0,0,0,.08);
}

.pipeline-table th{
    background:#2C7A7B;
    color:white;
    padding:12px;
    text-align:center;
}

.pipeline-table td{
    padding:12px;
    border-bottom:1px solid #e8e8e8;
    vertical-align:middle;
}

.pipeline-table tr:nth-child(even){
    background:#f8f9fa;
}

.pipeline-table td:nth-child(1){
    font-weight:600;
    width:22%;
}

.pipeline-table td:nth-child(3){
    text-align:center;
    font-weight:600;
}

.train{
    color:#0b8a42;
    font-weight:700;
}

.all{
    color:#1f4db8;
    font-weight:700;
}
</style>

<table class="pipeline-table">
<tr>
    <th>Étape</th>
    <th>Méthode</th>
    <th>Application</th>
    <th>Objectif</th>
</tr>

<tr>
    <td>Séparation</td>
    <td><b>GroupShuffleSplit + pHash</b> </td>
    <td class="all">Train • Val • Test</td>
    <td>Éviter les fuites de données</td>
</tr>

<tr>
    <td>Équilibrage</td>
    <td>Class weights</td>
    <td class="train">Train uniquement</td>
    <td>Compenser le déséquilibre</td>
</tr>

<tr>
    <td>Augmentation</td>
    <td>Rotations • Flips • Luminosité</td>
    <td class="train">Train uniquement</td>
    <td>Limiter le surapprentissage</td>
</tr>

<tr>
    <td>Normalisation</td>
    <td>Pixels dans [0 ; 1]</td>
    <td class="all">Tous les jeux</td>
    <td>Stabiliser l'apprentissage</td>
</tr>



</table>
""", unsafe_allow_html=True)


st.markdown("""
#### Focus — Séparation avec GroupShuffleSplit

Les images ont été regroupées en **familles de clones** grâce au
**pHash (Perceptual Hash)**. Les images visuellement très proches sont
conservées dans le même sous-ensemble (**Train**, **Validation** ou **Test**),
ce qui évite toute **fuite de données** et garantit une évaluation fiable des modèles.
""")

with st.expander("Voir un exemple de famille de clones (pHash)"):
    st.image(
        "images/Prétraitement/PHash.png",
        caption="Exemple de famille de clones identifiée par pHash",
        use_container_width=True,
    )

st.divider()

st.markdown("""
#### Bilan 
""")
kpi_row(
    [
        {
            "value": "70 %",
            "label": "ENTRAÎNEMENT",
            "sub": "67 377 images",
        },
        {
            "value": "15 %",
            "label": "VALIDATION",
            "sub": "14 370 images",
        },
        {
            "value": "15 %",
            "label": "TEST",
            "sub": "14 418 images",
        },
    ]
)

success_box(
    "<div style='line-height:1.8;'>"
    "<b>✓ Vérifications effectuées</b><br><br>"
    "✅ Splits stratifiés anti-fuite<br>"
    "✅ Les class weights et l'augmentation sont effectués uniquement sur le jeu d'entraînement<br>"
    "✅ Normalisation appliquée à l'ensemble des données<br><br>"
    "</div>"
    "<b>Les deux bases sont prêtes pour la modélisation </b>"
    "</div>"
)
import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from theme import inject_css, chapter_banner, hypo_row, kpi_row
import data_content as d

inject_css()
chapter_banner(
    "01",
    "Introduction",
    "")


st.markdown(
    """
    <div style="text-align: justify;">
    Les pertes agricoles dues aux maladies des plantes représentent entre <b>20 % et 40 %</b>
    de la production annuelle. Dans ce contexte, disposer d'un outil capable d'identifier
    rapidement une espèce et de détecter une maladie à partir d'une simple photographie
    constitue une aide potentielle au diagnostic précoce.
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("") 

st.markdown(
    """
    <div style="text-align: justify;">
    Le projet s'articule autour de la problématique suivante : à partir d'une <b>unique photographie
    d'une feuille</b>, est-il possible d'identifier automatiquement l'espèce d'une plante et de
    détecter la présence d'une maladie foliaire avec une fiabilité suffisante pour assister un
    utilisateur non spécialiste ?
    <br><br>
    <b>Périmètre de l'étude :</b> seuls les <b>symptômes visibles sur les feuilles</b> sont pris
    en compte.
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Hypothèses de travail")
hypo_row([
    {"title": f"{h['id']} · {h['titre']}", "body": h["enonce"]} for h in d.HYPOTHESES
])

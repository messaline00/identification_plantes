import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from theme import inject_css, TEAL, INDIGO, DARK
import data_content as d

inject_css()

st.markdown("<div style='height: 4vh'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown(
        f"<p style='text-align:center; color:{TEAL}; font-weight:700; "
        f"letter-spacing:0.15em; font-size:0.85rem;'>PROJET FIL ROUGE — SOUTENANCE</p>",
        unsafe_allow_html=True,
    )
    
    st.markdown(
    f"""
    <h1 style="
        color:{INDIGO};
        font-size:2.2rem;
        text-align:center;
        line-height:1.35;
        font-weight:700;
    ">
    Identification des plantes et détection des maladies foliaires<br>
    par apprentissage automatique et réseaux de neurones convolutifs
    </h1>
    """,
    unsafe_allow_html=True,)
    
    st.markdown(
        f"<p style='text-align:center; color:{TEAL}; font-style:italic; font-size:1.1rem;'>"
        f"Machine Learning · CNN baseline · CNN optimisés (transfer learning)</p>",
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height: 3vh'></div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style='background-color:{INDIGO}; border-radius:10px; padding:1.3rem 1.6rem;'>
        <p style='color:white; font-size:1.05rem; margin:0;'>
        À partir d'une <b>seule photo de feuille</b>, peut-on identifier automatiquement
        l'espèce d'une plante et détecter la présence d'une maladie, avec une fiabilité
        suffisante pour aider un utilisateur non expert ?
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height: 3vh'></div>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='text-align:center; color:{DARK};'><b>{d.TEAM}</b></p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align:center; color:{TEAL};'>"
        f"{d.CORPUS_FINAL:,} images · {d.TAXONS_N_CLASSES} taxons · {d.MALADIES_N_CLASSES} classes de maladies</p>"
        .replace(",", " "),
        unsafe_allow_html=True,
    )

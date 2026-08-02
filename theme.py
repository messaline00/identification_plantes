import streamlit as st

INDIGO = "#48496A"
TEAL = "#2AA99C"
LIGHT_TEAL = "#48C2B7"
PALE_TEAL = "#A7D9D2"
GREY = "#8A8794"
DARK = "#2B2740"
LAVENDER_FILL = "#DCDAE8"
GREEN = "#1E7A4F"
RED = "#B23B32"
AMBER = "#9A6916"
WHITE = "#FFFFFF"


def inject_css():
    st.markdown(
        f"""
        <style>
        .stApp {{ background-color: {WHITE}; }}
        h1, h2, h3 {{ color: {DARK}; font-family: Arial, sans-serif; }}
        p, li, span, div {{ font-family: Arial, sans-serif; }}

        .chapter-banner {{
            background-color: {INDIGO};
            border-radius: 10px;
            padding: 1.1rem 1.5rem;
            margin-bottom: 1.3rem;
        }}
        .chapter-banner .num {{
            color: {TEAL};
            font-weight: 700;
            font-size: 1.6rem;
        }}
        .chapter-banner .title {{
            color: {WHITE};
            font-weight: 700;
            font-size: 1.5rem;
            margin: 0;
        }}
        .chapter-banner .subtitle {{
            color: {LAVENDER_FILL};
            font-style: italic;
            font-size: 0.95rem;
        }}

        .kpi-card {{
            background-color: {INDIGO};
            border-radius: 10px;
            padding: 0.9rem 0.6rem;
            text-align: center;
        }}
        .kpi-card .value {{ color: {TEAL}; font-weight: 700; font-size: 1.7rem; }}
        .kpi-card .label {{ color: {WHITE}; font-weight: 700; font-size: 0.72rem; letter-spacing: 0.05em; }}
        .kpi-card .sub {{ color: {LAVENDER_FILL}; font-style: italic; font-size: 0.72rem; }}

        .hypo-card {{
            background-color: {INDIGO};
            border-radius: 10px;
            padding: 1rem 1.1rem;
            height: 100%;
        }}
        .hypo-card .h-title {{ color: {LIGHT_TEAL}; font-weight: 700; font-size: 1.05rem; margin-bottom: 0.4rem; }}
        .hypo-card .h-body {{ color: {WHITE}; font-size: 0.92rem; }}

        .verdict-confirmee {{ color: {GREEN}; font-weight: 700; }}
        .verdict-partielle {{ color: {AMBER}; font-weight: 700; }}
        .verdict-non {{ color: {RED}; font-weight: 700; }}

        .conclusion-box {{
            background-color: {LAVENDER_FILL};
            border-left: 6px solid {TEAL};
            border-radius: 6px;
            padding: 1rem 1.3rem;
            color: {DARK};
        }}
        .conclusion-box .c-title {{
            color: {TEAL}; font-weight: 700; text-transform: uppercase;
            font-size: 0.85rem; letter-spacing: 0.05em; margin-bottom: 0.5rem;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def chapter_banner(num, title, subtitle):
    st.markdown(
        f"""
        <div class="chapter-banner">
            <span class="num">{num}</span>
            <p class="title">{title}</p>
            <p class="subtitle">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def kpi_row(items):
    cols = st.columns(len(items))
    for col, item in zip(cols, items):
        with col:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="value">{item['value']}</div>
                    <div class="label">{item['label']}</div>
                    <div class="sub">{item.get('sub', '')}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def hypo_row(items):
    cols = st.columns(len(items))
    for col, item in zip(cols, items):
        with col:
            st.markdown(
                f"""
                <div class="hypo-card">
                    <div class="h-title">{item['title']}</div>
                    <div class="h-body">{item['body']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def conclusion_box(title, body_html):
    st.markdown(
        f"""
        <div class="conclusion-box">
            <div class="c-title">{title}</div>
            {body_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def team_card(prenom, nom, photo_b64=None):
    if photo_b64:
        avatar = (
            f"<img src='data:image/jpeg;base64,{photo_b64}' "
            f"style='width:140px; height:140px; border-radius:50%; object-fit:cover; "
            f"border:3px solid {TEAL};' />"
        )
    else:
        initiales = (prenom[:1] + nom[:1]).upper()
        avatar = (
            f"<div style='width:140px; height:140px; border-radius:50%; background:{LAVENDER_FILL}; "
            f"border:3px dashed {GREY}; display:flex; align-items:center; justify-content:center; "
            f"font-size:2.2rem; font-weight:700; color:{GREY};'>{initiales}</div>"
        )
    st.markdown(
        f"""
        <div style='text-align:center;'>
            {avatar}
            <p style='color:{DARK}; font-weight:700; margin:0.7rem 0 0; font-size:1.05rem;'>{prenom}</p>
            <p style='color:{TEAL}; margin:0; font-size:0.95rem;'>{nom}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


PLOTLY_LAYOUT = dict(
    font=dict(family="Arial", color=DARK),
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=10, r=10, t=50, b=10),
)

# =====================================================
# BOXES PERSONNALISÉES
# =====================================================

def info_box(text):
    st.markdown(
        f"""
        <div style="
            background-color:{WHITE};
            border-left:6px solid {TEAL};
            border-radius:10px;
            padding:1rem 1.2rem;
            margin:1rem 0;
            color:{DARK};
            line-height:1.6;
        ">
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


def warning_box(text):
    st.markdown(
        f"""
        <div style="
            background-color:{WHITE};
            border-left:6px solid {RED};
            border-radius:10px;
            padding:1rem 1.2rem;
            margin:1rem 0;
            color:{DARK};
            line-height:1.6;
        ">
            <span style="
                color:{RED};
                font-weight:700;
            ">
                ⚠
            </span>
            &nbsp;
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


def success_box(text):
    st.markdown(
        f"""
        <div style="
            background-color:{WHITE};
            border-left:6px solid {TEAL};
            border-radius:10px;
            padding:1rem 1.2rem;
            margin:1rem 0;
            color:{DARK};
            line-height:1.6;
        ">
            <span style="
                color:{GREEN};
                font-weight:700;
            ">
            </span>
            &nbsp;
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )

def white_card(text):
    st.markdown(
        f"""
        <div style="
            background-color:{WHITE};
            border:1px solid #E5E5E5;
            border-radius:10px;
            padding:1.2rem;
            margin-top:0.5rem;
            color:{DARK};
            line-height:1.6;
        ">
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )

def solutions_box(text):
    st.markdown(
        f"""
        <div style="
            background-color:{INDIGO};
            border-left:6px solid {INDIGO};
            border-radius:10px;
            padding:1rem 1.2rem;
            margin:1rem 0;
            color:{WHITE};
            line-height:1.6;
        ">
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )
hypo_row(
    [
        {
            "title": "Test H1",
            "body": "Texte simple"
        },
        {
            "title": "Test H2",
            "body": "Texte simple"
        },
    ]
)

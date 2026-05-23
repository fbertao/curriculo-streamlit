import streamlit as st

# CONFIGURAÇÃO DA PÁGINA

st.set_page_config(
    page_title="Fernanda Bertão",
    page_icon="🎲",
    layout="wide"
)

# CSS CUSTOMIZADO

st.markdown("""
<style>

/* ESCONDE SIDEBAR */

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

/* LAYOUT */

[data-testid="stAppViewContainer"] {
    background: white !important;
}

.block-container {
    padding-top: 2rem;
    padding-left: 6rem;
    padding-right: 6rem;
    max-width: 1200px;
}

/* HERO */

.hero-container {

    background:
    radial-gradient(
        circle at top left,
        rgba(236,112,0,0.12),
        transparent 35%
    ),
    radial-gradient(
        circle at top right,
        rgba(0,59,92,0.08),
        transparent 35%
    ),
    white;

    border: 1px solid #E5E7EB;
    border-radius: 32px;

    padding: 90px 60px;

    text-align: center;

    margin-top: 2rem;

    box-shadow:
    0 10px 40px rgba(0,0,0,0.04);
}

.hero-name {
    font-size: 72px;
    font-weight: 800;
    color: #003B5C;
    margin-bottom: 14px;
}

.hero-subtitle {
    font-size: 28px;
    color: #374151;
    margin-bottom: 10px;
}

.hero-company {
    font-size: 18px;
    color: #6B7280;
    margin-bottom: 20px;
}

.hero-keywords {
    font-size: 18px;
    font-weight: 600;
    color: #EC7000;
    margin-bottom: 40px;
}

/* BOTÕES */

.stButton > button,
.stLinkButton > a,
[data-testid="stPageLink-NavLink"] {

    background: white !important;
    color: #111827 !important;

    border: 1px solid #E5E7EB !important;
    border-radius: 18px !important;

    min-height: 55px;

    font-weight: 600 !important;

    box-shadow:
    0 4px 12px rgba(0,0,0,0.04);

    transition: all 0.2s ease;
}

/* TEXTO DOS PAGE LINKS */

[data-testid="stPageLink-NavLink"] p {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* HOVER */

.stButton > button:hover,
.stLinkButton > a:hover,
[data-testid="stPageLink-NavLink"]:hover {

    border: 1px solid #EC7000 !important;
    color: #EC7000 !important;

    transform: translateY(-2px);
}

/* MOBILE */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .hero-container {
        padding: 45px 22px;
        border-radius: 24px;
    }

    .hero-name {
        font-size: 38px;
        line-height: 1.05;
    }

    .hero-subtitle {
        font-size: 18px;
    }

    .hero-company {
        font-size: 14px;
    }

    .hero-keywords {
        font-size: 14px;
        line-height: 1.7;
    }
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HERO
# ==================================================

st.markdown("""
<div class='hero-container'>

<div class='hero-name'>
Fernanda Bertão
</div>

<div class='hero-subtitle'>
Estudante de Ciência e Tecnologia
</div>

<div class='hero-company'>
UFABC • Itaú • Dados
</div>

<div class='hero-keywords'>
Data Analytics | Machine Learning | SQL | Python | AWS
</div>

</div>
""", unsafe_allow_html=True)

# divisória 


st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/1_exp_itau.py",
        label="💼 Ver Experiência Itaú",
        use_container_width=True
    )

with col2:
    st.page_link(
        "pages/2_exp_academicas.py",
        label="🔬 Projetos Acadêmicos",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# links

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button(
        "🔗 LinkedIn",
        "https://www.linkedin.com/in/fbertao/",
        use_container_width=True
    )

with col2:
    st.link_button(
        "💻 GitHub",
        "https://github.com/fbertao",
        use_container_width=True
    )

with col3:
    st.link_button(
        "📄 Download CV",
        "https://drive.google.com/file/d/1Sc7kObUhBdNrLJ-e5J9XKNk1Zdn2hiHA/view?usp=sharing",
        use_container_width=True
    )
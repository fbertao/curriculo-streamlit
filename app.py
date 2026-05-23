import streamlit as st

# config da página

st.set_page_config(
    page_title="Fernanda Bertão",
    page_icon="🎲",
    layout="wide"
)

# CSS 

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


# hero

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
    if st.button(
        "💼 Ver Experiência Itaú",
        use_container_width=True
    ):
        st.switch_page("exp_itau")

with col2:
    if st.button(
        "🔬 Projetos Acadêmicos",
        use_container_width=True
    ):
        st.switch_page("exp_academicas")

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

# skills

st.markdown(
    "<div style='height:50px'></div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
text-align:center;
font-size:20px;
font-weight:700;
color:#003B5C;
margin-bottom:20px;
">
Skills
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
display:flex;
justify-content:center;
flex-wrap:wrap;
gap:12px;
">

<div style="
padding:10px 18px;
border-radius:999px;
background:#EFF6FF;
border:1px solid #D9E7FF;
font-weight:600;
color:#003B5C;
">
SQL • Intermediário
</div>

<div style="
padding:10px 18px;
border-radius:999px;
background:#EFF6FF;
border:1px solid #D9E7FF;
font-weight:600;
color:#003B5C;
">
Python • Intermediário
</div>

<div style="
padding:10px 18px;
border-radius:999px;
background:#FFF4EB;
border:1px solid #FFE2C5;
font-weight:600;
color:#EC7000;
">
AWS • Básico
</div>

<div style="
padding:10px 18px;
border-radius:999px;
background:#FFF4EB;
border:1px solid #FFE2C5;
font-weight:600;
color:#EC7000;
">
Machine Learning • Básico
</div>

</div>
""", unsafe_allow_html=True)
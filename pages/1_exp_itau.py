import streamlit as st

# config

st.set_page_config(
    page_title="Experiência — Itaú",
    page_icon="💼",
    layout="wide"
)

# css
st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

/* 
   FUNDO / CONTAINER
 */

[data-testid="stAppViewContainer"] {
    background: #FFFFFF !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    padding-left: 5rem;
    padding-right: 5rem;
    max-width: 1200px;
}

/*
   TIPOGRAFIA
  */

.page-title {
    font-size: 42px;
    font-weight: 800;
    color: #003B5C !important;
    margin-bottom: 8px;
    line-height: 1.15;
}

.page-subtitle {
    font-size: 17px;
    color: #4B5563 !important;
    line-height: 1.7;
    max-width: 900px;
}

.section-title {
    font-size: 27px;
    font-weight: 750;
    color: #003B5C !important;
    margin-top: 42px;
    margin-bottom: 20px;
}

/*
   BOTÃO VOLTAR
*/

.stButton > button {
    background: white !important;
    color: #003B5C !important;

    border: 1px solid #E5E7EB !important;
    border-radius: 12px !important;

    min-height: 42px;
    padding: 0 20px;

    font-weight: 600 !important;

    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #EC7000 !important;
    color: #EC7000 !important;
}

/*
   HEADER CARD
*/

.experience-header {
    margin-top: 22px;

    padding: 30px 34px;

    border: 1px solid #E5E7EB;
    border-radius: 22px;

    background: linear-gradient(
        135deg,
        #FFF9F4 0%,
        #FFFFFF 48%,
        #F7FAFC 100%
    );

    box-shadow:
        0 8px 24px rgba(0, 0, 0, 0.04);
}

/*
   ITAÚ CARD
  */

.company-card {
    display: flex;
    align-items: center;
    gap: 22px;

    padding: 24px 26px;

    border: 1px solid #E5E7EB;
    border-radius: 18px;

    background: white;

    box-shadow:
        0 5px 16px rgba(0, 0, 0, 0.035);

    margin-bottom: 25px;
}

.itau-logo {
    width: 68px;
    height: 68px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #EC7000;
    color: white !important;

    border-radius: 15px;

    font-size: 21px;
    font-weight: 800;
}

.company-role {
    font-size: 20px;
    font-weight: 750;
    color: #003B5C !important;
    margin-bottom: 4px;
}

.company-name {
    font-size: 15px;
    font-weight: 600;
    color: #EC7000 !important;
}

.company-date {
    font-size: 14px;
    color: #6B7280 !important;
    margin-top: 8px;
}

/* 
   PROJECT CARDS
*/

.project-card {
    border: 1px solid #E5E7EB;
    border-radius: 18px;

    padding: 24px 26px;

    background: white;

    box-shadow:
        0 5px 16px rgba(0, 0, 0, 0.035);

    height: 100%;

    transition: all 0.2s ease;
}

.project-card:hover {
    border-color: #D5DDE3;

    box-shadow:
        0 8px 22px rgba(0, 0, 0, 0.07);

    transform: translateY(-2px);
}

.project-title {
    font-size: 19px;
    font-weight: 750;
    color: #003B5C !important;
    margin-bottom: 7px;
}

.project-description {
    font-size: 14px;
    color: #4B5563 !important;
    line-height: 1.6;
    margin-top: 12px;
}

/*
   TECH TAGS
  */

.tech-tag {
    display: inline-block;

    background: #F1F6FA;

    color: #003B5C !important;

    border: 1px solid #DCE8F0;

    padding: 5px 10px;

    border-radius: 20px;

    font-size: 12px;
    font-weight: 600;

    margin-right: 5px;
    margin-bottom: 5px;
}

/*
   IMPACT CARD
*/

.impact-card {
    margin-top: 30px;

    padding: 24px 28px;

    border-left: 4px solid #EC7000;

    border-top: 1px solid #E5E7EB;
    border-right: 1px solid #E5E7EB;
    border-bottom: 1px solid #E5E7EB;

    border-radius: 14px;

    background: #FFFDFB;
}

.impact-title {
    color: #003B5C !important;
    font-size: 18px;
    font-weight: 750;
    margin-bottom: 8px;
}

.impact-text {
    color: #4B5563 !important;
    font-size: 14px;
    line-height: 1.6;
}

/*
   EXPANDERS
 */

div[data-testid="stExpander"] {
    border: 1px solid #E5E7EB !important;
    border-radius: 15px !important;

    margin-bottom: 12px;

    box-shadow:
        0 3px 12px rgba(0,0,0,0.025);

    overflow: hidden;
}

div[data-testid="stExpander"]:hover {
    border-color: #D5DDE3 !important;
}

.streamlit-expanderHeader {
    color: #003B5C !important;
    font-size: 15px !important;
    font-weight: 650 !important;
}

/*
   MOBILE
*/

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
    }

    .page-title {
        font-size: 32px;
    }

    .page-subtitle {
        font-size: 15px;
    }

    .experience-header {
        padding: 22px;
    }

    .company-card {
        padding: 20px;
    }

    .section-title {
        font-size: 23px;
    }

    .project-card {
        margin-bottom: 15px;
    }
}

</style>
""", unsafe_allow_html=True)


# VOLTAR

if st.button("← Voltar para Home"):
    st.switch_page("app.py")

# HEADER

st.markdown("""
<div class="experience-header">

    <div class="page-title">
        💼 Experiência — Itaú
    </div>

    <div class="page-subtitle">
        Estagiária na comunidade Plataforma e Jornadas de Daily Baking,
        atuando no desenvolvimento e monitoramento de indicadores-chave,
        análise de volumetria e identificação de desafios em projetos
        de modernização da plataforma de débitos automáticos.
    </div>

    <br>

    <span class="tech-tag">Athena / SQL</span>
    <span class="tech-tag">S3</span>
    <span class="tech-tag">QuickSight</span>
    <span class="tech-tag">SageMaker</span>
    <span class="tech-tag">Python</span>
    <span class="tech-tag">Pacote Office</span>

</div>
""", unsafe_allow_html=True)

# EXPERIÊNCIA

st.markdown(
    '<div class="section-title">🏢 Experiência profissional</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="company-card">

    <div class="itau-logo">
        itaú
    </div>

    <div>
        <div class="company-role">
            Estagiária de Dados
        </div>

        <div class="company-name">
            Itaú Unibanco
        </div>

        <div class="company-date">
            📅 Experiência atual
        </div>
    </div>

</div>
""", unsafe_allow_html=True)


# PROJETOS EM DESTAQUE

st.markdown(
    '<div class="section-title">🚀 Projetos em destaque</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

# HUB

with col1:

    st.markdown("""
    <div class="project-card">

        <div class="project-title">
            📊 HUB de Ocorrências
        </div>

        <span class="tech-tag">Python</span>
        <span class="tech-tag">SQL</span>
        <span class="tech-tag">Streamlit</span>
        <span class="tech-tag">Pandas</span>

        <div class="project-description">

            Dashboard analítico desenvolvido em conjunto com
            times de dados para acompanhamento de reclamações
            e identificação de oportunidades na visão cliente.

        </div>

    </div>
    """, unsafe_allow_html=True)

# GOVERNANÇA

with col2:

    st.markdown("""
    <div class="project-card">

        <div class="project-title">
            🗂️ Governança de Dados
        </div>

        <span class="tech-tag">SQL</span>
        <span class="tech-tag">Data Quality</span>
        <span class="tech-tag">Governança</span>

        <div class="project-description">

            Atualização da documentação de bases críticas,
            incluindo mapeamento de atributos, regras,
            tipos de dados e De x Para de campos.

        </div>

    </div>
    """, unsafe_allow_html=True)


st.write("")


col3, col4 = st.columns(2, gap="large")


# REJEIÇÕES

with col3:

    st.markdown("""
    <div class="project-card">

        <div class="project-title">
            📈 Análise de Rejeições de Débitos
        </div>

        <span class="tech-tag">Python</span>
        <span class="tech-tag">Pandas</span>
        <span class="tech-tag">Análise Exploratória</span>

        <div class="project-description">

            Projeto analítico para identificação dos principais
            ofensores de rejeições de débitos e levantamento
            de oportunidades de melhoria operacional.

        </div>

    </div>
    """, unsafe_allow_html=True)

# IA

with col4:

    st.markdown("""
    <div class="project-card">

        <div class="project-title">
            🤖 Agente de IA para Documentação
        </div>

        <span class="tech-tag">IA</span>
        <span class="tech-tag">Documentação</span>
        <span class="tech-tag">Knowledge Base</span>

        <div class="project-description">

            Participação no desenvolvimento de um agente de IA
            voltado à centralização e consulta de documentações
            técnicas e operacionais.

        </div>

    </div>
    """, unsafe_allow_html=True)


# OUTRAS ATUAÇÕES

st.markdown(
    '<div class="section-title">⚙️ Outras atuações</div>',
    unsafe_allow_html=True
)


with st.expander("Modernização da Plataforma de Débitos"):

    st.markdown("""
    **Responsabilidades**

    - Levantamento de dados volumétricos
    - Validação de cenários operacionais
    - Acompanhamento do ciclo de vida dos débitos
    - Monitoramento de indicadores da modernização
    """)


with st.expander("Painel de Modernização — Nova Efetivação"):

    st.markdown("""
    **Principais entregas**

    - Consolidação das principais visões de indicadores
    - Atualização horária
    - Acompanhamento da evolução da modernização
    """)


with st.expander("Modelo de Machine Learning para Classificação"):

    st.markdown("""
    **Projeto em desenvolvimento**

    Projeto voltado à aplicação de Machine Learning para
    classificação de reclamações relacionadas a débitos automáticos.

    **Abordagem**

    - Clusterização de reclamações
    - Modelagem supervisionada
    - Classificação binária
    - Regressão logística
    """)

# IMPACTO

st.markdown("""
<div class="impact-card">

    <div class="impact-title">
        💡 O que essa experiência me proporcionou
    </div>

    <div class="impact-text">

        Experiência prática com análise de dados, construção e
        acompanhamento de indicadores, documentação de bases,
        identificação de insights e aplicação de tecnologias
        de dados em um ambiente corporativo.

    </div>

</div>
""", unsafe_allow_html=True)
import streamlit as st

# config da página

st.set_page_config(
    page_title="Experiência Itaú",
    page_icon="💼",
    layout="wide"
)
# CSS

st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

/* fundo */

[data-testid="stAppViewContainer"] {
    background: white !important;
}

.block-container {
    padding-top: 2rem;
    padding-left: 6rem;
    padding-right: 6rem;
    max-width: 1200px;
}

/* header */

.page-title {
    font-size: 52px;
    font-weight: 800;
    color: #003B5C;
    margin-bottom: 12px;
}

.page-subtitle {
    font-size: 18px;
    color: #6B7280;
    margin-bottom: 40px;
}

/* expanders */

div[data-testid="stExpander"] {
    border: 1px solid #E5E7EB !important;
    border-radius: 22px !important;

    box-shadow:
    0 6px 18px rgba(0,0,0,0.04);

    margin-bottom: 18px;

    overflow: hidden;
}

div[data-testid="stExpander"]:hover {
    border: 1px solid #EC7000 !important;
}

.streamlit-expanderHeader {
    color: #111827 !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* texto */

p, li, span, label, div {
    color: #111827 !important;
}

/* techs */

code {
    background: #EFF6FF !important;
    color: #003B5C !important;

    padding: 4px 10px !important;
    border-radius: 8px !important;

    font-size: 13px !important;
    font-weight: 600 !important;
}

/* botões */

.stButton > button {

    background: white !important;
    color: #111827 !important;

    border: 1px solid #E5E7EB !important;
    border-radius: 16px !important;

    min-height: 50px;
    font-weight: 600 !important;
}

/* mobile */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .page-title {
        font-size: 34px;
    }

    .page-subtitle {
        font-size: 15px;
    }

    .streamlit-expanderHeader {
        font-size: 15px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# header

st.markdown(
    "<div style='height:40px'></div>",
    unsafe_allow_html=True
)

st.page_link(
    "app.py",
    label="← Voltar para Home"
)

st.markdown("""
<div class='page-title'>
💼 Experiência — Itaú
</div>

<div class='page-subtitle'>
Estagiária na comunidade Plataforma e Jornadas de Daily Baking,
atuando no desenvolvimento e monitoramento de indicadores-chave,
análise de volumetria e identificação de desafios em projetos de
modernização da plataforma de débitos automáticos.
<br><br>
Experiências com:
<b>Athena (SQL)</b>,
<b>S3</b>,
<b>QuickSight</b>,
<b>SageMaker (Python)</b>,
<b>Pacote Office</b>
</div>
""", unsafe_allow_html=True)

# projetos

with st.expander("📊 HUB de Ocorrências"):

    st.markdown("""
**Dashboard analítico desenvolvido em conjunto com times de dados
para acompanhamento de reclamações e identificação de oportunidades
na visão cliente.**

### Objetivos
- Acompanhamento constante das reclamações
- Identificação de oportunidades de melhoria
- Eficiência na rotina de extração e divulgação
""")

with st.expander("🗂️ Governança de Dados"):

    st.markdown("""
**Atualização da documentação de bases críticas utilizadas pelo time.**

### Atividades
- Mapeamento de atributos e campos
- Levantamento de regras e tipos de dados
- Atualização de documentação técnica
- Atualização de De x Para de campos

### Impacto
Maior rastreabilidade, entendimento e confiabilidade
das bases utilizadas nas análises.
""")

with st.expander("📈 Análise de Rejeições de Débitos"):

    st.markdown("""
**Projeto analítico para identificação dos principais ofensores
de rejeições de débitos e oportunidades de melhoria operacional.**

### Entregas
- Identificação dos principais motivos de rejeição
- Levantamento dos produtos com maior incidência
- Geração de insights para áreas parceiras
""")

with st.expander("🤖 Agente de IA para Documentação Técnica"):

    st.markdown("""
**Participação no desenvolvimento de um agente de IA voltado à
centralização e consulta de documentações técnicas e operacionais.**

### Contribuições
- Alimentação da base de conhecimento
- Organização de documentação técnica
- Apoio ao treinamento do agente
- Estruturação de informações para acesso rápido
""")

with st.expander("⚙️ Modernização da Plataforma de Débitos"):

    st.markdown("""
### Responsabilidades
- Levantamento de dados volumétricos
- Validação de cenários operacionais
- Acompanhamento do ciclo de vida dos débitos
- Monitoramento de indicadores da modernização
""")

with st.expander("⚙️ Painel de Modernização — Nova Efetivação"):

    st.markdown("""
### Benefícios
- Principais visões de indicadores consolidados
- Atualização horária
- Acompanhamento da evolução da modernização
""")

with st.expander("🧠 Modelo de Machine Learning para Classificação"):

    st.markdown("""
**Projeto em desenvolvimento para clusterização e classificação
de reclamações de débitos automáticos.**

### Abordagem
- Clusterização de reclamações
- Modelagem supervisionada
- Classificação binária
- Regressão logística
""")
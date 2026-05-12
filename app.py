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

/* ===== FUNDO GERAL ===== */

[data-testid="stAppViewContainer"] {
    background: white !important;
}

.main {
    background: white !important;
}

[data-testid="stHeader"] {
    background: white !important;
}

.block-container {
    background: white !important;
    padding-top: 2rem;
    padding-left: 8rem;
    padding-right: 8rem;
}

/* ===== SIDEBAR ===== */

section[data-testid="stSidebar"] {
    background: #F8F9FB !important;
}

/* ===== TEXTO ===== */

html, body {
    background: white !important;
    color: black !important;
    font-family: Arial, sans-serif;
}

p, span, label, li, div {
    color: black !important;
}

/* ===== TÍTULOS ===== */

h1 {
    color: #003B5C !important;
    font-size: 56px !important;
    font-weight: 700 !important;
    margin-bottom: 0;
}

h2 {
    color: #003B5C !important;
}

h3 {
    color: black !important;
}

/* ===== HEADER ===== */

.hero-box {
    background: #F8F9FB;
    border: 1px solid #E5E7EB;
    border-left: 8px solid #EC7000;
    border-radius: 22px;
    padding: 35px;
    margin-bottom: 30px;
}

.subtitle {
    color: #475569 !important;
    font-size: 20px;
}

/* ===== BOTÕES ===== */

.stLinkButton > a {
    background: white !important;
    border: 1px solid #E5E7EB !important;
    border-radius: 14px !important;
    color: black !important;
    font-weight: 600 !important;
}

.stLinkButton > a:hover {
    border: 1px solid #EC7000 !important;
    color: #EC7000 !important;
}

/* ===== EXPANDERS ===== */

.streamlit-expanderHeader {
    color: black !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

div[data-testid="stExpander"] {
    background: white !important;
    border: 1px solid #D9D9D9 !important;
    border-radius: 18px !important;
    margin-bottom: 14px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
}

div[data-testid="stExpander"]:hover {
    border: 1px solid #EC7000 !important;
}

[data-testid="stExpanderDetails"] {
    background: white !important;
    color: black !important;
}

/* ===== METRICS ===== */

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
}

/* ===== DIVIDER ===== */

hr {
    border: none;
    border-top: 1px solid #E5E7EB;
    margin-top: 3rem;
    margin-bottom: 3rem;
}

</style>
""", unsafe_allow_html=True)

# CABEÇALHO

st.markdown("""
<div class='hero-box'>

# Fernanda Bertão

<p class='subtitle'>
Itaú • UFABC • Dados
</p>

Estagiária em Análise de Dados no Itaú • Débitos Automáticos.  
Estudante de Ciência e Tecnologia na **UFABC** .

</div>
""", unsafe_allow_html=True)

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
        "https://drive.google.com/file/d/1EmCJgnXyH5Wz_X9FjjthlOQLQWwtMy2E/view?usp=sharing",
        use_container_width=True
    )

st.divider()

# EXPERIÊNCIA


st.header("💼 Experiência — Itaú")

st.write("""
Estagiária na comunidade **Plataforma e Jornadas de Daily Baking**, como membro cross atendendo as Squads Recepção de Pagementos, Efetivação de Pagamentos e Torre de Prioridade de Pagamentos.
Atuando no desenvolvimento e monitoramento de indicadores-chave, análise de volumetria e identificação de desafios em projetos de modernização da plataforma de débitos automáticos.

Experiências com: Athena (SQL), S3, QuickSight, SageMaker (Python), Pacote Office
""")

with st.expander("📊 HUB de Ocorrências", expanded=False):
    st.markdown("""
**Dashboard analítico desenvolvido em conjunto com times de dados
para acompanhamento de reclamações e identificação de oportunidades
na visão cliente.**

### Atividades
- Criação de lógica (SQL) para o produto débito automático
- Adição de linha de plataforma de débitos automáticos como filtro
                
### Impacto
Identificação de oportunidades de melhoria, acompanhamento constante de reclamações e eficiência na rotina de extração e divulgação de informações relevantes para áreas parceiras.
""")

with st.expander("🗂️ Governança de Dados", expanded=False):
    st.markdown("""
**Atualização da documentação de bases críticas
utilizadas pelo time.**

### Atividades
- Mapeamento de atributos e campos
- Levantamento de regras e tipos de dados
- Atualização de documentação técnica
- Atualização de De x Para de campos

### Impacto
Maior rastreabilidade, entendimento e confiabilidade
das bases utilizadas nas análises.
""")

with st.expander("📈 Análise de Rejeições de Débitos", expanded=False):
    st.markdown("""
**Projeto analítico para identificação dos principais ofensores
de rejeições de débitos e oportunidades de melhoria operacional.**

    
### Atividades
- Identificação dos principais motivos de rejeição
- Levantamento dos produtos com maior incidência
- Geração de insights para áreas parceiras

### Impacto
Melhoria da eficiência analítica e maior confiabilidade
nas análises operacionais.
""")

with st.expander("🤖 Agente de IA para Documentação Técnica", expanded=False):
    st.markdown("""
**Participação no desenvolvimento de um agente de IA voltado à
centralização e consulta de documentações técnicas e operacionais.**

### Atividades
- Criação e alimentação da base de conhecimento
- Organização de documentação técnica
- Apoio ao treinamento do agente
- Estruturação de informações para acesso rápido

### Impacto
Facilitar o acesso ao conhecimento para times
técnicos, de dados e negócio.
""")

with st.expander("⚙️ Modernização da Plataforma de Débitos", expanded=False):
    st.markdown("""
**Participação em iniciativa de modernização operacional
da plataforma de débitos automáticos.**

### Atividades
- Levantamento de dados volumétricos
- Validação de cenários operacionais
- Acompanhamento do ciclo de vida dos débitos
- Monitoramento de indicadores da modernização
""")

with st.expander("⚙️ Painel para acompanhamento de Modernização - Nova Efetivação", expanded=False):
    st.markdown("""
**Painel desenvolvido para acompanhamento diário dos porincipais indicadores do Nova Efetivação, proprocionando uma visão clara e objetiva da modernização.**

### Atividades
- Estudo de bases de dados e entendimento de indicadores-chave
- Revisão de regras
- Criação da base (SPEC) pra criação do painel
- Painel V1 no QuickSight
- Criação de uma visão histórica para acompanhamento da evolução da modernização
                
### Benefícios
Principais visões de indicadores consolidados em um único local, peridiocidade de atualização por **hora** e acompanhamento da evolução da modernização.
""")

with st.expander("🧠 Modelo de Machine Learning para Classificação", expanded=False):
    st.markdown("""
**Projeto em desenvolvimento para clustrização e classificação de reclamações de débitos automáticos para identificação de problemas da plataforma.**

### Atividades
- NLP para clusterização de reclamações
- Regressão Logística para classificação binária (plataforma e produtos de débitos)
                
### Impacto
Visão clara sobre a origem dos principais problemas relacionados a débitos, otimização de tempo e redução de trabalho manual na análise de dores.
""")

st.divider()

# FORMAÇÃO
st.header("🎓 Formação")

st.subheader("UFABC — Universidade Federal do ABC")

st.write("""
Formação quantitativa com foco em:

- Interdisciplinar em Ciências
- Ciência de Dados
- Matemática Aplicada
""")

st.divider()
# PROJETOS ACADÊMICOS


st.header("🔬 Projetos Acadêmicos")

with st.expander("📈 TrendBot — Previsão de Ativos Financeiros", expanded=False):
    st.markdown("""
Projeto de **Iniciação Científica** voltado à previsão
probabilística de ativos financeiros utilizando
**séries temporais e machine learning**.

### Desenvolvimento
- Base de dados do Kaggle
- Janela deslizante de 20 dias
- Criação de alvo binário  
(subiu ou não subiu)

### Tecnologias
`Python` `Pandas`  
`Machine Learning`  
`Time Series`
""")

st.divider()

# SKILLS

st.header("🛠️ Skills")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("SQL", "Intermediário")

with col2:
    st.metric("Outras ferramentas AWS", "Básico")

with col3:
    st.metric("Python", "Intermediário")

with col4:
    st.metric("Machine Learning", "Básico")

st.divider()
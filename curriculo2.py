import streamlit as st

# confi da pag

st.set_page_config(
    page_title="Fernanda Bertão",
    page_icon="📊",
    layout="wide"
)

import streamlit as st

# confi da pag

st.set_page_config(
    page_title="Fernanda Bertão",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

/* ======== PALETA ITAÚ ======== */

:root {
    --itau-orange: #EC7000;
    --itau-blue: #003B5C;
    --light-bg: #F8F9FB;
    --card-bg: #FFFFFF;
    --border: #E8ECF2;
    --text: #1E293B;
    --subtitle: #64748B;
}

/* ======== GERAL ======== */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: white;
    color: var(--text);
}

.main {
    padding-left: 8rem;
    padding-right: 8rem;
}

/* ======== TITULOS ======== */

h1 {
    color: var(--itau-blue);
    font-size: 58px;
    font-weight: 700;
    margin-bottom: 0;
}

h2 {
    color: var(--itau-blue);
    margin-top: 30px;
}

h3 {
    color: var(--itau-blue);
}

/* ======== HERO ======== */

.hero-box {
    background: linear-gradient(
        135deg,
        rgba(236,112,0,0.08),
        rgba(0,59,92,0.03)
    );

    padding: 40px;
    border-radius: 28px;
    border: 1px solid var(--border);
    margin-bottom: 30px;
}

.subtitle {
    font-size: 22px;
    color: var(--subtitle);
}

/* ======== BOTÕES ======== */

.stLinkButton > a {
    background-color: white !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    color: var(--itau-blue) !important;
    font-weight: 600 !important;
    transition: 0.3s;
}

.stLinkButton > a:hover {
    border: 1px solid var(--itau-orange) !important;
    color: var(--itau-orange) !important;
}

/* ======== EXPANDERS ======== */

.streamlit-expanderHeader {
    font-size: 18px;
    font-weight: 600;
    color: var(--itau-blue);
}

div[data-testid="stExpander"] {
    border-radius: 20px !important;
    border: 1px solid var(--border) !important;
    background-color: white !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    transition: 0.3s;
}

div[data-testid="stExpander"]:hover {
    border: 1px solid var(--itau-orange) !important;
}

/* ======== INFO BOX ======== */

div[data-testid="stMarkdownContainer"] ul {
    line-height: 1.8;
}

/* ======== METRICS ======== */

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

div[data-testid="stMetric"]:hover {
    border: 1px solid var(--itau-orange);
    transition: 0.3s;
}

/* ======== DIVIDER ======== */

hr {
    margin-top: 3rem;
    margin-bottom: 3rem;
    border: none;
    border-top: 1px solid #ECECEC;
}

/* ======== SIDEBAR ======== */

[data-testid="stSidebar"] {
    background-color: #FAFAFA;
    border-right: 1px solid var(--border);
}

</style>
            
/* TEXTO DOS EXPANDERS */
.streamlit-expanderHeader {
    color: #003B5C !important;
    font-weight: 600 !important;
}

/* CORPO DO EXPANDER */
[data-testid="stExpanderDetails"] {
    background-color: white !important;
    color: #1E293B !important;
    border-radius: 16px;
    padding: 10px;
}

/* TEXTO INTERNO */
[data-testid="stMarkdownContainer"] {
    color: #1E293B !important;
}

/* st.info */
[data-testid="stAlert"] {
    background-color: #F8F9FB !important;
    color: #1E293B !important;
    border: 1px solid #E8ECF2 !important;
    border-radius: 16px;
}

</style>
""", unsafe_allow_html=True)

# cabeçalho

st.markdown("""
<div class='hero-box'>

# Fernanda Bertão

<p class='subtitle'>
UFABC • Itaú • Dados
</p>

Estagiária em Análise de Dados no Itaú, na área de débitos automáticos.  
Estudante da **UFABC** com experiência em pesquisa acadêmica.

Atualmente desenvolvendo projetos em
**previsão de séries temporais financeiras**.

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
        "https://drive.google.com/file/d/1Sc7kObUhBdNrLJ-e5J9XKNk1Zdn2hiHA/view?usp=sharing",
        use_container_width=True
    )

st.divider()

# exp

st.header("💼 Experiência — Itaú")

st.write("""
Estagiária na comunidade **Plataforma e Jornadas de Daily Baking**, atuando no desenvolvimento e monitoramento de indicadores-chave, análise de volumetria e identificação de desafios em projetos de modernização da plataforma de débitos automáticos.

Experiências com: Athena (SQL), S3, QuickSight, SageMaker (Python), Pacote Office
""")

# ---------- PROJETO 1 ----------
with st.expander("📊 HUB de Ocorrências", expanded=False):

    st.markdown("""
**Dashboard analítico desenvolvido em conjunto com times de dados
para acompanhamento de reclamações e identificação de oportunidades
na visão cliente.**

### Objetivos
- Acompanhamento constante das reclamações.
- Identificação de oportunidades de melhoria.
- Eficiência na rotina de extração e divulgação.
""")


# ---------- PROJETO 2 ----------
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


# ---------- PROJETO 3 ----------
with st.expander("📈 Análise de Rejeições de Débitos", expanded=False):

    st.markdown("""
**Projeto analítico para identificação dos principais ofensores
de rejeições de débitos e oportunidades de melhoria operacional.**

### Entregas
- Identificação dos principais motivos de rejeição
- Levantamento dos produtos com maior incidência
- Geração de insights para áreas parceiras

### Resultado
Melhoria da eficiência analítica e maior confiabilidade
nas análises operacionais.
""")


# ---------- PROJETO 4 ----------
with st.expander("🤖 Agente de IA para Documentação Técnica", expanded=False):

    st.markdown("""
**Participação no desenvolvimento de um agente de IA voltado à
centralização e consulta de documentações técnicas e operacionais.**

### Contribuições
- Alimentação da base de conhecimento
- Organização de documentação técnica
- Apoio ao treinamento do agente
- Estruturação de informações para acesso rápido

### Objetivo
Facilitar o acesso ao conhecimento para times
técnicos, de dados e negócio.
""")


# ---------- PROJETO 5 ----------
with st.expander("⚙️ Modernização da Plataforma de Débitos", expanded=False):

    st.markdown("""
**Participação em iniciativa de modernização operacional
da plataforma de débitos automáticos.**

### Responsabilidades
- Levantamento de dados volumétricos
- Validação de cenários operacionais
- Acompanhamento do ciclo de vida dos débitos
- Monitoramento de indicadores da modernização
""")


# ---------- PROJETO 7 ----------
with st.expander(
    "⚙️ Painel para acompanhamento de Modernização - Nova Efetivação",
    expanded=False
):

    st.markdown("""
**Painel desenvolvido para acompanhamento diário dos principais indicadores do Nova Efetivação, proporcionando uma visão clara e objetiva da modernização.**

### Benefícios
- Principais visões de indicadores consolidados em um único local
- Periodicidade de atualização por **hora**
- Acompanhamento da evolução da modernização.
""")


# ---------- PROJETO 6 ----------
with st.expander(
    "🧠 Modelo de Machine Learning para Classificação",
    expanded=False
):

    st.markdown("""
**Projeto em desenvolvimento para clusterização e classificação de reclamações de débitos automáticos.**

### Abordagem
- Clusterização de reclamações
- Modelagem supervisionada
- Classificação binária
- Regressão logística
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

# ---------- PROJETO ACADÊMICO ----------
with st.expander(
    "📈 TrendBot — Previsão de Ativos Financeiros",
    expanded=False
):

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



# cabeçalho

st.markdown("""
<div class='hero-box'>

# Fernanda Bertão

<p class='subtitle'>
UFABC • Itaú • Dados
</p>

Estagiária em Análise de Dados no Itaú, na área de débitos automáticos.  
Estudante da **UFABC** com experiência em pesquisa acadêmica.

Atualmente desenvolvendo projetos em
**previsão de séries temporais financeiras**.

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
        "https://drive.google.com/file/d/1Sc7kObUhBdNrLJ-e5J9XKNk1Zdn2hiHA/view?usp=sharing",
        use_container_width=True
    )

st.divider()

# exp

st.header("💼 Experiência — Itaú")

st.write("""
Estagiária na comunidade **Plataforma e Jornadas de Daily Baking**, atuando no desenvolvimento e monitoramento de indicadores-chave, análise de volumetria e identificação de desafios em projetos de modernização da plataforma de débitos automáticos.

Experiências com: Athena (SQL), S3, QuickSight, SageMaker (Python), Pacote Office
""")

# ---------- PROJETO 1 ----------
with st.expander("📊 HUB de Ocorrências", expanded=False):

    st.markdown("""
**Dashboard analítico desenvolvido em conjunto com times de dados
para acompanhamento de reclamações e identificação de oportunidades
na visão cliente.**

### Objetivos
- Acompanhamento constante das reclamações.
- Identificação de oportunidades de melhoria.
- Eficiência na rotina de extração e divulgação.
""")


# ---------- PROJETO 2 ----------
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


# ---------- PROJETO 3 ----------
with st.expander("📈 Análise de Rejeições de Débitos", expanded=False):

    st.markdown("""
**Projeto analítico para identificação dos principais ofensores
de rejeições de débitos e oportunidades de melhoria operacional.**

### Entregas
- Identificação dos principais motivos de rejeição
- Levantamento dos produtos com maior incidência
- Geração de insights para áreas parceiras

### Resultado
Melhoria da eficiência analítica e maior confiabilidade
nas análises operacionais.
""")


# ---------- PROJETO 4 ----------
with st.expander("🤖 Agente de IA para Documentação Técnica", expanded=False):

    st.markdown("""
**Participação no desenvolvimento de um agente de IA voltado à
centralização e consulta de documentações técnicas e operacionais.**

### Contribuições
- Alimentação da base de conhecimento
- Organização de documentação técnica
- Apoio ao treinamento do agente
- Estruturação de informações para acesso rápido

### Objetivo
Facilitar o acesso ao conhecimento para times
técnicos, de dados e negócio.
""")


# ---------- PROJETO 5 ----------
with st.expander("⚙️ Modernização da Plataforma de Débitos", expanded=False):

    st.markdown("""
**Participação em iniciativa de modernização operacional
da plataforma de débitos automáticos.**

### Responsabilidades
- Levantamento de dados volumétricos
- Validação de cenários operacionais
- Acompanhamento do ciclo de vida dos débitos
- Monitoramento de indicadores da modernização
""")


# ---------- PROJETO 7 ----------
with st.expander(
    "⚙️ Painel para acompanhamento de Modernização - Nova Efetivação",
    expanded=False
):

    st.markdown("""
**Painel desenvolvido para acompanhamento diário dos principais indicadores do Nova Efetivação, proporcionando uma visão clara e objetiva da modernização.**

### Benefícios
- Principais visões de indicadores consolidados em um único local
- Periodicidade de atualização por **hora**
- Acompanhamento da evolução da modernização.
""")


# ---------- PROJETO 6 ----------
with st.expander(
    "🧠 Modelo de Machine Learning para Classificação",
    expanded=False
):

    st.markdown("""
**Projeto em desenvolvimento para clusterização e classificação de reclamações de débitos automáticos.**

### Abordagem
- Clusterização de reclamações
- Modelagem supervisionada
- Classificação binária
- Regressão logística
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

# ---------- PROJETO ACADÊMICO ----------
with st.expander(
    "📈 TrendBot — Previsão de Ativos Financeiros",
    expanded=False
):

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


import streamlit as st

# config da página

st.set_page_config(
    page_title="Projetos Acadêmicos",
    page_icon="🔬",
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

/* título do expander */

[data-testid="stExpander"] summary {

    color: #111827 !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* texto do header */

[data-testid="stExpander"] summary * {
    color: #111827 !important;
}
            
[data-testid="stExpanderDetails"] * {
    color: #111827 !important;
}
            
[data-testid="stExpander"] summary * {
    color: #111827 !important;
}

/* texto */

.stMarkdown p,
.stMarkdown li,
.stMarkdown span,
.stMarkdown label {
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
        
.stButton > button * {
    color: #111827 !important;
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

if st.button("← Voltar para Home"):
    st.switch_page("app.py")

st.markdown("""
<div class='page-title'>
🔬 Projetos Acadêmicos
</div>

<div class='page-subtitle'>
Projetos desenvolvidos durante a graduação
com foco em ciência de dados, machine learning,
automação e liderança em comunidades acadêmicas.
</div>
""", unsafe_allow_html=True)


# ic

with st.expander("📈 TrendBot — Previsão de Ativos Financeiros"):

    st.markdown("""
Projeto de **Iniciação Científica (UFABC)** desenvolvido
sob orientação do **Prof. Mateus Coelho**, com foco na
previsão probabilística de movimentos direcionais
(**Up / Not Up**) em ativos financeiros utilizando
**Deep Learning e séries temporais**.

O objetivo do projeto não é prever o mercado de forma
determinística, mas gerar **sinais probabilísticos**
para apoio à decisão, permitindo ajuste de diferentes
níveis de confiança (**threshold**) conforme o perfil
de risco desejado.

### Desenvolvimento

- Estruturação de pipeline de séries temporais
- Transformação de preços históricos em
janelas deslizantes de **20 dias**
- Conversão de preços em variações percentuais
- Tratamento de outliers e normalização dos dados
- Modelagem preditiva utilizando Deep Learning

### Modelagem

Arquitetura baseada em rede neural densa com:

- Camadas Dense + ReLU
- Batch Normalization
- Dropout para controle de overfitting
- Regularização e balanceamento de classes
- Early Stopping e Learning Rate Reduction

### Avaliação

Análise do desempenho utilizando:

- Accuracy
- Precision
- Recall
- F1-Score
- AUC-ROC
- Matriz de confusão

Além disso, foram avaliados diferentes níveis
de confiança (**threshold**) para análise do
trade-off entre **risco, precisão e volume
de operações**.

### Tecnologias

`Python`
`Pandas`
`TensorFlow/Keras`
`Scikit-Learn`
`Machine Learning`
`Time Series`
`Deep Learning`
""")

# GREEN TEAM

with st.expander("🎯 Data Lead — Green Team"):

    st.markdown("""
Green Team é uma entidade estudantil de computação, com vários núcleos de atuação. Atualmente, atuo como **Data Lead** no núcleo de dados, onde ministro aulas para iniciantes em dados, preparo atividades práticas para fixação de conteúdo e lidero projetos de análise de dados para organizações sociais parceiras, com foco em geração de impacto social por meio da ciência de dados.
""")

# AWS CLUB

with st.expander("☁️ Tech Lead — AWS Cloud Club"):

    st.markdown("""
Participação como **Tech Lead** no AWS Cloud Club,
com foco em iniciativas tecnológicas, organização
de projetos e disseminação de conhecimento técnico.
""")

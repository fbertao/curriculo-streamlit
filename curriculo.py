import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# carregamento dos dados
df = pd.read_csv("entregas.csv")

# Padronizar texto (evita problema de acento e espaço)
df["empresa"] = df["empresa"].str.strip().str.lower()
df["tipo"] = df["tipo"].str.strip().str.lower()

# titulo
st.title("Fernanda Bertão")
st.subheader("Ciência de Dados - UFABC")
st.subheader("Estagiária Analista de Dados (Itaú - dezembro/2024 - presente)")

st.markdown("""
Profissional com atuação em:
- Analises de dados com viés para negócios
- Clusterização e análise exploratória
- Governança de dados
- Machine Learning (projeto acadêmico)
            
**Modelos de Machine Learning:**
- DNN (Deep Neural Network)
- Regressão Logística
- Random Forest
""")

st.divider()

# filtro lateral
st.sidebar.header("Filtros")

empresa_filtro = st.sidebar.multiselect(
    "Filtrar por Empresa",
    options=df["empresa"].unique(),
    default=df["empresa"].unique()
)

tipo_filtro = st.sidebar.multiselect(
    "Filtrar por Tipo",
    options=df["tipo"].unique(),
    default=df["tipo"].unique()
)

df_filtrado = df[
    (df["empresa"].isin(empresa_filtro)) &
    (df["tipo"].isin(tipo_filtro))
]

# KPI principais 
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de Projetos", len(df_filtrado))
col2.metric("Projetos Itaú", (df_filtrado["empresa"]=="itau").sum())
col3.metric("Projetos Modernização", (df_filtrado["tipo"]=="modernizacao").sum())
col4.metric("Projetos ML", (df_filtrado["tipo"]=="machine learning").sum())

st.divider()

st.subheader("Resumo profissional")
st.write("""
    Sou estagiária na área de débito automático no Itaú Unibanco, onde participo do desenvolvimento e acompanhamento de projetos de análise de dados utilizando ferramentas da AWS no dia a dia, como Athena (SQL), S3, QuickSight e Glue.
    Na faculdade, estou envolvida em dois projetos relevantes: 
         
    - Pesquisa científica: desenvolvimento de um TrendBot usando modelos de machine learning (DNN, Deep Neural Network), aplicando diariamente bibliotecas de python (pandas, tensorflow, scikit learn, matplot, numpy), conceitos matemáticos e git / github.
         
    - Green Team: entidade estudantil voltada para estudantes da computação. Atuei por 9 meses como gestora de dados, ministrando aulas e acompanhando projetos. Atualmente, continuo como integrante do grupo, exercendo a função de Analista de AWS Cloud em um núcleo de estudos focados em computação em nuvem.
    
    Meu linkedin é https://www.linkedin.com/in/fbertao/
""")

# graficos de distribuição
st.subheader("Distribuição por Tipo de Entrega")
fig1  = px.histogram(
    df_filtrado,
    x="tipo",
    color_discrete_sequence=["#FF0000"]
    )
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Distribuição por Categoria Técnica")
fig2 = px.histogram(
    df_filtrado, 
    x="categoria_tecnica",
    color_discrete_sequence=["#FF0000"]
    )
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# detalhe dos projetos
st.subheader("Explorar Projeto em Detalhe")

projeto = st.selectbox("Selecione um projeto", df_filtrado["entrega"].unique())

detalhes = {
    "HUB de Ocorrencias": """
**Objetivo:** Monitoramento detalhado de reclamações bancárias  
**Impacto Técnico:** Construção de queries + clusterização  
**Impacto de Negócio:** Acompanhamento real-time e identificação de causas  
""",

    "Portal de Governanca": """
**Objetivo:** Organizar e documentar bases utilizadas em squads de débito  
**Impacto Técnico:** Discovery de bases, atualização de atributos  
**Impacto de Negócio:** Mitigação de risco analítico  
""",

    "Levantamento BACEN": """
**Objetivo:** Redução de reclamações via BACEN  
**Impacto Técnico:** Clusterização procedente vs improcedente  
**Impacto de Negócio:** Aumento de satisfação do cliente  
""",

    "Rejeicoes de Debitos": """
**Objetivo:** Reduzir rejeições na plataforma  
**Impacto Técnico:** Análise exploratória de produtos e motivos  
**Impacto de Negócio:** Maior eficiência operacional  
""",

    "Agente de IA (Debitinho)": """
**Objetivo:** Criar facilitador inteligente para squad no dia a dia  
**Impacto Técnico:** Knowledge base + Prompt Engineering + Treinamento contínuo  
**Impacto de Negócio:** Agilidade no acesso à documentação técnica  
""",

    "Piloto Convivencia": """
**Objetivo:** Acompanhamento de cenários de modernização  
**Impacto Técnico:** Validação de cenários + acompanhamento de fluxo  
**Impacto de Negócio:** Maior confiabilidade na implantação  
""",

    "Nova Efetivacao": """
**Objetivo:** Acompanhar fluxo legado vs modernizado  
**Impacto Técnico:** Construção de painel via QuickSight  
""",

    "TrendBot": """
**Projeto de Machine Learning (UFABC)**  

**Objetivo:** Prever probabilidade de ativo subir no próximo dia  

**Técnico:**
- Janela deslizante de 20 dias
- Modelo DNN
- Matriz de confusão
- Simulador com threshold  

🔗 https://github.com/fbertao/TrendBot-financeiro.py
"""
}

if projeto in detalhes:
    st.markdown(detalhes[projeto])
else:
    st.warning("Detalhes não encontrados para esse projeto.")
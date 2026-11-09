import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dados import obter_dados_municipios

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Dashboard Demográfico: Crescimento Populacional Municipal",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS customizada
st.markdown("""
<style>
    .metric-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-title {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #94a3b8;
        margin-bottom: 6px;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #f8fafc;
    }
    .metric-sub {
        font-size: 0.8rem;
        margin-top: 6px;
        color: #cbd5e1;
    }
</style>
""", unsafe_allow_html=True)

# --- BASE DE DADOS DOS MUNICÍPIOS (CENÁRIO BRASIL) ---
@st.cache_data
def carregar_dados():
    return obter_dados_municipios()

df_full = carregar_dados()

# --- SIDEBAR DE CONTROLE E FILTROS ---
st.sidebar.title("Filtros do Dashboard")
st.sidebar.markdown("Explore o ritmo de expansão anual e as assimetrias demográficas.")

# Filtro Região
regioes_disponiveis = ["Todas as Regiões"] + sorted(df_full["regiao"].unique().tolist())
regiao_selecionada = st.sidebar.selectbox("Macrorregião:", regioes_disponiveis)

# Filtro Porte
portes_disponiveis = ["Todos os Portes"] + [
    "Pequeno (<20k)", 
    "Médio-Pequeno (20k-50k)", 
    "Médio (50k-150k)", 
    "Médio-Grande (150k-500k)", 
    "Grande / Metrópole (>500k)"
]
porte_selecionado = st.sidebar.selectbox("Porte Populacional:", portes_disponiveis)

# Filtro Range de Taxa
min_taxa, max_taxa = float(df_full["taxa"].min()), float(df_full["taxa"].max())
range_taxa = st.sidebar.slider(
    "Ritmo Anual (% a.a.):",
    min_value=min_taxa,
    max_value=max_taxa,
    value=(min_taxa, max_taxa),
    step=0.1,
    format="%.1f%%"
)

# Filtro de Busca
busca_municipio = st.sidebar.text_input("Buscar município ou UF:")

# Aplicação dos filtros
df_filtrado = df_full.copy()
if regiao_selecionada != "Todas as Regiões":
    df_filtrado = df_filtrado[df_filtrado["regiao"] == regiao_selecionada]
if porte_selecionado != "Todos os Portes":
    df_filtrado = df_filtrado[df_filtrado["porte"] == porte_selecionado]

df_filtrado = df_filtrado[
    (df_filtrado["taxa"] >= range_taxa[0]) & 
    (df_filtrado["taxa"] <= range_taxa[1])
]

if busca_municipio.strip():
    termo = busca_municipio.strip().lower()
    df_filtrado = df_filtrado[
        df_filtrado["nome"].str.lower().str.contains(termo) | 
        df_filtrado["uf"].str.lower().str.contains(termo)
    ]

# --- CABEÇALHO PRINCIPAL ---
st.title("📊 Crescimento Populacional Absoluto & Ritmo Anual dos Municípios")
st.markdown("""
Análise detalhada do **ritmo de expansão anual** dos municípios brasileiros com foco no cálculo rigoroso e interpretação 
estatística de **médias**, **medianas**, **desvios padrão** e o impacto em **volume absoluto de habitantes/ano**.
""")

# --- CÁLCULO DAS ESTATÍSTICAS ---
if len(df_filtrado) > 0:
    media_taxa = df_filtrado["taxa"].mean()
    mediana_taxa = df_filtrado["taxa"].median()
    desvio_taxa = df_filtrado["taxa"].std(ddof=1) if len(df_filtrado) > 1 else 0.0
    cv_taxa = (desvio_taxa / abs(media_taxa) * 100) if media_taxa != 0 else 0.0
    total_ganho_abs = df_filtrado["ganho_absoluto"].sum()
    pop_total_amostra = df_filtrado["pop"].sum()
    n_declinio = (df_filtrado["taxa"] < 0).sum()
    n_boom = (df_filtrado["taxa"] > 2.0).sum()
else:
    media_taxa = mediana_taxa = desvio_taxa = cv_taxa = total_ganho_abs = pop_total_amostra = n_declinio = n_boom = 0

# --- CARDS DE MÉTRICAS (KPIS) ---
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="Média da Taxa Anual",
        value=f"{media_taxa:+.2f}% a.a.",
        delta=f"{media_taxa - mediana_taxa:+.2f} p.p. vs mediana",
        delta_color="off",
        help="Média aritmética das taxas. Sensível a cidades com expansão atípica."
    )

with col2:
    st.metric(
        label="Mediana (Município Típico)",
        value=f"{mediana_taxa:+.2f}% a.a.",
        delta="Percentil 50%",
        delta_color="off",
        help="Metade dos municípios cresce abaixo deste valor e metade acima. Insensível a outliers."
    )

with col3:
    st.metric(
        label="Desvio Padrão (σ)",
        value=f"{desvio_taxa:.2f}%",
        delta=f"CV: {cv_taxa:.0f}%",
        delta_color="off",
        help="Mensura a dispersão e desigualdade entre municípios. Quanto maior, maior a polarização."
    )

with col4:
    st.metric(
        label="Crescimento Absoluto",
        value=f"{total_ganho_abs:+,d} hab/ano".replace(",", "."),
        delta=f"Base: {pop_total_amostra/1e6:.1f}M hab",
        delta_color="off",
        help="Volume real de habitantes adicionados anualmente no conjunto de municípios."
    )

with col5:
    status_assimetria = "Positiva (μ > Md)" if media_taxa > mediana_taxa + 0.1 else ("Negativa (μ < Md)" if media_taxa < mediana_taxa - 0.1 else "Simétrica")
    st.metric(
        label="Assimetria / Tendência",
        value=status_assimetria,
        delta=f"{n_declinio} declínio | {n_boom} boom",
        delta_color="off",
        help="Indica a inclinação da curva e a presença de polos de crescimento que puxam a média."
    )

st.markdown("---")

# --- GRÁFICOS INTERATIVOS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Comparativo Regional (Média vs Mediana)", 
    "📊 Distribuição & Assimetria (Histograma)", 
    "🎯 Matriz de Ritmo (Taxa % vs Ganho Absoluto)", 
    "📦 Dispersão e Quartis (Boxplot)"
])

with tab1:
    st.subheader("Comparativo por Macrorregião: Média, Mediana e Desvio Padrão")
    st.markdown(r"""
    Compare a **Média** (azul) e a **Mediana** (verde) de cada região. As barras de erro representam a 
    amplitude de **$\pm 1$ Desvio Padrão**, ilustrando o grau de heterogeneidade intra-regional.
    """)
    
    # Cálculo das estatísticas por região
    df_reg = df_full.groupby("regiao")["taxa"].agg(
        Media="mean",
        Mediana="median",
        Desvio="std",
        Contagem="count"
    ).reset_index()

    fig_reg = go.Figure()
    
    # Barra da Média com Barra de Erro (Desvio Padrão)
    fig_reg.add_trace(go.Bar(
        x=df_reg["regiao"],
        y=df_reg["Media"],
        name="Média Aritmética (μ)",
        marker_color="#3b82f6",
        error_y=dict(type='data', array=df_reg["Desvio"], visible=True, color="#ef4444", thickness=1.5, width=6),
        hovertemplate="<b>%{x}</b><br>Média: %{y:.2f}% a.a.<br>Desvio Padrão: ±%{error_y.array:.2f} p.p.<extra></extra>"
    ))
    
    # Barra da Mediana
    fig_reg.add_trace(go.Bar(
        x=df_reg["regiao"],
        y=df_reg["Mediana"],
        name="Mediana (Percentil 50)",
        marker_color="#10b981",
        hovertemplate="<b>%{x}</b><br>Mediana: %{y:.2f}% a.a.<extra></extra>"
    ))
    
    fig_reg.update_layout(
        barmode='group',
        height=450,
        xaxis_title="Macrorregião",
        yaxis_title="Ritmo Anual de Crescimento (% a.a.)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig_reg, use_container_width=True)

with tab2:
    st.subheader("Distribuição de Frequência das Taxas Anuais")
    st.markdown("""
    O histograma evidencia a **forma da distribuição**. As linhas verticais tracejadas marcam a **Mediana** 
    e a **Média**, permitindo diagnosticar a cauda longa à direita (assimetria provocada por cidades de forte atração).
    """)
    
    if len(df_filtrado) > 0:
        fig_hist = px.histogram(
            df_filtrado, 
            x="taxa", 
            nbins=20,
            color="regiao",
            marginal="rug",
            labels={"taxa": "Taxa de Crescimento Anual (% a.a.)", "count": "Nº de Municípios"},
            hover_data=["nome", "uf", "pop", "ganho_absoluto"]
        )
        # Linha vertical da Média
        fig_hist.add_vline(x=media_taxa, line_width=2.5, line_dash="dash", line_color="#3b82f6", 
                           annotation_text=f"Média: {media_taxa:.2f}%", annotation_position="top left")
        # Linha vertical da Mediana
        fig_hist.add_vline(x=mediana_taxa, line_width=2.5, line_dash="dash", line_color="#10b981", 
                           annotation_text=f"Mediana: {mediana_taxa:.2f}%", annotation_position="top right")
        
        fig_hist.update_layout(height=450, margin=dict(l=40, r=40, t=40, b=40))
        st.plotly_chart(fig_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado com os filtros selecionados.")

with tab3:
    st.subheader("Matriz de Ritmo: Taxa Anual (%) vs Ganho Absoluto (+Hab/ano)")
    st.markdown("""
    Cruze o **ritmo relativo (%)** com o **volume populacional adicionado (+habitantes/ano)**. 
    O tamanho das bolhas reflete a população total de cada município.
    """)
    
    if len(df_filtrado) > 0:
        fig_scatter = px.scatter(
            df_filtrado,
            x="taxa",
            y="ganho_absoluto",
            size="pop",
            color="regiao",
            hover_name="nome",
            hover_data={"uf": True, "pop": ":,d", "taxa": ":.2f", "ganho_absoluto": ":,d"},
            labels={
                "taxa": "Taxa Anual de Crescimento (% a.a.)",
                "ganho_absoluto": "Ganho Absoluto (+Habitantes/ano)",
                "regiao": "Região"
            },
            size_max=35
        )
        fig_scatter.add_hline(y=0, line_dash="dot", line_color="#64748b")
        fig_scatter.add_vline(x=0, line_dash="dot", line_color="#64748b")
        fig_scatter.update_layout(height=480, margin=dict(l=40, r=40, t=40, b=40))
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para dispersão.")

with tab4:
    st.subheader("Dispersão e Quartis por Região (Boxplot)")
    st.markdown(r"""
    O Boxplot permite verificar claramente os **outliers** (pontos isolados), a distância interquartil 
    ($IQR = Q_3 - Q_1$) e a linha central da mediana por região geográfica.
    """)
    
    fig_box = px.box(
        df_full,
        x="regiao",
        y="taxa",
        color="regiao",
        points="all",
        hover_name="nome",
        labels={"taxa": "Taxa Anual (% a.a.)", "regiao": "Região"}
    )
    fig_box.update_layout(height=450, showlegend=False, margin=dict(l=40, r=40, t=40, b=40))
    st.plotly_chart(fig_box, use_container_width=True)

st.markdown("---")

# --- GUIA DE INTERPRETAÇÃO DEMOGRÁFICA E ESTATÍSTICA ---
st.subheader("🧠 Interpretação Estatística Aprofundada")

c_int1, c_int2, c_int3 = st.columns(3)

with c_int1:
    st.markdown(r"""
    #### 1. Média vs. Mediana
    - **O Fenômeno da Assimetria Positiva:** Em estudos municipais, a média quase sempre supera a mediana ($\mu > Md$).
    - **O Risco da Média:** Poucos municípios com expansão explosiva (ex: polos do agronegócio em MT/GO ou mineração no PA) elevam a média artificialmente.
    - **Recomendação Prática:** Para entender o comportamento do **município típico**, utilize sempre a **mediana**.
    """)

with c_int2:
    st.markdown(r"""
    #### 2. O Papel do Desvio Padrão ($\sigma$)
    - **Heterogeneidade Espacial:** Um desvio padrão alto (ex: $> 2.0\%$) revela que municípios vizinhos vivem realidades opostas: uns crescendo acima de $4\%$ a.a. e outros em declínio.
    - **Centro-Oeste e Sudeste:** Apresentam forte dispersão por abrigarem tanto centros dinâmicos quanto cidades interioranas estagnadas.
    - **Sul:** Apresenta menor dispersão e taxas mais moderadas, reflexo de transição demográfica avançada.
    """)

with c_int3:
    st.markdown(r"""
    #### 3. Ritmo Relativo vs. Volume Absoluto
    - **Ritmo (% a.a.):** Crucial para saber a velocidade de saturação de serviços públicos locais (creches, saneamento).
    - **Volume (+Hab/ano):** Uma cidade de 15 mil habitantes crescendo a $5\%$ adiciona $+750$ hab/ano. Uma metrópole crescendo a apenas $0.5\%$ adiciona $+10.000$ hab/ano.
    - Ambas as métricas são indispensáveis para o planejamento orçamentário.
    """)

st.markdown("---")

# --- SIMULADOR DE PROJEÇÃO POPULACIONAL ---
st.subheader("🔮 Simulador de Projeção: Impacto da Média vs Mediana")
st.markdown("Simule a evolução de um município e veja na prática o viés de sobre-estimativa ao utilizar a média em vez da mediana.")

sim_col1, sim_col2, sim_col3 = st.columns([1, 1, 2])

with sim_col1:
    pop_inicial = st.number_input("População Inicial (hab):", min_value=1000, max_value=15000000, value=100000, step=10000)
    anos_projecao = st.slider("Horizonte de Projeção (anos):", min_value=1, max_value=30, value=10)

with sim_col2:
    # Projeção Exponencial: P(t) = P0 * (1 + r)^t
    r_mediana = mediana_taxa / 100
    r_media = media_taxa / 100
    
    pop_proj_mediana = int(pop_inicial * ((1 + r_mediana) ** anos_projecao))
    pop_proj_media = int(pop_inicial * ((1 + r_media) ** anos_projecao))
    delta_proj = pop_proj_media - pop_proj_mediana
    
    st.markdown(f"""
    **Projetado pela Mediana ({mediana_taxa:+.2f}%):**  
    <span style="font-size:1.3rem; font-weight:bold; color:#10b981;">{pop_proj_mediana:,d} hab</span>  
    *(+{pop_proj_mediana - pop_inicial:,d} hab)*
    
    **Projetado pela Média ({media_taxa:+.2f}%):**  
    <span style="font-size:1.3rem; font-weight:bold; color:#3b82f6;">{pop_proj_media:,d} hab</span>  
    *(+{pop_proj_media - pop_inicial:,d} hab)*
    """.replace(",", "."), unsafe_allow_html=True)

with sim_col3:
    # Gráfico da Projeção ao Longo do Tempo
    anos = np.arange(0, anos_projecao + 1)
    curva_mediana = [pop_inicial * ((1 + r_mediana) ** t) for t in anos]
    curva_media = [pop_inicial * ((1 + r_media) ** t) for t in anos]
    
    df_curva = pd.DataFrame({
        "Ano": anos,
        "Cenário Mediana (Típico)": curva_mediana,
        "Cenário Média (Inflado)": curva_media
    })
    
    fig_proj = px.line(
        df_curva, 
        x="Ano", 
        y=["Cenário Mediana (Típico)", "Cenário Média (Inflado)"],
        labels={"value": "População Projetada", "variable": "Cenário"},
        color_discrete_map={"Cenário Mediana (Típico)": "#10b981", "Cenário Média (Inflado)": "#3b82f6"}
    )
    fig_proj.update_layout(height=260, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_proj, use_container_width=True)

st.markdown("---")

# --- TABELA DE DADOS INTERATIVA ---
st.subheader("📋 Tabela Amostral de Municípios")
st.markdown(f"Exibindo **{len(df_filtrado)}** municípios de acordo com os filtros definidos na barra lateral.")

df_tabela = df_filtrado.copy()
df_tabela["pop_fmt"] = df_tabela["pop"].apply(lambda x: f"{x:,.0f}".replace(",", "."))
df_tabela["taxa_fmt"] = df_tabela["taxa"].apply(lambda x: f"{x:+.2f}%")
df_tabela["ganho_fmt"] = df_tabela["ganho_absoluto"].apply(lambda x: f"{x:+,.0f}".replace(",", "."))

df_display = df_tabela[[
    "nome", "uf", "regiao", "pop_fmt", "taxa_fmt", "ganho_fmt", "porte"
]].rename(columns={
    "nome": "Município",
    "uf": "UF",
    "regiao": "Região",
    "pop_fmt": "População Base",
    "taxa_fmt": "Taxa Anual (% a.a.)",
    "ganho_fmt": "Ganho Absoluto (+Hab/ano)",
    "porte": "Classificação Porte"
})

st.dataframe(df_display, use_container_width=True, height=350)

# Botão de Download CSV
csv_data = df_filtrado.to_csv(index=False, sep=";", decimal=",").encode("utf-8-sig")
st.download_button(
    label="📥 Baixar Dados Filtrados (CSV)",
    data=csv_data,
    file_name="crescimento_populacional_municipios.csv",
    mime="text/csv"
)

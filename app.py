import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import requests
from io import StringIO

# Estilo CSS para aumentar o visual
st.markdown("""
<style>
    body {
        font-family: Arial, sans-serif;
        color: #FFFFFF;  /* Cor do texto */
    }
    .title {
        font-size: 48px;  /* Tamanho do título */
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 36px;  /* Tamanho dos subtítulos */
        color: #2196F3;
        margin-top: 30px;
    }
    .dataframe {
        font-size: 22px;  /* Tamanho do texto da tabela */
    }
    .stSidebar .stSelectbox,
    .stSidebar .stSlider,
    .stSidebar .stTextInput {
        font-size: 20px;  /* Tamanho das fontes nos filtros */
    }
    .stSidebar .stSlider > div {
        font-size: 18px;  /* Tamanho das fontes no slider */
    }
</style>
""", unsafe_allow_html=True)

# Título da aplicação
st.markdown('<h1 class="title">Análise de Vinhos</h1>', unsafe_allow_html=True)

# Desabilitar avisos de certificado SSL (não recomendado para produção)
requests.packages.urllib3.disable_warnings()

# URL do arquivo CSV no GitHub
url = 'https://raw.githubusercontent.com/alansms/banco_de_dados_vinhos/main/wine.csv'

# Tentar baixar o dataset
try:
    response = requests.get(url, verify=False)
    response.raise_for_status()
    data = response.text
    df = pd.read_csv(StringIO(data))
    st.success("Dados carregados com sucesso.")
except requests.exceptions.RequestException as err:
    st.error(f"Erro na requisição: {err}")

# Remover colunas duplicadas
df = df.loc[:, ~df.columns.duplicated()]

# Manter apenas as colunas relevantes
expected_columns = ['Nome do Vinho', 'Origem', 'Teor Alcoólico', 'Acidez Málica',
                    'Cinzas', 'Alcalinidade das Cinzas', 'Magnésio', 'Fenóis Totais',
                    'Flavonoides']

available_columns = [col for col in expected_columns if col in df.columns]
df = df[available_columns]

# Exibir o DataFrame para verificação
st.subheader("DataFrame verificado:")
st.dataframe(df.style.set_table_attributes('class="dataframe"').set_properties(**{'font-size': '22px'}))

# Definindo colunas numéricas disponíveis
numeric_columns = ['Teor Alcoólico', 'Acidez Málica', 'Cinzas', 'Alcalinidade das Cinzas',
                   'Magnésio', 'Fenóis Totais', 'Flavonoides']

# Converter as colunas numéricas
for col in numeric_columns:
    if col in df.columns:  # Verifica se a coluna está disponível
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Remover linhas com valores nulos
df.dropna(subset=numeric_columns, inplace=True)

# Filtros na barra lateral
st.sidebar.title("Filtros")
localidade_selecionada = st.sidebar.selectbox("Selecione a Localidade:", df['Origem'].unique())
nome_vinho_selecionado = st.sidebar.text_input("Filtrar pelo Nome do Vinho:")
alcohol_min = st.sidebar.slider("Álcool Mínimo:", min_value=float(df['Teor Alcoólico'].min()),
                                max_value=float(df['Teor Alcoólico'].max()),
                                value=float(df['Teor Alcoólico'].min()))
alcohol_max = st.sidebar.slider("Álcool Máximo:", min_value=float(df['Teor Alcoólico'].min()),
                                max_value=float(df['Teor Alcoólico'].max()),
                                value=float(df['Teor Alcoólico'].max()))

# Aplicar filtros ao DataFrame
df_filtrado = df[
    (df['Origem'] == localidade_selecionada) &
    (df['Nome do Vinho'].str.contains(nome_vinho_selecionado, case=False)) &
    (df['Teor Alcoólico'] >= alcohol_min) &
    (df['Teor Alcoólico'] <= alcohol_max)
    ]
st.subheader("Dados Filtrados")
st.dataframe(df_filtrado.style.set_table_attributes('class="dataframe"').set_properties(**{'font-size': '22px'}))

# Adicionar filtro para seleção de gráfico
st.sidebar.subheader("Selecione um Gráfico para Visualizar")
grafico_selecionado = st.sidebar.selectbox("Escolha o Gráfico:", ["Distribuição do Teor Alcoólico", "Método Elbow", "Silhouette Score", "Visualização PCA"])

# Gráficos adicionais
if grafico_selecionado == "Distribuição do Teor Alcoólico":
    st.subheader("Distribuição do Teor Alcoólico")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Teor Alcoólico'], bins=20, kde=True)
    plt.title('Distribuição do Teor Alcoólico')
    plt.xlabel('Teor Alcoólico')
    plt.ylabel('Frequência')
    st.pyplot(plt)

elif grafico_selecionado == "Método Elbow":
    # Normalização dos dados para clustering
    X = df[numeric_columns]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Determinação do número ideal de clusters usando o método Elbow
    wcss = []
    k_values = range(2, 11)

    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)

    # Plotando o gráfico do Método Elbow
    st.subheader("Método Elbow para Determinar o Número Ideal de Clusters")
    fig1, ax1 = plt.subplots(figsize=(12, 8))
    ax1.plot(k_values, wcss, 'bo-')
    ax1.set_xlabel('Número de Clusters (k)', fontsize=20)
    ax1.set_ylabel('WCSS', fontsize=20)
    ax1.set_title('Método Elbow', fontsize=24)
    st.pyplot(fig1)

elif grafico_selecionado == "Silhouette Score":
    # Normalização dos dados para clustering
    X = df[numeric_columns]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Determinação do número ideal de clusters usando Silhouette Score
    silhouette_scores = []
    k_values = range(2, 11)

    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        score = silhouette_score(X_scaled, kmeans.labels_)
        silhouette_scores.append(score)

    # Plotando o gráfico do Silhouette Score
    st.subheader("Silhouette Score para Diferentes Valores de k")
    fig2, ax2 = plt.subplots(figsize=(12, 8))
    ax2.plot(k_values, silhouette_scores, 'bo-')
    ax2.set_xlabel('Número de Clusters (k)', fontsize=20)
    ax2.set_ylabel('Silhouette Score', fontsize=20)
    ax2.set_title('Silhouette Score', fontsize=24)
    st.pyplot(fig2)

elif grafico_selecionado == "Visualização PCA":
    # Normalização dos dados para clustering
    X = df[numeric_columns]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Ajustar o modelo K-means com o número ideal de clusters
    k_optimal = 3  # Escolhido com base na análise anterior
    kmeans = KMeans(n_clusters=k_optimal, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    df['Cluster'] = labels

    # Gráfico PCA
    st.subheader("Visualização PCA dos Clusters")
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    df['PCA1'], df['PCA2'] = X_pca[:, 0], X_pca[:, 1]

    fig3, ax3 = plt.subplots(figsize=(12, 8))
    sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=df, palette='Set1', s=200, ax=ax3)
    ax3.set_title('Clusters de Vinhos Visualizados no Espaço PCA', fontsize=24)
    ax3.set_xlabel('Componente Principal 1', fontsize=20)
    ax3.set_ylabel('Componente Principal 2', fontsize=20)
    st.pyplot(fig3)
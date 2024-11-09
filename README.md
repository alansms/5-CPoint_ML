# Análise de Agrupamento de Vinhos com K-means

## Teste on-line do código:
[https://4-checkpointmachinelearning-uhbyg2zsazcjwnvhejwylw.streamlit.app](https://4-checkpointmachinelearning-uhbyg2zsazcjwnvhejwylw.streamlit.app)

## Introdução

Este projeto utiliza o algoritmo K-means para agrupar vinhos com base em suas características químicas. O objetivo é identificar vinhos similares, ajudando consumidores e produtores a categorizar seus produtos de maneira eficiente.

## Problema

A dificuldade em classificar vinhos com base em suas propriedades químicas pode ser um desafio tanto para consumidores quanto para produtores. Com a grande variedade de vinhos disponíveis no mercado, é crucial entender como as diferentes características se correlacionam. A análise de agrupamento oferece uma maneira de segmentar vinhos em grupos que compartilham características comuns, facilitando a identificação de padrões e preferências.

## Solução Proposta

Para abordar esse problema, este projeto utiliza o algoritmo K-means, uma técnica de aprendizado não supervisionado, para agrupar vinhos com características semelhantes. Os dados são analisados e visualizados, permitindo que tanto os produtores quanto os consumidores identifiquem rapidamente quais vinhos são mais adequados a seus gostos ou necessidades.

A solução inclui o uso de várias variáveis disponíveis na base de dados, como:
- Teor Alcoólico
- Acidez Málica
- Cinzas
- Alcalinidade das Cinzas
- Magnésio
- Fenóis Totais
- Flavonoides

O processo começa com o pré-processamento dos dados, seguido pelo ajuste do K-means e pela análise dos grupos formados. O uso do método Elbow e Silhouette Score ajuda a determinar o número ideal de clusters, proporcionando uma análise robusta.

## Visualização Gráfica com Streamlit

Para tornar a análise interativa e acessível, utilizamos o Streamlit, uma poderosa biblioteca que permite criar interfaces web de maneira rápida e fácil. Com o Streamlit, o usuário pode interagir com os dados através de filtros, como seleção de localidade e faixa de teor alcoólico, além de visualizar gráficos que mostram a distribuição de características, como:
- Distribuição do Teor Alcoólico
- Método Elbow para determinar o número ideal de clusters
- Silhouette Score para avaliação da qualidade do agrupamento
- Visualização PCA dos clusters

A interface do usuário é intuitiva, permitindo que qualquer pessoa, mesmo sem um profundo conhecimento em ciência de dados, compreenda facilmente as análises realizadas.

## Recursos Utilizados

- **Python**: Linguagem de programação utilizada.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Scikit-learn**: Biblioteca para aprendizado de máquina, utilizada para o algoritmo K-means.
- **Matplotlib e Seaborn**: Bibliotecas para visualização de dados.
- **Streamlit**: Biblioteca para criar a interface do usuário do aplicativo web.

## Passo a Passo do Projeto

1. **Pré-processamento dos Dados**:
   - Remoção de colunas irrelevantes.
   - Tratamento de dados nulos.
   - Normalização das características químicas.
  
2. **Ajuste do K-means**:
   - Aplicação do algoritmo K-means aos dados normalizados.

3. **Método Elbow e Silhouette Score**:
   - Uso do método Elbow para determinar o número ideal de clusters.
   - Cálculo do Silhouette Score para avaliar a qualidade do agrupamento.

4. **Análise dos Grupos**:
   - Cálculo das características médias dos vinhos em cada grupo.
   - Identificação do grupo com maior teor alcoólico e o grupo com maior acidez.

## Gráficos

A aplicação inclui os seguintes gráficos:
- **Distribuição do Teor Alcoólico**
- **Método Elbow**
- **Silhouette Score**
- **Visualização PCA dos Clusters**

## Comentários e Justificativas

O código está comentado em detalhes para explicar cada passo do processo. As funções utilizadas foram escolhidas com base na eficácia em realizar as tarefas necessárias e são amplamente reconhecidas na literatura sobre aprendizado de máquina.

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/alansms/5-CPoint_ML
## Como Executar o Projeto

	1.	Clone o repositório:
https://github.com/alansms/5-CPoint_ML

	2.	Instale as dependências:
pip install -r requirements.txt

	3.	Execute o script:
streamlit run app.py

4.	Acesse o aplicativo no seu navegador.

## Conclusão

Esse projeto proporciona uma análise visual e quantitativa dos vinhos com base em suas propriedades químicas. Através do agrupamento K-means, podemos entender melhor as semelhanças e diferenças entre os vinhos, oferecendo insights valiosos tanto para consumidores quanto para produtores.



# Código
```python

!pip install pandas streamlit matplotlib seaborn scikit-learn requests
# Importação de Bibliotecas
# Importação das bibliotecas necessárias para o projeto.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import requests
from io import StringIO

# URL do arquivo CSV no GitHub
url = 'https://raw.githubusercontent.com/alansms/banco_de_dados_vinhos/main/wine.csv'

# Tentar baixar o dataset
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.text
    df = pd.read_csv(StringIO(data))
    print("Dados carregados com sucesso.")
except requests.exceptions.RequestException as err:
    print(f"Erro na requisição: {err}")

# Remover colunas duplicadas
df = df.loc[:, ~df.columns.duplicated()]

# Manter apenas as colunas relevantes
expected_columns = ['Nome do Vinho', 'Origem', 'Teor Alcoólico', 'Acidez Málica',
                    'Cinzas', 'Alcalinidade das Cinzas', 'Magnésio', 'Fenóis Totais',
                    'Flavonoides']

available_columns = [col for col in expected_columns if col in df.columns]
df = df[available_columns]

# Exibir o DataFrame para verificação
print("DataFrame verificado:")
df.head()

# Converter as colunas numéricas
numeric_columns = ['Teor Alcoólico', 'Acidez Málica', 'Cinzas', 'Alcalinidade das Cinzas',
                   'Magnésio', 'Fenóis Totais', 'Flavonoides']

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remover linhas com valores nulos
df.dropna(subset=numeric_columns, inplace=True)


# Exibir estatísticas descritivas
print(df.describe())

# Visualização da distribuição de uma das variáveis
sns.histplot(df['Teor Alcoólico'], bins=20)
plt.title('Distribuição do Teor Alcoólico')
plt.xlabel('Teor Alcoólico')
plt.ylabel('Frequência')
plt.show()


# Normalização dos dados para clustering
X = df[numeric_columns]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determinação do número ideal de clusters usando o método Elbow
wcss = []
silhouette_scores = []
k_values = range(2, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
    score = silhouette_score(X_scaled, kmeans.labels_)
    silhouette_scores.append(score)

# Plotando o gráfico do Método Elbow
plt.figure(figsize=(10, 5))
plt.plot(k_values, wcss, 'bo-')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('WCSS')
plt.title('Método Elbow')
plt.grid()
plt.show()

# Plotando o gráfico do Silhouette Score
plt.figure(figsize=(10, 5))
plt.plot(k_values, silhouette_scores, 'bo-')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score')
plt.grid()
plt.show()


# Seleção do número ideal de clusters
k_optimal = 3
kmeans = KMeans(n_clusters=k_optimal, random_state=42)
labels = kmeans.fit_predict(X_scaled)

# Adicionar os labels dos clusters ao DataFrame original
df['Cluster'] = labels

# Análise das características médias por cluster
cluster_means = df.groupby('Cluster')[numeric_columns].mean().reset_index()
print("Características médias de cada cluster:")
print(cluster_means)

# Gráfico PCA para visualização dos clusters
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Adicionar as componentes principais ao DataFrame
df['PCA1'] = X_pca[:, 0]
df['PCA2'] = X_pca[:, 1]

# Plotar os clusters no espaço PCA
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=df, palette='Set1', s=100)
plt.title('Clusters de Vinhos Visualizados no Espaço PCA')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.grid()
plt.show()








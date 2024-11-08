## Análise de Agrupamento de Vinhos com K-means
### Teste on-line do código:
https://4-checkpointmachinelearning-uhbyg2zsazcjwnvhejwylw.streamlit.app

## Introdução

Este projeto utiliza o algoritmo K-means para agrupar vinhos com base em suas características químicas. O objetivo é identificar vinhos similares, ajudando consumidores e produtores a categorizar seus produtos de maneira eficiente.

Problema

A dificuldade em classificar vinhos com base em suas propriedades químicas pode ser um desafio tanto para consumidores quanto para produtores. Com a grande variedade de vinhos disponíveis no mercado, é crucial entender como as diferentes características se correlacionam. A análise de agrupamento oferece uma maneira de segmentar vinhos em grupos que compartilham características comuns, facilitando a identificação de padrões e preferências.

Solução Proposta

Para abordar esse problema, este projeto utiliza o algoritmo K-means, uma técnica de aprendizado não supervisionado, para agrupar vinhos com características semelhantes. Os dados são analisados e visualizados, permitindo que tanto os produtores quanto os consumidores identifiquem rapidamente quais vinhos são mais adequados a seus gostos ou necessidades.

A solução inclui o uso de várias variáveis disponíveis na base de dados, como:
	•	Teor Alcoólico
	•	Acidez Málica
	•	Cinzas
	•	Alcalinidade das Cinzas
	•	Magnésio
	•	Fenóis Totais
	•	Flavonoides

O processo começa com o pré-processamento dos dados, seguido pelo ajuste do K-means e pela análise dos grupos formados. O uso do método Elbow e Silhouette Score ajuda a determinar o número ideal de clusters, proporcionando uma análise robusta.

Visualização Gráfica com Streamlit

Para tornar a análise interativa e acessível, utilizamos o Streamlit, uma poderosa biblioteca que permite criar interfaces web de maneira rápida e fácil. Com o Streamlit, o usuário pode interagir com os dados através de filtros, como seleção de localidade e faixa de teor alcoólico, além de visualizar gráficos que mostram a distribuição de características, como:
	•	Distribuição do Teor Alcoólico
	•	Método Elbow para determinar o número ideal de clusters
	•	Silhouette Score para avaliação da qualidade do agrupamento
	•	Visualização PCA dos clusters

A interface do usuário é intuitiva, permitindo que qualquer pessoa, mesmo sem um profundo conhecimento em ciência de dados, compreenda facilmente as análises realizadas.

Recursos Utilizados

	•	Python: Linguagem de programação utilizada.
	•	Pandas: Biblioteca para manipulação e análise de dados.
	•	Scikit-learn: Biblioteca para aprendizado de máquina, utilizada para o algoritmo K-means.
	•	Matplotlib e Seaborn: Bibliotecas para visualização de dados.
	•	Streamlit: Biblioteca para criar a interface do usuário do aplicativo web.

Passo a Passo do Projeto

	1.	Pré-processamento dos Dados:
	•	Remoção de colunas irrelevantes.
	•	Tratamento de dados nulos.
	•	Normalização das características químicas.
	2.	Ajuste do K-means:
	•	Aplicação do algoritmo K-means aos dados normalizados.
	3.	Método Elbow e Silhouette Score:
	•	Uso do método Elbow para determinar o número ideal de clusters.
	•	Cálculo do Silhouette Score para avaliar a qualidade do agrupamento.
	4.	Análise dos Grupos:
	•	Cálculo das características médias dos vinhos em cada grupo.
	•	Identificação do grupo com maior teor alcoólico e o grupo com maior acidez.

Gráficos

A aplicação inclui os seguintes gráficos:
	•	Distribuição do Teor Alcoólico:
 	•	Método Elbow:
 	•	Silhouette Score:
  	•	Visualização PCA dos Clusters:
   	•	Visualização PCA dos Clusters:

## Comentários e Justificativas

O código está comentado em detalhes para explicar cada passo do processo. 
As funções utilizadas foram escolhidas com base na eficácia em realizar as tarefas necessárias e são amplamente reconhecidas na literatura sobre aprendizado de máquina.



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







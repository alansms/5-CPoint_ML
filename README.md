## Análise de Agrupamento de Vinhos com K-means

## Introdução

Neste projeto, utilizamos o algoritmo K-means para agrupar vinhos com base em características químicas. O objetivo é identificar vinhos similares e entender como suas características se agrupam, o que pode ser útil para consumidores e produtores que buscam categorizar seus produtos.

Problema e Solução Proposta

O problema que estamos abordando é a dificuldade em classificar vinhos de maneira eficiente com base em suas propriedades. Com a análise de agrupamento, podemos segmentar os vinhos em grupos, ajudando na identificação de padrões e características comuns. A solução proposta envolve o uso do algoritmo K-means, que é uma técnica popular de aprendizado não supervisionado para agrupamento.

## Passo a Passo do Projeto

	1.	Pré-processamento dos Dados:
	•	Remoção de colunas irrelevantes que não contribuem para a análise.
	•	Tratamento de dados nulos para garantir que o modelo seja treinado com dados completos.
	•	Normalização das características para que todas estejam na mesma escala, facilitando a comparação entre elas.
	2.	Ajuste do K-means:
	•	Aplicação do algoritmo K-means aos dados normalizados para agrupar os vinhos em categorias baseadas em suas características químicas.
	3.	Método Elbow e Silhouette Score:
	•	Implementação do método Elbow para determinar o número ideal de grupos (clusters) ao observar a variação interna entre os grupos à medida que o número de clusters aumenta.
	•	Cálculo do Silhouette Score para avaliar a qualidade do agrupamento, permitindo entender quão bem cada vinho se encaixa em seu cluster.
	4.	Análise dos Grupos:
	•	Análise das características médias dos vinhos em cada grupo.
	•	Identificação do grupo com o maior teor alcoólico e o grupo com maior acidez, e comparações das características entre os grupos, como teor alcoólico, acidez, cinzas, etc.

## Comentários e Justificativas

O código está comentado em detalhes para explicar cada passo do processo. 
As funções utilizadas foram escolhidas com base na eficácia em realizar as tarefas necessárias e são amplamente reconhecidas na literatura sobre aprendizado de máquina.



## Como Executar o Projeto

	1.	Clone o repositório:
git clone https://github.com/seu_usuario/seu_repositorio.git

	2.	Instale as dependências:
pip install -r requirements.txt

	3.	Execute o script:
streamlit run app.py

4.	Acesse o aplicativo no seu navegador.

## Conclusão

Esse projeto proporciona uma análise visual e quantitativa dos vinhos com base em suas propriedades químicas. Através do agrupamento K-means, podemos entender melhor as semelhanças e diferenças entre os vinhos, oferecendo insights valiosos tanto para consumidores quanto para produtores.







# Olá, me chamo Kauã e...
|
|
V
Desenvolvi uma aplicação simples, gostaria de demonstrar a lógica de classificação de um algoritmo de classificação simples, baseado em entradas e saídas. A ideia é analisar o comportamento do usuário (o que ele curte e com quem compartilha) e recomendar conteúdo (em formato mock). Trata-se de uma biblioteca (library) que simula um algoritmo de recomendação, sendo um mock, mas ótimo para estudo e treino da linguagem.


# Class recommend
Tudo começa com a class recommend. Nela estão contidas os métodos de análise e recomendação. O algoritmo de recomendação se baseia em ponteiros. o algoritmo necessita que history.content e content tenhos 10 chaves com valor. cada valor das chaves contém um item, que será comparado com outros valores da chave. Se forem iguais, o contador incrementará + 1, logo, será possível verificar o grau de similaridade entre um conteúdo e outro
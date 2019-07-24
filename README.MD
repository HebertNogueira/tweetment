# tweetment
> Captura de Tweets e análise sentimental

![LOGO-TWEETMENT](https://github.com/HebertNogueira/tweetment/raw/master/static/img/bg-logo-top.jpg)

## Descrição

Captura de tweets únicos (excluídos da capturas os RTs) do termo #1 nos trending topics com a biblioteca __Tweepy__.

Todos os tweets e resultados da análise são salvos no __MongoDB__ através da biblioteca __PyMongo__, neste caso pode-se usar um BD local, ou, em nuvem com o __MongoDB Atlas__.

A análise sentimental é feita com a biblioteca __Textblob__, e, como a biblioteca __Textblob__ faz análise apenas de termos em inglês, é feita uma tradução para o inglês com a biblioteca __Googletrans__.

O resultado da análise pode ser visto no terminal após a execução, ou, através do navegador utilizando o __Flask__.

Para o resultado no navegador há um gráfico do resultado da análise produzido com o __Matplotlib__.
# tweetment
> Captura de Tweets e análise sentimental



## Descrição

Captura de tweets unicos (excluidos da capturas os RTs) do termo #1 nos trending topics com a biblioteca __Tweepy__.

Todos os tweets e resutados da analise sao salvos no __MongoDB__ atraves da biblioteca __PyMongo__, neste caso pode-se usar um BD local, ou, em nuvem com o __MongoDB Atlas__.

A analise sentimental e efeita com a biblioteca __Textblob__, e, como a biblioteca __Textblob__ faz analise apenas de termos em ingles, e feita uma traducao para o ingles com a biblioteca __Googletrans__.

O resultado da analse pode ser visto no terminal apos a execucao, ou, atraves do navegador utilizando o __Flask__.

Para o resultado no navegador ha um grafico do resultado da analise produzido com o __Matplotlib__.

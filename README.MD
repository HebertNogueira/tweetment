# tweetment
> Captura de Tweets e análise sentimental

![LOGO-TWEETMENT](https://github.com/HebertNogueira/tweetment/raw/master/static/img/bg-logo-top.jpg)

## Descrição

Captura de tweets únicos (excluídos da capturas os RTs) do termo #1 nos trending topics com a biblioteca __Tweepy__.

Todos os tweets e resultados da análise são salvos no __MongoDB__ através da biblioteca __PyMongo__, neste caso pode-se usar um BD local, ou, em nuvem com o __MongoDB Atlas__.

A análise sentimental é feita com a biblioteca __Textblob__, e, como a biblioteca __Textblob__ faz análise apenas de termos em inglês, é feita uma tradução para o inglês com a biblioteca __Googletrans__.

O resultado da análise pode ser visto no terminal após a execução, ou, através do navegador utilizando o __Flask__.

Para o resultado no navegador há um gráfico do resultado da análise produzido com o __Matplotlib__.

## REQUISITOS

* Python 3+
* MongoDB


### Pacotes Necessários
- [x] pymongo
- [x] numpy
- [x] tweepy
- [x] matplotlib
- [x] textblob
- [x] googletrans
- [x] flask
- [ ] dnspython - Opcional, caso for usar o MongoDB Atlas, instale.

## ACESSO A API DO TWITTER

Para a ferramenta funcionar corretamente é necessário ter as chaves de acesso a API do __Twitter__, para isto, faça um cadastro em __developer.twitter.com__ e requisite-as, são quatro chaves:

* consumer_key
* consumer_secret
* access_token
* access_token_secret

Coloque-as no arquivo __tweepy_auth.py__.


## EXECUÇÃO

Para iniciar o processo de captura e análise, é necessário chamar o arquivo __ignite.py__ no terminal, este arquivo aceita dois parâmetros via linha de comando:

* __new__ : Para a primeira execucao
* __INT__ : Qualquer número inteiro, para indicar quantos tweets serão captados, se não for indicado será usado o valor padrão __200__

Obrigatoriamente o __new__ deve ser o primeiro, caso queira indicar a quantidade de tweets na primeira execução.

#### Exemplos

* para a primeira execucao 

```
python3 ignite.py new
```
ou
```
python3 ignite.py new 35
```


* Demais execucoes:

```
python3 ignite.py
```
ou
```
python3 ignite.py 100
```

## VISUALIZACAO

Navegue até a pasta do projeto e execute o arquivo __index.py__:

```
python3 index.py
```

Sera iniciado um servidor web local com o __Flask__ no endereco:

http://127.0.0.1


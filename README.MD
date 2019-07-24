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

### Pacotes necessarios
- [x] pymongo
- [x] numpy
- [x] tweepy
- [x] matplotlib
- [x] textblob
- [x] googletrans
- [x] flask
- [ ] dnspython - Opcional, caso for usar o MongoDB Atlas, instale.


## EXECUCAO

1. Para iniciar o processo de captura e analise, e necessario chamar o arquivo __ignite.py__ no terminal, este arquivo aceita dois parametros via linha de comando:

* __new__ : Para a primeira execucao
* __INT__ : Qualquer numero inteiro, para indicar quantos tweets serao captados, se nao for indicado sera usado o valor padrao __200__

Obrigatoriamente o __new__ deve ser o primeiro, caso queira indicar a quantidade de tweets na primeira execucao.

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

Navegue ate a pasta do projeto e execute o arquivo index.py:

```
python3 index.py
```

Sera iniciado um servidor web local com o __Flask__ no endereco:

http://127.0.0.1


from textblob import TextBlob as tb
from trendings import Trendings as tt
from googletrans import Translator
from connect_mongo import ConnectMongo as cm
from datetime import datetime
import re
import time

class TextblobTrendings():


	def sentimentCheck(now,trending):

		# Configurando conexao do MongoDB
		client = cm.connectMongo()
		db = client.twitterCollection

		#Declarando variaveis
		translator = Translator()
		polarity_result = {}
		tweet_list = {}
		count = 0
		polarityNegative = 0
		PolarityPositive = 0

		#Iniciando aalise de sentimentos
		for tweet in db.tweets.find():

			#remover caracteres especiais
			tweet_clean = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ:., ]', '', tweet['text'])

			#Traduzindo para ingles e efetuando analise
			tweet_list[count] = translator.translate(tweet_clean, dest='en').text
			analysis = tb(tweet_list[count])
			polarity_result[count] = analysis.sentiment.polarity

			# Printando tweet e resultado da analise no terminal
			print('Tweet => ' + tweet_list[count])
			print('=========> ' + str(len(tweet_list)) + ' ==> '+ str(polarity_result[count]))

			# Salvando polaridade no tweet ou deletando se invalido para calculo
			if polarity_result[count] <= 1 and polarity_result[count] >= -1 and polarity_result[count] != 0:
				db.tweets.update({'_id':tweet['_id']},{'$set':{'polarity':polarity_result[count]}})
				print('PARCIAL: ' + str(sum(polarity_result.values())))

			else:
				db.tweets.delete_many({'_id':tweet['_id']})
				del(polarity_result[count])

			# Pause na traducao, para nao ser bloqueado pelo Google
			if count%2==0 and count !=0:
				print('Dormindo 2 segundos')
				time.sleep(2)
			if count%10==0 and count !=0:
				print('Dormindo 10 segundos')
				time.sleep(10)
			count+=1

		# Calculando e arrdondando polaridade media em 2 casas decimais
		if (int(sum(polarity_result.values()) > 0)):
			polarityAverage = round(sum(polarity_result.values())/len(polarity_result), 2)
		else:
			polarityAverage = 0
			
		print('## Total Feelings: ' + str(len(polarity_result.values())) + ' ==> Average: ' + str(polarityAverage))

		# Salvando resultado da analise
		tt.updateTrending(now,trending,polarityAverage)

		# retornando media no metodo
		return polarityAverage
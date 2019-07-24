from trendings import Trendings as tt
from catch_trendings import CatchTrendings as ct
from datetime import datetime

class Initial():
	def doit():

		# Salvando data para renomear BD apos analise.
		dt = datetime.now()
		now = str(dt.day) + '_' + str(dt.month) + '_' + str(dt.year) + '_' + str(dt.hour) + '_' + str(dt.minute) + '_' + str(dt.second)

		#Pega os TTs
		tt.trendingCheck(now)

		#pega a posicao 1 dos TTs
		list_tt = tt.listTrending()

		# Captura os Tweets referente a posicao 1 dos TTs
		# Efetua analise sentimental
		# Gera imagem do gauge referente a media dos resultados da analise
		catch_tweets = ct.catchTrendings(list_tt, now)

	doit()
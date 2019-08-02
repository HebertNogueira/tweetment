from trendings import Trendings as tt
from catch_trendings import CatchTrendings as ct
from datetime import datetime

class Initial():
	def doit():

		# Salvando data para renomear BD apos analise.
		now = str(format(datetime.now(), "%d_%m_%Y_%H_%M_%S"))

		#Pega os TTs
		tt.trendingCheck(now)

		#pega a posicao 1 dos TTs
		list_tt = tt.listTrending()

		# Captura os Tweets referente a posicao 1 dos TTs
		# Efetua analise sentimental
		# Gera imagem do gauge referente a media dos resultados da analise
		catch_tweets = ct.catchTrendings(list_tt, now)

	doit()
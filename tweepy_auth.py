import tweepy

class TweepyAuth():
	
	def tweepyAuth():

		# Keys para consumo da API do Twitter
		# https://developer.twitter.com
		# altere o  < adicione aqui > pelos valores entregue pelo Twitter
		consumer_key = " < adicione aqui > "
		consumer_secret = " < adicione aqui > "
		access_token = " < adicione aqui > "
		access_token_secret = " < adicione aqui > "

		# Configurando Handler
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		return auth
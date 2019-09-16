from flask import Flask, render_template, redirect, url_for
from connect_mongo import ConnectMongo as cm
from bson.objectid import ObjectId
from bson.json_util import dumps
import os

app = Flask(__name__)

@app.route('/trending/<string:ttd>', methods=['GET'])
def catchTrendigParams(ttd):
	client = cm.connectMongo()
	db = client.trendingsDisplay
	result = db.trendingTopicsDisplay.find({'_id': ObjectId(ttd)})
	return  dumps(result)

@app.route('/')
def index():
	result = catch_tt()
	return render_template('index.html', result=result)

def catch_tt():
	client = cm.connectMongo()
	db = client.trendingsDisplay
	count = 0
	response={}

	for trend_return in db.trendingTopicsDisplay.find():
		response[count] = trend_return
		count+=1
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True,port=80)

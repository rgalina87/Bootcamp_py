from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

api_key = 'd18cca8b-bd8a-46e7-8741-5b385e8f23b1'

def get_latest_for_id(coin_id):
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
	parameters ={
		  'convert':'USD',
		  'id' : coin_id
		}
	headers = {
	 'Accepts': 'application/json',
	 'X-CMC_PRO_API_KEY': api_key,
	}
	session = Session()
	session.headers.update(headers)
	try:
		response = session.get(url, params=parameters)
		data = json.loads(response.text)
		return data
	except (ConnectionError, Timeout, TooManyRedirects) as e:
		return e

def get_latest_for_all():
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
	parameters = {
		'start':'1',
		'limit':'5000',
		'convert':'USD'
		}
	headers = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': api_key,
	}
	session = Session()
	session.headers.update(headers)
	try:
		response = session.get(url, params=parameters)
		data = json.loads(response.text)
		return data
	except (ConnectionError, Timeout, TooManyRedirects) as e:
		return e

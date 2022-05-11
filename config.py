from dotenv import load_dotenv
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

API_KEY = environ.get('API_KEY')
TOKEN = environ.get('TOKEN')



currencies_list = ['RUB', 'UAH', 'AUD', 'EUR', 'BTC', 'ETH', 'LTC', 'CZK', 'XLM', 'BNB']
currencies_list.sort()
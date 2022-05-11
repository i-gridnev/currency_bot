import requests
from config import API_KEY, currencies_list

def format_data(data):
  result = {}
  for item in data:
    result[item['asset_id_quote']] = round(item['rate'], 2)
  return {key: value for key, value in sorted(result.items())}


def pull_in_base(currencies: list) -> None:
  # base currency USD!!!

  currencies_ = currencies.copy()
  currencies_str = ','.join(currencies_)

  url = f'http://rest.coinapi.io/v1/exchangerate/USD?invert=false&filter_asset_id={currencies_str}&apikey={API_KEY}'
  data = requests.get(url).json()['rates']
  data = format_data(data)

  return data

print(pull_in_base(currencies_list))

# test_data = [
#     {
#       "time": "2022-05-05T13:49:35.4000000Z",
#       "asset_id_quote": "AUD",
#       "rate": 1.395633270711120676837215898
#     },
#     {
#       "time": "2022-05-05T13:49:35.4000000Z",
#       "asset_id_quote": "BTC",
#       "rate": 0.0000255476718822771662110174
#     },
#     {
#       "time": "2022-05-05T13:49:35.4000000Z",
#       "asset_id_quote": "RUB",
#       "rate": 65.824989593253870552684771733
#     },
#     {
#       "time": "2022-05-05T13:49:35.4000000Z",
#       "asset_id_quote": "UAH",
#       "rate": 32.752425807099640082835277422
#     },
#     {
#         "time": "2022-05-05T13:49:35.4000000Z",
#         "asset_id_quote": "CNY",
#         "rate": 0.752425807099640082835277422
#     }
#   ]

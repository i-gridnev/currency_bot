import requests
from database import insert

API_KEY = '4FA548D3-89FF-45AF-8C4F-D618B1842BA2'

test_data = [
    {
      "time": "2022-05-05T13:49:35.4000000Z",
      "asset_id_quote": "AUD",
      "rate": 1.395633270711120676837215898
    },
    {
      "time": "2022-05-05T13:49:35.4000000Z",
      "asset_id_quote": "BTC",
      "rate": 0.0000255476718822771662110174
    },
    {
      "time": "2022-05-05T13:49:35.4000000Z",
      "asset_id_quote": "RUB",
      "rate": 65.824989593253870552684771733
    },
    {
      "time": "2022-05-05T13:49:35.4000000Z",
      "asset_id_quote": "UAH",
      "rate": 32.752425807099640082835277422
    },
    {
        "time": "2022-05-05T13:49:35.4000000Z",
        "asset_id_quote": "CNY",
        "rate": 0.752425807099640082835277422
    }
  ]

insert(test_data)

def get_data(url: str) -> dict:
    return requests.get(url).json()['rates']

def show_currency(base_currency: str, currencies: list, base_num: int = 1) -> str:
    currencies_ = currencies.copy()
    if base_currency in currencies_:
        currencies_.remove(base_currency)
    currencies_str = ','.join(currencies_)

    data = get_data(
        f'http://rest.coinapi.io/v1/exchangerate/{base_currency}?invert=false&filter_asset_id={currencies_str}&apikey={API_KEY}')

    res = f'{base_num} {base_currency}:\n'
    for curr in currencies_:
        value = round(data[currencies_.index(curr)]['rate'], 2)*base_num
        res += f'\n{data[currencies_.index(curr)]["asset_id_quote"]} = {value}'

    return res
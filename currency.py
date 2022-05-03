import requests, re

API_KEY = '4FA548D3-89FF-45AF-8C4F-D618B1842BA2'


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

# rule = '\d\s[A-Z, a-z]{3}'
#
# text = '25 usd'
# currencies_list = ['USD', 'RUB', 'UAH', 'AUD', 'EUR']
# print(bool(re.search(rule, text)))
#
# if bool(re.search(rule, text)):
#     base = ''.join(text.split()[1:])
#     # print(show_currency(base.upper(), currencies_list, int(text[0])))
#     print(int(''.join(text.split()[:1])))
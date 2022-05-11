import sqlite3
from config import currencies_list

DATABASE = 'currencies.db'
TABLE = 'currencies'


def init_table():
    columns = f'CREATE TABLE IF NOT EXISTS {TABLE} (ID INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT'
    for item in currencies_list:
        columns += f', {item} REAL'
    columns += ');'

    with sqlite3.connect(DATABASE) as db:
        db.execute(columns)

init_table()

# def insert(data: list):
#     with sqlite3.connect(DATABASE) as db:
#         query = f'INSERT INTO {TABLE} (id, date'
#         for item in currencies_list:
#             query += f', {item}'
#         query += ') VALUES (NULL, ?'
#         for item in range(len(currencies_list)):
#             query += ', ?'
#         query += ');'
    
#         temp = {}
#         for item in data:
#             temp[]
        


# def insert(data: list):
#     with sqlite3.connect(DATABASE) as db:
#         v = {}
#         for item in data:
#             v[item['asset_id_quote']] = round(item['rate'], 2)

#         query = f"INSERT INTO {TABLE} (id, date, UAH, RUB, AUD, CNY, BTC) VALUES (NULL, ?, ?, ?, ?, ?, ?);"
#         db.execute(query, (date, v['UAH'], v['RUB'],
#                    v['AUD'], v['CNY'], v['BTC']))

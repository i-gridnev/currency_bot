import sqlite3
from datetime import datetime

DATABASE = 'currencies.db'
TABLE = 'currencies'


def init_table():
    with sqlite3.connect(DATABASE) as db:
        db.execute(f"CREATE TABLE IF NOT EXISTS {TABLE}(ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                   f"date TEXT, UAH REAL, RUB REAL, AUD REAL, CNY REAL, BTC REAL);")


def insert(data: list):
    with sqlite3.connect(DATABASE) as db:
        date = datetime.now().strftime("%H:%M:%S")
        v = {}
        for item in data:
            v[item['asset_id_quote']] = round(item['rate'], 2)

        query = f"INSERT INTO {TABLE} (id, date, UAH, RUB, AUD, CNY, BTC) VALUES (NULL, ?, ?, ?, ?, ?, ?);"
        db.execute(query, (date, v['UAH'], v['RUB'], v['AUD'], v['CNY'], v['BTC']))

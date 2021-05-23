import requests

req=requests.get('https://min-api.cryptocompare.com/data/v2/histohour', params={
       'fsym': "BTC",     # 仮想通貨のシンボル
       'tsym': "JPY",     # ペアの通貨のシンボル
       'limit': 2000,     # レコードの取得数、最大2000
       'e': "bitFlyerFX", # 取引所
       'toTs': -1       # 取得したいデータの基準となるタイムスタンプ(unixtime)
       })

print(req.content)
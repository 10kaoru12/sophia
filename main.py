import numpy as np
import pip._vendor.requests as requests
 
response = requests.get("https://api.bitflyer.jp/v1/ticker/")
print(response.json().get("best_bid"))
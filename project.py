import pandas as pd
import requests
from datetime import datetime

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

df = df[
    [
        "id",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]
]

df.rename(
    columns={
        "id": "coin_name",
        "symbol": "coin_symbol",
        "current_price": "price_usd",
        "market_cap": "market_cap_usd",
        "total_volume": "volume_24h",
        "price_change_percentage_24h": "price_change_24h_pct"
    },
    inplace=True
)

df["timestamp"] = datetime.now()

print(df.head(20))

filename = "project.csv"
df.to_csv(filename, index=False)

print("File saved:", filename)

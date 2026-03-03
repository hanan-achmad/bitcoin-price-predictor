import pandas as pd
import requests
from datetime import datetime

def fetch_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["bitcoin"]["usd"]

def main():
    today = datetime.today().strftime("%Y-%m-%d")
    price = fetch_btc_price()

    df = pd.DataFrame({
        "date": [today],
        "btc_price_usd": [price]
    })

    df.to_csv("data/prediction_results/daily_predictions.csv", index=False)
    print("BTC price saved successfully.")

if __name__ == "__main__":
    main()

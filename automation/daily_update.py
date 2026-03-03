import pandas as pd
from datetime import datetime

def main():
    today = datetime.today().strftime("%Y-%m-%d")

    # Dummy prediction
    prediction = 0.01

    df = pd.DataFrame({
        "date": [today],
        "prediction": [prediction]
    })

    df.to_csv("data/prediction_results/daily_predictions.csv", index=False)
    print("Prediction saved successfully.")

if __name__ == "__main__":
    main()

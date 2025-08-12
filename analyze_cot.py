# analyze_cot.py
import pandas as pd

def analyze_trends(df):
    trends = []
    for pair in df['Pair'].unique():
        pair_df = df[df['Pair'] == pair].sort_values("Date")
        if len(pair_df) < 2:
            continue
        latest = pair_df.iloc[-1]['NonComm_Net']
        prev = pair_df.iloc[-2]['NonComm_Net']
        change = latest - prev
        trend = "Bullish" if change > 0 else "Bearish" if change < 0 else "Neutral"
        trends.append({"Pair": pair, "Latest": latest, "Change": change, "Trend": trend})
    return pd.DataFrame(trends)

if __name__ == "__main__":
    df = pd.read_csv("cot_sample.csv")
    print(analyze_trends(df))

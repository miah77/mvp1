import os
import pandas as pd
import streamlit as st

# Get CSV path relative to this script
BASE_DIR = os.path.dirname(__file__)
csv_path = os.path.join(BASE_DIR, "cot_sample.csv")

# Load data
df = pd.read_csv(csv_path)

st.title("Commitment of Traders - Sample Dashboard")
st.write("Sample COT data preview:")
st.dataframe(df)

# Example: Trend by currency
currency = st.selectbox("Select currency:", df['Currency'].unique())
filtered = df[df['Currency'] == currency]
st.line_chart(filtered.set_index("Date")['Net_Positions'])

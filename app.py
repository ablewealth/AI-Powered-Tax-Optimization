import streamlit as st
import pandas as pd
from utma_tax_optimizer.utma_optimizer import optimize_utma

st.title("UTMA/UGMA Tax Optimization System - 2025")

uploaded_file = st.file_uploader("Upload your accounts CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:", df.head())
    results = []
    for idx, row in df.iterrows():
        account_data = {
            'year': 2025,
            'positions': eval(row['positions']),
            'ytd_income': float(row['ytd_income'])
        }
        plan = optimize_utma(account_data)
        results.append({
            'account_id': row['account_id'],
            'optimization_plan': plan
        })
    st.write("Optimization Results:")
    for result in results:
        st.subheader(f"Account: {result['account_id']}")
        st.json(result['optimization_plan'])

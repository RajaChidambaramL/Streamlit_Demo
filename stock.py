import streamlit as st
import yfinance as yt

ticker_symbol = st.text_input("Type your symbol", value = "AAPL")


ticker_data = yt.Ticker(ticker_symbol)
# ticker_df = ticker_data.history(period = "1mo")

# st.dataframe(ticker_df, use_container_width=True)
#
# ticker_df = ticker_data.history(period = "1d", start = "2022-11-06", end = "2023-11-05")
# st.dataframe(ticker_df, use_container_width=True)

d1,d2 = st.columns(2)

with d1:
    start = st.date_input("Start Date")
with d2:
    end = st.date_input("End Date")

ticker_df = ticker_data.history(period = "1d", start = start, end = end)

col1,col2 = st.columns(2)

with col1:
    st.line_chart(ticker_df, y="Close")
with col2:
    st.line_chart(ticker_df, y="Volume")

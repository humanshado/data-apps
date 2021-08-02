import yfinance as yf
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import graphviz as gv
from PIL import Image

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

number = st.slider("pick a number", 0, 100)
date = st.date_input("Pick a date")

#define the ticker symbol
tickerSymbol = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# display data
st.dataframe(tickerDf)

"""
***
"""

# Open	High	Low	Close	Volume	Dividends	Stock Splits
col1, col2 = st.beta_columns([2, 3])
col1.subheader("Closing Price")
col1.line_chart(tickerDf.Close)

col2.subheader("Volume Price")
col2.line_chart(tickerDf.Volume)

"""
#### California Housing Prices
***
"""

df = pd.read_csv('../databank/housing.csv')
locations = df[['longitude', 'latitude']]

col1, col2 = st.beta_columns([3, 1])
col1.subheader("Map of California")
col1.map(locations)
col2.subheader("Lng & Lat")
col2.dataframe(locations)

"""
***
"""
st.subheader('Daily Routines')
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

"""
***
"""
images = [
    Image.open('images/ring.png'),
    Image.open('images/bracelet.png'),
    Image.open('images/earrings.png'),
    Image.open('images/necklace.png')
  ]
from random import randint
#image = Image.open('images/ring.png')
for i in range(1, 10):
    rn = randint(0,3)
    cols = st.beta_columns(4)
    cols[0].image(images[rn], use_column_width=True)
    cols[1].image(images[rn], use_column_width=True)
    cols[2].image(images[rn], use_column_width=True)
    cols[3].image(images[rn], use_column_width=True)




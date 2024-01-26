#!/usr/bin/python3
from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.graph_objects as go

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

#print(bitcoin_data)
bitcoin_prices = bitcoin_data['prices']
bitcoin_df = pd.DataFrame(bitcoin_prices, columns=['TimeStamp', 'Price'])

bitcoin_df['Date'] = pd.to_datetime(bitcoin_df['TimeStamp'], unit='ms')
print(bitcoin_df)

candlestick_data = bitcoin_df.groupby(bitcoin_df.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x= candlestick_data.index,
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])])
fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date',
        yaxis_title='Price (USD $)', title='Bitcoin Candlestick Chart Over Past 30 Days')

plot(fig, filename='bitcoin_candlestick_graph.html')

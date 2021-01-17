import pandas as pd 
import plotly.graph_objects as go 
from datetime import datetime

file_read = pd.read_csv('data.csv')

chart = go.Figure(data=[go.Candlestick(x=file_read['Date'],
                open = df['Open'],
                high = df['High'],
                low = df['.Low'],
                close = df['Close'])])

chart.show()

# Importing required libraries
import datetime
import yfinance as yf
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)
app.title = "Stock Visualisation"

app.layout = html.Div(children=[
    html.H1("Stock Visualisation Dashboard"),
    html.H4("Please enter the stock name"),
    dcc.Input(id='input', value='AAPL', type='text'),
    html.Div(id='output-graph')
])

@app.callback(
    Output('output-graph', 'children'),
    [Input('input', 'value')]
)
def update_graph(stock_name):
    print(f"Fetching data for: {stock_name}")
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2021, 1, 1)
    try:
        df = yf.download(stock_name, start=start, end=end)
        print("Data fetched successfully")
    except Exception as e:
        print(f"Error fetching data: {e}")
        return html.Div(f"Error fetching data for {stock_name}")

    fig = go.Figure(
        data=[go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close']
        )]
    )
    
    fig.update_layout(title=f'Stock Data for {stock_name}', xaxis_title='Date', yaxis_title='Price')
    
    return dcc.Graph(figure=fig)


if __name__ == '__main__':
    app.run_server(debug=True, port =8051)

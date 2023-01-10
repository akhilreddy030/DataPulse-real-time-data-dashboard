import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
from data_fetcher import get_data

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Real-Time Data Dashboard'),
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # Update every 10 seconds
        n_intervals=0
    )
])

@app.callback(
    dash.dependencies.Output('live-update-graph', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    data = get_data()
    df = pd.DataFrame(data)
    
    trace = go.Scatter(
        x=df['timestamp'],
        y=df['value'],
        mode='lines+markers'
    )
    
    return {
        'data': [trace],
        'layout': go.Layout(
            title='Live Data',
            xaxis=dict(title='Time'),
            yaxis=dict(title='Value')
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)

import dash
import dash.dcc as dcc
import dash.html as html
from dash.dependencies import Input, Output
import requests
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='DuckDB Data in Dash'),

    html.Div(children='''
        A simple example displaying data from DuckDB.
    '''),

    dcc.Graph(
        id='example-graph'
    ),

    dcc.Interval(
        id='interval-component',
        interval=5*1000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(Output('example-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph(n):
    # Fetch data from FastAPI
    response = requests.get("http://127.0.0.1:8000/items")
    data = response.json()

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['id', 'name', ["values"]])

    # Create figure
    figure = {
        'data': [
            {'x': df['id'], 'y': df['name'], 'type': 'bar', 'name': 'Items'},
        ],
        'layout': {
            'title': 'Items from DuckDB'
        }
    }

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)

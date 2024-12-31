import pandas as pd
from dash import Dash, html

app = Dash(__name__)
df = pd.read_csv('../supporting/wordList 2024-10-07.csv', encoding='latin1')

#create a global variable to pass to the callback
message = 'hello world'

app.layout = html.Div([
    html.Button('Click me: 0', id='counter-button')
])

from probe_cb_basic import *

if __name__ == '__main__':
    app.run_server(debug=True)
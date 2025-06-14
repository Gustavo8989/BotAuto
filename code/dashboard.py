import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

def teste():
    app = dash.Dash(__name__) 
    df = pd.DataFrame({
        'x':[1,2,3,4,5],
        'y':[10,11,12,13,14],
        'z':[20,18,16,14,12]
    }) 
    app.layout = html.Div(children=[html.H1(children='Aplicação de teste'),dcc.Graph(id='Grafico teste',figure=px.scatter(df,x='x',y='y',size='z',title="Dashboard teste")
                                                                                      )
                                   ])
    app.run_server(debug=True)



if __name__ == '__main__':
    teste()

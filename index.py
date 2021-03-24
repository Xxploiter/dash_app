import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pickle
# Connect to main app.py file
from app import app
from app import server
import webbrowser
df = px.data.gapminder()




df1 = pd.read_csv('piera')


def pie_c():
    df1 = pd.read_csv('piera')
    positi= df1[df1.rating == 1]
    negati= df1[df1.rating==0]
    pos=len(positi.index)
    neg=len(negati.index)
    fig1 = px.pie(df1, values=(pos,neg), names=['positive','Negative'], color_discrete_sequence=px.colors.sequential.RdBu)
    return fig1


# Connect to your app pages

card_question = dbc.CardGroup(
    [
dbc.Card(
    [
        dbc.CardBody([
            html.H4("Sentiment Analysis", className="card-title"),
            html.P("5 Basics steps that needs to be followed for any machine learning project", className="card-text"),
            dbc.ListGroup(
                [
                    dbc.ListGroupItem("Step-1 Gather data "),
                    dbc.ListGroupItem("Step-2 preprocess your data"),
                    dbc.ListGroupItem("Step-3 Train your machine learning model"),
                    dbc.ListGroupItem("Step-4 Test your model"),
                    dbc.ListGroupItem("Step-5 Improve"),
                ], flush=True)
        ]),
    ], color="warning",
),
dbc.Card(
    [html.H4("Composition of positive reviews and negative reviews", className="card-title",style={'color': 'lumen'}),
     html.Hr(),
 dcc.Graph(figure = pie_c()),
 dbc.ListGroupItem("the data was gathered from scraping the website and following is the pie-chart of the positive and negative reviews"),
 html.P("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", className="card-text")
                            ],outline=False)])        
app.layout = html.Div([dbc.Row([dbc.Col(card_question, width=12),])])
                #dbc.Col(card_graph1, width=6)], justify="around")])

actual_layout=app.layout

from apps import wc,vt
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

def layout_():
    sidebar = dbc.Card([
    dbc.CardBody([
        html.H2("Navigate", className="display-4"),
        html.Hr(),
        html.P(
            "Explore further below", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/", active="exact"),
                dbc.NavLink("Analyze", href="/apps/vt", active="exact"),
                dbc.NavLink("WordCloud", href="/apps/wc", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ]),
    ], color="Gainsboro ", style={"height":"100vh",
                             "width": "16rem", "position":"fixed"}),
    content = html.Div(id="page-content", style={"margin-Right": "16rem"},children=[])
    
    app.layout = dbc.Container([
    dcc.Location(id="url"),
    dbc.Row([
        dbc.Col(sidebar,width=6),
        dbc.Col(content,width=8, style={"margin-left":"16rem"})
        ], className="mb-4"),
    ], fluid=True)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return actual_layout
                
    if pathname == '/apps/vt':
        return vt.create_app_ui()
    if pathname == '/apps/wc':
        return wc.layout
    else:
        return "error"



def main():
    global app
    layout_()
    open_browser()
    app.run_server()

if __name__=='__main__':
    main()
   


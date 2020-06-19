import pickle 

with open('corona_merged.file', 'rb') as f: 
    df = pickle.load(f)

import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import datetime

import pandas as pd


df = df[['message', 'locations', 'time', 'short_date']]
app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    columns=[
            {"name": i, "id": i, "deletable": True, 
            "selectable": True} for i in df.columns
        ],
    data=df.to_dict('records'),
    editable=True,
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    column_selectable="single",
    row_selectable="multi",
    row_deletable=True,
    selected_columns=[],
    selected_rows=[],
    page_action="native",
    page_current= 0,
    page_size= 100,
  #  style_table={
   #     'height': 400,
   # },
    style_data={
        'width': '150px', 
        'minWidth': '150px', 
        'maxWidth': '150px',
        'overflow': 'native',
        'textOverflow': 'ellipsis',
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
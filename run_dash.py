import pickle 
with open('corona_dash', 'rb') as f:   
    corona_dash = pickle.load(f)

import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import datetime

import pandas as pd

corona_dash.head(3)

corona_dash = corona_dash[['Дата', 'День недели', 'Сообщение', 'Тема', 'Геотег',
                           'Негативность сообщения','Позитивность сообщения', 'Нейтральность сообщения']]

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    columns=[
            {"name": i, "id": i, "deletable": True, 
            "selectable": True} for i in corona_dash.columns
        ],
    data=corona_dash.to_dict('records'),
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
        'width': '250px', 
        'minWidth': '250px', 
        'maxWidth': '250px',
        'overflow': 'native',
        'textOverflow': 'ellipsis',
    }
)


if __name__ == '__main__':
    app.run_server(debug=True, port='8887')
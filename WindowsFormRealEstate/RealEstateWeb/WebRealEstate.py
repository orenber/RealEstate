<<<<<<< HEAD
import dash  #(version 1.12.0)
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import pyodbc



# -------------------------------------------------------------------------------------
# Import the cleaned data (importing sql into pandas)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ORENBER-PC\MSSQLSERVER2008;'
                      'Database=RealEstate;'
                      'Trusted_Connection=yes;')


df = pd.read_sql_query('SELECT * FROM purchase', conn)


# Creating an ID column name gives us more interactive capabilities
df['id'] = df['block']
df.set_index('id', inplace=True, drop=False)
print(df.columns)

# -------------------------------------------------------------------------------------
# App layout
app = dash.Dash(__name__, prevent_initial_callbacks=True) # this was introduced in Dash version 1.12.0

# Sorting operators (https://dash.plotly.com/datatable/filtering)
app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
            if i == "iso_alpha3" or i == "year" or i == "id"
            else {"name": i, "id": i, "deletable": True, "selectable": True}
            for i in df.columns
        ],
        data=df.to_dict('records'),  # the contents of the table
        editable=True,              # allow editing of data inside all cells
        filter_action="native",     # allow filtering of data by user ('native') or not ('none')
        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",         # sort across 'multi' or 'single' columns
        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        row_selectable="multi",     # allow users to select 'multi' or 'single' rows
        row_deletable=True,         # choose if user can delete a row (True) or not (False)
        selected_columns=[],        # ids of columns that user selects
        selected_rows=[],           # indices of rows that user selects
        page_action="native",       # all data is passed to the table up-front or not ('none')
        page_current=0,             # page number that user is on
        page_size=6,                # number of rows visible per page
        style_cell={                # ensure adequate header width when text is shorter than cell's text
            'minWidth': 95, 'maxWidth': 95, 'width': 95
        },
        style_cell_conditional=[    # align text columns to left. By default they are aligned to right
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['country', 'iso_alpha3']
        ],
        style_data={                # overflow cells' content into multiple lines
            'whiteSpace': 'normal',
            'height': 'auto'
        }
    ),

    html.Br(),
    html.Br(),
    html.Div(id='bar-container'),
    html.Div(id='choromap-container')

])


# ---------------------- draw  fit data line plot------------------------------
=======
from dash.dependencies import Input,Output
import dash_table
import pandas as pd


#------------------------------------------------
# import data from sql 


# create table  


# set the data into table 


# crate daynamic graf


# creat map



# show the selected data on the map 



>>>>>>> origin/master





<<<<<<< HEAD
# -------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run_server(debug=True)
=======


>>>>>>> origin/master

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

"""
grn = pd.read_excel('CMI TOTAL GRN -AUG 2020.xlsx')
ret = pd.read_excel('SUPPLIER WISE PURCHASE RETURN DETAILS.xlsx')
stk = pd.read_excel('CMI TOTAL STOCK AUG-2020.xlsx')
trn= pd.read_excel('CMI TOTAL TRANSFER -AUG 2020.xlsx')
sc=pd.read_excel('CMI TOTAL S & C -AUG 2020.xlsx')


grn ["GRN Value"] = grn['GRN Value'].astype('int')
sc ["Total"] = sc['Total'].astype('int')
trn ["Accepted Value"] = trn['Accepted Value'].astype('int')
ret["Cost Price"] = ret["Cost Price"].astype('int')
stk['STOCK_VALUE'] = stk['STOCK_VALUE'].astype('int')


trnic=trn.groupby('Item Cat Name')['Accepted Value'].sum()
trnic=trnic.to_frame(name=None)
lst=[]
for i in range(len(trnic)):
    lst.append("Inter Unit Transfer")
trnic.insert(1,"Stock_Status",lst,True)
trnic = trnic.rename(columns={'Accepted Value':'Aggrigate_Values'})


grnic=grn.groupby('Item Category')['GRN Value'].sum()
grnic=pd.DataFrame(grnic, columns = ["Item Category","GRN Value"])
lst=[]
for i in range(len(grnic)):
    lst.append("GRN Value")
grnic.insert(0,"Stock_Status",lst,True)
grnic.head(10)
grnic = grnic.rename(columns={'GRN Value':'Aggrigate_Values'})


scic=sc.groupby('Category')['Total'].sum()

scic=scic.to_frame(name=None)
lst=[]
for i in range(len(scic)):
    lst.append("Sales & Consumption")
scic.insert(0,"Stock_Status",lst,True)
scic.head(10)
scic = scic.rename(columns={'Total':'Aggrigate_Values'})


scic=sc.groupby('Category')['Total'].sum()

scic=scic.to_frame(name=None)
lst=[]
for i in range(len(scic)):
    lst.append("Sales & Consumption")
scic.insert(0,"Stock_Status",lst,True)
scic.head(10)
scic = scic.rename(columns={'Total':'Aggrigate_Values'})


stkic=stk.groupby('Item Category')['STOCK_VALUE'].sum()

stkic=stkic.to_frame(name=None)
lst=[]
for i in range(len(stkic)):
    lst.append("Closing Stock")
stkic.insert(0,"Stock_Status",lst,True)
#print(stkic.head(10))
stkic = stkic.rename(columns={'STOCK_VALUE':'Aggrigate_Values'})


retic=ret.groupby('Item Category')['Cost Price'].sum()


retic=retic.to_frame(name=None)
lst=[]
for i in range(len(retic)):
    lst.append("Returns")
retic.insert(0,"Stock_Status",lst,True)
retic.head(10)
retic = retic.rename(columns={'Cost Price':'Aggrigate_Values'})


result = pd.concat([grnic,scic, stkic,retic,trnic], axis=0, sort=True)
#print(result)


result=result.drop(["Item Category"], axis = 1) 


#result.to_excel("result.xlsx")"""

df = pd.read_excel('result.xlsx')

df = df.rename(columns={'Unnamed: 0':'Item_Category'})

df['Aggrigate_Values'] = df['Aggrigate_Values'].abs()


df1= pd.read_excel('result_1.xlsx')


df1['Aggrigate_Values_SubCat'] = df1['Aggrigate_Values_SubCat'].abs()

df2 = pd.read_excel('result2.xlsx')

#df = pd.read_excel("Aster Pre Final DB.xlsx",encoding="latin1")

 # Create bar chart with drop down list

app = dash.Dash(__name__)
app.layout = html.Div([


    html.Div([
        html.H2("ASTER DM HEAlTHCARE STATISTICS REPORT"),
        html.Img(src="/assets/images.png")
    ],style={'text-align': 'center',
        
            "color" : "#FF0000"

    }, className="banner"),
    
    html.Br(),
    html.Br(),




    html.Div([
        dcc.Dropdown(id='Aster_report',
                     multi=True,
                     clearable=True,
                     value=['Item Sub Category','Total Qty'],
                     placeholder='Select columns',
                     options=[{'label': c, 'value': c}
                              for c in (df1['Item_Category'].unique())])

            ], style={'width': '40%',
              'margin-left': '30%',
              'background-color': '#2EBECD'
    }),
    html.Div([
    dcc.Graph(id='Product_stats',
              config={'displayModeBar': True})

        ],className="six columns",
        style={'margin-left':'10%','margin-top':'1%'}),


    ##########################################

    


    html.Br(),
    html.Br(),
    html.Div([
        dcc.Dropdown(id='Aster_report1',
                     multi=True,
                     clearable=True,
                     value=['Item Sub Category','Total Qty'],
                     placeholder='Select columns',
                     options=[{'label': j, 'value': j}
                              for j in (df['Stock_Status'].unique())])
            ], style={'width': '40%',
              'margin-left': '30%',
              'background-color': '#2EBECD'
    }),
    html.Div([
    dcc.Graph(id='Product_stats1',
              config={'displayModeBar': True})

        ],className="six columns",
        style={'margin-left':'10%','margin-top':'1%'}),


    ##########################################


    html.Br(),
    html.Br(),
    html.Div([
        dcc.Dropdown(id='Aster_report2',
                     multi=True,
                     clearable=True,
                     value=['Item Sub Category','Total Qty'],
                     placeholder='Select columns',
                     options=[{'label': k, 'value': k}
                              for k in (df2['Category'].unique())])
            ], style={'width': '40%',
              'margin-left': '30%',
              'background-color': '#2EBECD'
    }),
    html.Div([
    dcc.Graph(id='Product_stats2',
              config={'displayModeBar': True})

        ],className="six columns",
        style={'margin-left':'10%','margin-top':'1%'})



##########*********************************

    ])

#app.css.append_css({
#    "external_url" : "https://codepen.io/chriddyp/pen/bWLwgP.css"
#    })
@app.callback(Output('Product_stats', 'figure'),
    [Input('Aster_report', 'value')])

def annual_by_country_barchart(Aster_report):



    
    
    return {'data': [go.Bar(x=df1[df1['Item_Category'] == c]['Sub Category'],
                        y=df1[df1['Item_Category'] == c]['Aggrigate_Values_SubCat'],
                        textposition='auto',
                        name=c)
                        for c in Aster_report],

            'layout': go.Layout(
             title='List of Products: ' + ', '.join(Aster_report),

            plot_bgcolor='#EFEFEF',
            paper_bgcolor='#ffffff ',

            font={'family': 'Palatino'},
            width=1050,
            height = 520,
             barmode='group',
             template='seaborn',
             yaxis=dict(
                 title='Inventory Statistics',
                 titlefont_size=18,
                 tickfont_size=14,
             ),
             xaxis=dict(
                 title='Category',
                 titlefont_size=18,
                 tickfont_size=14,

             ),

         )

    }

##########################################################

@app.callback(Output('Product_stats1', 'figure'),
    [Input('Aster_report1', 'value')])

def annual_by_country_barchart(Aster_report1):



    
    
    return {'data': [go.Bar(x=df[df['Stock_Status'] == j]['Item_Category'],
                        y=df[df['Stock_Status'] == j]['Aggrigate_Values'],
                        textposition='auto',
                        name=j)
                        for j in Aster_report1],

            'layout': go.Layout(
             title='Stock consumed and available: ' + ', '.join(Aster_report1),

            plot_bgcolor='#EFEFEF',
            paper_bgcolor='#ffffff ',

            font={'family': 'Palatino'},
            width=1050,
            height = 520,
             barmode='group',
             template='seaborn',
             yaxis=dict(
                 title='Inventory Statistics',
                 titlefont_size=18,
                 tickfont_size=14,
             ),
             xaxis=dict(
                 title='Category',
                 titlefont_size=18,
                 tickfont_size=14,

             ),

         )

    }

####################################################################3


@app.callback(Output('Product_stats2', 'figure'),
    [Input('Aster_report2', 'value')])

def annual_by_country_barchart(Aster_report2):



    
    
    return {'data': [go.Bar(x=df2[df2['Category'] == k]['Doctor Name'],
                        y=df2[df2['Category'] == k]['Total'],
                        textposition='auto',
                        name=k)
                        for k in Aster_report2],

            'layout': go.Layout(
             title='Items consumed by Doctor: ' + ', '.join(Aster_report2),

            plot_bgcolor='#EFEFEF',
            paper_bgcolor='#ffffff ',

            font={'family': 'Palatino'},
            width=1050,
            height = 520,
             barmode='group',
             template='seaborn',
             yaxis=dict(
                 title='Inventory Statistics',
                 titlefont_size=18,
                 tickfont_size=14,
             ),
             xaxis=dict(
                 title='Category',
                 titlefont_size=18,
                 tickfont_size=14,

             ),

         )

    }


if __name__ == '__main__':
    app.run_server(debug=True)
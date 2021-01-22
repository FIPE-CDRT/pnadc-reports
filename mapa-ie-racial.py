# -*- coding: utf-8 -*-
# Preciso de do input fundamental aqui, que é a base com os ie_racial

# To-do: 
#    o título muda toda hora de acordo com a var selecionada, tem que ficar parado
#    cortar só no BR e aumentar o tamanho do grafico com relação ao botao de seleção


import plotly.graph_objects as go
import pandas as pd
import json


# GeoJSON do mapa dos 

with open('input/brazil_geo.json', encoding='utf-8') as response:    
    mapa_estados = json.load(response)




# Create figure
fig = go.Figure()

for sector in ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze']:

    fig.add_trace(go.Choropleth(geojson = mapa_estados,
                                featureidkey = "properties.name",
                                locations = ie_racial['nome'],
                                z = ie_racial[sector].astype(float),
                                colorscale = "Viridis",
                                zmin = -1,
                                zmax = 1))

# Add dropdowns
fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list(
            [dict(label = 'Agricultura, pecu�ria, produ��oo florestal, pesca e aquicultura',
                  method = 'update',
                  args = [{'visible': [True, False, False, False, False, False, False, False, False, False, False]},
                          {'title': 'Agricultura, pecu�ria, produ��oo florestal, pesca e aquicultura',
                           'showlegend':True}]),
             dict(label = 'Ind�stria geral',
                  method = 'update',
                  args = [{'visible': [False, True, False, False, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Ind�tria geral',
                           'showlegend':True}]),
             dict(label = 'Constru��o',
                  method = 'update',
                  args = [{'visible': [False, False, True, False, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Constru��o',
                           'showlegend':True}]),
             dict(label = 'Com�rcio, repara��o de ve�culos automotores e motocicletas',
                  method = 'update',
                  args = [{'visible': [False, False, False, True, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Com�rcio, repara��o de ve�culos automotores e motocicletas',
                           'showlegend':True}]),
             dict(label = 'Transporte, armazenagem e correios�',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, True, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Transporte, armazenagem e correios�',
                           'showlegend':True}]),
             dict(label = 'Alojamento e alimenta��o�',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, True, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Alojamento e alimenta��o�',
                           'showlegend':True}]),
             dict(label = 'Informa��o, comunica��o e atividades financeiras, imobili�rias, profissionais e administrativas',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, True, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Informa��o, comunica��o e atividades financeiras, imobili�rias, profissionais e administrativas',
                           'showlegend':True}]),
             dict(label = 'Administra��o p�blica, defesa e seguridade social',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, True, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Administra��o p�blica, defesa e seguridade social',
                           'showlegend':True}]),
             dict(label = 'Educa��o, sa�de humana e servi�os sociais',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, True, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Educa��o, sa�de humana e servi�os sociais',
                           'showlegend':True}]),
             dict(label = 'Outros Servi�os',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, False, True, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Outros Servi�os',
                           'showlegend':True}]),
             dict(label = 'Servi�os dom�sticos',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, False, False, True]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Servi�os dom�sticos',
                           'showlegend':True}]),
            ])
        )
    ])

fig.update_layout(
    title_text = '͍ndice de Equil�brio Racial',
    geo_scope='south america', 
)

fig.write_html("tmp/ie_racial.html")

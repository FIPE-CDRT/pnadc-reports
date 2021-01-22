# -*- coding: utf-8 -*-
# Preciso de do input fundamental aqui, que Ã© a base com os ie_racial

# To-do: 
#    o tÃ­tulo muda toda hora de acordo com a var selecionada, tem que ficar parado
#    cortar sÃ³ no BR e aumentar o tamanho do grafico com relaÃ§Ã£o ao botao de seleÃ§Ã£o


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
            [dict(label = 'Agricultura, pecuária, produçãoo florestal, pesca e aquicultura',
                  method = 'update',
                  args = [{'visible': [True, False, False, False, False, False, False, False, False, False, False]},
                          {'showlegend':True}]),
             dict(label = 'Indústria geral',
                  method = 'update',
                  args = [{'visible': [False, True, False, False, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
             dict(label = 'Construção',
                  method = 'update',
                  args = [{'visible': [False, False, True, False, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
             dict(label = 'Comércio, reparação de veí­culos automotores e motocicletas',
                  method = 'update',
                  args = [{'visible': [False, False, False, True, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
             dict(label = 'Transporte, armazenagem e correios ',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, True, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
             dict(label = 'Alojamento e alimentação ',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, True, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
             dict(label = 'Informação, comunicação e atividades financeiras, imobiliárias, profissionais e administrativas',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, True, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
             dict(label = 'Administração pública, defesa e seguridade social',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, True, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
             dict(label = 'Educação, saúde humana e serviços sociais',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, True, False, False]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
             dict(label = 'Outros Serviços',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, False, True, False]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
             dict(label = 'Serviços domésticos',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, False, False, True]}, # the index of True aligns with the indices of plot traces
                          {'showlegend':True}]),
            ])
        )
    ])

fig.update_layout(
    title_text = 'Índice de Equilí­brio Racial',
    geo_scope='south america', 
)

fig.write_html("tmp/ie_racial.html")

# -*- coding: utf-8 -*-
# Preciso de do input fundamental aqui, que √© a base com os ie_racial

# To-do: 
#    o t√≠tulo muda toda hora de acordo com a var selecionada, tem que ficar parado
#    cortar s√≥ no BR e aumentar o tamanho do grafico com rela√ß√£o ao botao de sele√ß√£o


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
            [dict(label = 'Agricultura, pecu·ria, produÁ„oo florestal, pesca e aquicultura',
                  method = 'update',
                  args = [{'visible': [True, False, False, False, False, False, False, False, False, False, False]},
                          {'title': 'Agricultura, pecu·ria, produÁ„oo florestal, pesca e aquicultura',
                           'showlegend':True}]),
             dict(label = 'Ind˙stria geral',
                  method = 'update',
                  args = [{'visible': [False, True, False, False, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'IndÌtria geral',
                           'showlegend':True}]),
             dict(label = 'ConstruÁ„o',
                  method = 'update',
                  args = [{'visible': [False, False, True, False, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'ConstruÁ„o',
                           'showlegend':True}]),
             dict(label = 'ComÈrcio, reparaÁ„o de veÌ≠culos automotores e motocicletas',
                  method = 'update',
                  args = [{'visible': [False, False, False, True, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'ComÈrcio, reparaÁ„o de veÌ≠culos automotores e motocicletas',
                           'showlegend':True}]),
             dict(label = 'Transporte, armazenagem e correios†',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, True, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Transporte, armazenagem e correios†',
                           'showlegend':True}]),
             dict(label = 'Alojamento e alimentaÁ„o†',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, True, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Alojamento e alimentaÁ„o†',
                           'showlegend':True}]),
             dict(label = 'InformaÁ„o, comunicaÁ„o e atividades financeiras, imobili·rias, profissionais e administrativas',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, True, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'InformaÁ„o, comunicaÁ„o e atividades financeiras, imobili·rias, profissionais e administrativas',
                           'showlegend':True}]),
             dict(label = 'AdministraÁ„o p˙blica, defesa e seguridade social',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, True, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'AdministraÁ„o p˙blica, defesa e seguridade social',
                           'showlegend':True}]),
             dict(label = 'EducaÁ„o, sa˙de humana e serviÁos sociais',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, True, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'EducaÁ„o, sa˙de humana e serviÁos sociais',
                           'showlegend':True}]),
             dict(label = 'Outros ServiÁos',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, False, True, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Outros ServiÁos',
                           'showlegend':True}]),
             dict(label = 'ServiÁos domÈsticos',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, False, False, True]}, # the index of True aligns with the indices of plot traces
                          {'title': 'ServiÁos domÈsticos',
                           'showlegend':True}]),
            ])
        )
    ])

fig.update_layout(
    title_text = 'Õçndice de EquilÌ≠brio Racial',
    geo_scope='south america', 
)

fig.write_html("tmp/ie_racial.html")

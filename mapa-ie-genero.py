# Preciso de do input fundamental aqui, que é a base com os ie_genero

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
                                locations = ie_genero['nome'],
                                z = ie_genero[sector].astype(float),
                                colorscale = "Viridis",
                                zmin = -1,
                                zmax = 1))

# Add dropdowns
fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list(
            [dict(label = 'Agricultura, pecuária, produção florestal, pesca e aquicultura',
                  method = 'update',
                  args = [{'visible': [True, False, False, False, False, False, False, False, False, False, False]},
                          {'title': 'Agricultura, pecuária, produção florestal, pesca e aquicultura',
                           'showlegend':True}]),
             dict(label = 'Indústria geral',
                  method = 'update',
                  args = [{'visible': [False, True, False, False, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Indústria geral',
                           'showlegend':True}]),
             dict(label = 'Construção',
                  method = 'update',
                  args = [{'visible': [False, False, True, False, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Construção',
                           'showlegend':True}]),
             dict(label = 'Comércio, reparação de veículos automotores e motocicletas',
                  method = 'update',
                  args = [{'visible': [False, False, False, True, False, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Comércio, reparação de veículos automotores e motocicletas',
                           'showlegend':True}]),
             dict(label = 'Transporte, armazenagem e correio ',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, True, False, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Transporte, armazenagem e correio ',
                           'showlegend':True}]),
             dict(label = 'Alojamento e alimentação ',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, True, False, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Alojamento e alimentação ',
                           'showlegend':True}]),
             dict(label = 'Informação, comunicação e atividades financeiras, imobiliárias, profissionais e administrativas',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, True, False, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Informação, comunicação e atividades financeiras, imobiliárias, profissionais e administrativas',
                           'showlegend':True}]),
             dict(label = 'Administração pública, defesa e seguridade social ',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, True, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Administração pública, defesa e seguridade social ',
                           'showlegend':True}]),
             dict(label = 'Educação, saúde humana e serviços sociais',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, True, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Educação, saúde humana e serviços sociais',
                           'showlegend':True}]),
             dict(label = 'Outros Serviços',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, False, True, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Outros Serviços',
                           'showlegend':True}]),
             dict(label = 'Serviços domésticos',
                  method = 'update',
                  args = [{'visible': [False, False, False, False, False, False, False, False, False, False, True]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Serviços domésticos',
                           'showlegend':True}]),
            ])
        )
    ])

fig.update_layout(
    title_text = 'Índice de Equilíbrio de Gênero',
    geo_scope='south america', # limite map scope to USA
)

fig.write_html("tmp/ie_genero.html")

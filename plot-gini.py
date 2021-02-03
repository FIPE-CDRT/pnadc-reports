# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 08:47:47 2021

@author: Lucas
"""

import os
import plotly.graph_objects as go
import pandas as pd
import json

os.chdir('C:/Users/Lucas/Desktop/pnadc-reports')

serie_gini = pd.read_csv('tmp/serie_gini.csv')


color1 = 'rgb(64, 64, 64)'
width1 = 4
size1 = 8

color2 = 'rgb(192, 192, 192)'
width2 = 2
size2 = 4

fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Acre'],
                    mode='lines+markers',
                    name='AC',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Alagoas'],
                    mode='lines+markers',
                    name='AL',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Amapá'],
                    mode='lines+markers',
                    name='AM',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Amazonas'],
                    mode='lines+markers',
                    name='AM',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Bahia'],
                    mode='lines+markers',
                    name='BA',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Ceará'],
                    mode='lines+markers',
                    name='CE',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Distrito.Federal'],
                    mode='lines+markers',
                    name='DF',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Espírito.Santo'],
                    mode='lines+markers',
                    name='ES',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Goiás'],
                    mode='lines+markers',
                    name='GO',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Maranhão'],
                    mode='lines+markers',
                    name='MA',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Mato.Grosso'],
                    mode='lines+markers',
                    name='MT',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Mato.Grosso.do.Sul'],
                    mode='lines+markers',
                    name='MS',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Minas.Gerais'],
                    mode='lines+markers',
                    name='MG',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Pará'],
                    mode='lines+markers',
                    name='PA',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Paraíba'],
                    mode='lines+markers',
                    name='PB',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Paraná'],
                    mode='lines+markers',
                    name='PR',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Pernambuco'],
                    mode='lines+markers',
                    name='PE',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Piauí'],
                    mode='lines+markers',
                    name='PI',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Rio.de.Janeiro'],
                    mode='lines+markers',
                    name='RJ',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Rio.Grande.do.Norte'],
                    mode='lines+markers',
                    name='RN',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Rio.Grande.do.Sul'],
                    mode='lines+markers',
                    name='RS',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Rondônia'],
                    mode='lines+markers',
                    name='RO',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Roraima'],
                    mode='lines+markers',
                    name='RR',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Santa.Catarina'],
                    mode='lines+markers',
                    name='SC',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Sergipe'],
                    mode='lines+markers',
                    name='SE',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Tocantins'],
                    mode='lines+markers',
                    name='TO',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )

fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['São.Paulo'],
                    mode = 'lines+markers',
                    name = 'SP', 
                    line = dict(color=color1, width = width1),
                    marker = dict(color = color1, size = size1))
              )

fig.update_layout(
    title_text = 'Evolução do Índice de Gini',
    annotations=[
        go.layout.Annotation(x = 0.5,
                             y = -0.1,
                             text = ('Dados da PNADC 3T.'),                   
                             showarrow = False, xref='paper', yref='paper', 
                             xanchor='center',
                             yanchor='auto',
                             xshift=0,
                             yshift=0
        )],
    font=dict(
            family="Courier",
            size=10,
            color="black"
        )    
)



fig.write_html("tmp/gini.html",
               include_plotlyjs="cdn")


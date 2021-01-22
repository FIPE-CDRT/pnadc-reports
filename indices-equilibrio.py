# To do:
#    limpar o código, tem muito df sobrando sem motivo
#    double check nas operacoes



import pandas as pd
import numpy as np
import pnadc
import os
import json
import plotly.express as px


# tentar generalizar isso daqui fazendo o diretorio de trabalho seja automaticamente
# a localizacao do script

if os.getenv('username') == 'lucas.cardoso':
    os.chdir('C:/Users/lucas.cardoso/Desktop/pnadc-reports/')
elif os.getenv('username') == 'Lucas':
    os.chdir('C:/Users/Lucas/Desktop/pnadc-reports/')


os.mkdir('tmp/')


# dando problema no pacote, tem que baixar os dicionários antes
# arquivo da última PNAD tá zuado, tem que 


# Mapa do IER por UF baseado na última PNAD Trimestral

pnadc.extract.docs('tmp/')

pnad_raw = pnadc.build(data_file = 'PNADC_032020.txt',
                       input_file = 'input/input_PNADC_trimestral.txt')
    
pnadc_sp = (pnad_raw
            .filter(items=['V2007', 'V2010', 'V4010', 'VD4010','VD4016','VD4002', 'V1028', 'UF'])
            .query('VD4002 == 1')
            .assign(cod = np.floor(pnad_raw['V4010']/1000),
                    setor = pnad_raw['VD4010'],
                    mulher = (pnad_raw['V2007'] == 2).astype(int),
                    negro = (pnad_raw['V2010'].isin([2,4])).astype(int),
                    salario = pnad_raw['VD4016'],
                    count = 1,
                    peso = pnad_raw['V1028'])
            .query('salario == salario'))                     # NaN são diferentes entre si
                
del pnad_raw


# proporções a nível setor-ocupação

wm = lambda x: np.average(x, weights = pnadc_sp.loc[x.index, 'peso'])

b_ocup_setor = (pnadc_sp.groupby(['setor', 'cod', 'UF'])
                .agg(b_mulher = ('mulher', wm),
                     b_negro = ('negro', wm),
                     salario_medio = ('salario', 'sum'))       # massa salarial!!! (salario médio fica muito estranho)
                .reset_index())

p_ocup = (pnadc_sp.groupby(['cod', 'UF'])
          .agg(p_mulher = ('mulher', wm),
               p_negro = ('negro', wm))
          .reset_index()
          )

indice_estado = (b_ocup_setor
                 .merge(right = p_ocup,
                               how = 'inner',
                               on = ['cod', 'UF'])
                 )

indice_estado.loc[indice_estado.p_mulher == 0, 'p_mulher'] = 0.01     # em 2 lugares é zero!

indice_estado['ie_racial_pre'] = (((indice_estado['b_negro'] - indice_estado['p_negro'])/indice_estado['p_negro'])*((indice_estado['p_negro'])/(1-indice_estado['p_negro']))**(indice_estado['b_negro']))*indice_estado['salario_medio']
indice_estado['ie_genero_pre'] = (((indice_estado['b_mulher'] - indice_estado['p_mulher'])/indice_estado['p_mulher'])*((indice_estado['p_mulher'])/(1-indice_estado['p_mulher']))**(indice_estado['b_mulher']))*indice_estado['salario_medio']

indice_estado = indice_estado.filter(['UF', 'setor', 'ie_racial_pre', 'ie_genero_pre', 'salario_medio'])

indice_estado = indice_estado.groupby(['UF', 'setor']).sum().reset_index()

indice_estado = indice_estado[indice_estado['setor'] != 12]

indice_estado['ie_racial'] = indice_estado['ie_racial_pre']/indice_estado['salario_medio']
indice_estado['ie_genero'] = indice_estado['ie_genero_pre']/indice_estado['salario_medio']
 
ie_genero = (indice_estado.pivot(index = 'UF',
                                columns = 'setor',
                                values = 'ie_genero')
                           .reset_index()
             )

ie_racial = (indice_estado.pivot(index = 'UF',
                                columns = 'setor',
                                values = 'ie_racial')
                           .reset_index()
             )


siglas = pd.read_csv('input/siglas-estados.csv')

ie_genero = ie_genero.merge(right = siglas,
                            how = 'inner',
                            left_on = 'UF',
                            right_on = 'COD')

ie_genero = ie_genero.rename(columns={1.0: 'um',
                                      2.0: 'dois',
                                      3.0: 'tres',
                                      4.0: 'quatro',
                                      5.0: 'cinco',
                                      6.0: 'seis',
                                      7.0: 'sete',
                                      8.0: 'oito',
                                      9.0: 'nove',
                                      10.0: 'dez',
                                      11.0: 'onze',
                                      'NOME': 'nome'})

ie_genero['SIGLA'] = ie_genero['SIGLA'].astype(str)


ie_racial = ie_racial.merge(right = siglas,
                            how = 'inner',
                            left_on = 'UF',
                            right_on = 'COD')

ie_racial = ie_racial.rename(columns={1.0: 'um',
                                      2.0: 'dois',
                                      3.0: 'tres',
                                      4.0: 'quatro',
                                      5.0: 'cinco',
                                      6.0: 'seis',
                                      7.0: 'sete',
                                      8.0: 'oito',
                                      9.0: 'nove',
                                      10.0: 'dez',
                                      11.0: 'onze',
                                      'NOME': 'nome'})

ie_racial['SIGLA'] = ie_racial['SIGLA'].astype(str)

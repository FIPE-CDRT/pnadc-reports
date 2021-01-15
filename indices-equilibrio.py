import pandas as pd
import numpy as np
import pnadc
import os
import math

# tentar generalizar isso daqui fazendo o diretorio de trabalho seja automaticamente
# a localizacao do script

if os.getenv('username') == 'lucas.cardoso':
    os.chdir('C:/Users/lucas.cardoso/Desktop/pnadc-reports/')
elif os.getenv('username') == 'Lucas':
    os.chdir('C:/Users/Lucas/Desktop/pnadc-reports/')


os.mkdir('tmp/')


# dando problema no pacote, tem que baixar os dicionários antes

pnadc.extract.docs('tmp/')

pnad_raw = pnadc.get(2, 2020, 'tmp/')
    
pnad = (pnad_raw
        .filter(items=['V2007', 'V2010', 'V4010', 'VD4010','VD4017','VD4002', 'V1028', 'UF'])
        .query('UF == 35 & VD4002 == 1')
        .assign(cod = np.floor(pnad_raw['V4010']/1000),
                setor = pnad_raw['VD4010'],
                mulher = (pnad_raw['V2007'] == 2).astype(int),
                negro = (pnad_raw['V2010'].isin([2,4])).astype(int),
                salario = pnad_raw['VD4017'])
        .query('salario == salario'))                     # NaN são diferentes entre si
                
del pnad_raw
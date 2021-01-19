import pandas as pd
import numpy as np
import pnadc
import os

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
    
pnadc_sp = (pnad_raw
            .filter(items=['V2007', 'V2010', 'V4010', 'VD4010','VD4017','VD4002', 'V1028', 'UF'])
            .query('UF == 35 & VD4002 == 1')
            .assign(cod = np.floor(pnad_raw['V4010']/1000),
                    setor = pnad_raw['VD4010'],
                    mulher = (pnad_raw['V2007'] == 2).astype(int),
                    negro = (pnad_raw['V2010'].isin([2,4])).astype(int),
                    salario = pnad_raw['VD4017'],
                    count = 1,
                    peso = pnad_raw['V1028'])
            .query('salario == salario'))                     # NaN são diferentes entre si
                
del pnad_raw


# proporções a nível setor-ocupação

wm = lambda x: np.average(x, weights = pnadc_sp.loc[x.index, 'peso'])

b_ocup_setor = (pnadc_sp.groupby(['setor', 'cod'])
                .agg(b_mulher = ('mulher', wm),
                     b_negro = ('negro', wm),
                     salario_medio = ('salario', wm))
                )


p_ocup = (pnadc_sp.groupby('cod')
          .agg(p_mulher = ('mulher', wm),
               p_negro = ('negro', wm))
          )



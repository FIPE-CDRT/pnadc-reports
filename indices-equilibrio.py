import pandas as pd
import pnadc
import os


# tentar generalizar isso daqui fazendo o diretorio de trabalho seja automaticamente
# a localizacao do sript

if os.getenv('username') == 'lucas.cardoso':
    os.chdir('C:/Users/lucas.cardoso/Desktop/pnadc-reports/')
elif os.getenv('username') == 'Lucas':
    os.chdir('C:/Users/Lucas/Desktop/pnadc-reports/')


os.mkdir("tmp/")


# dando problema no pacote, tem que baixar os dicionários antes

pnadc.extract.docs("tmp/")

pnad = pnadc.get(2, 2020, "tmp/")[["V2007", "V2010", "V4010", "VD4010","VD4017",\
                                   "VD4002", "V1028", "UF"]]["UF" == "São Paulo"]

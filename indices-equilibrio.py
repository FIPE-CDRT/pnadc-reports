import pandas as pd
import pnadc
import os


# tentar generalizar isso daqui fazendo o diretorio de trabalho seja automaticamente
# a localizacao do sript

if os.getenv('username') == 'lucas.cardoso':
    os.chdir('C:/Users/lucas.cardoso/Desktop/pnadc-reports/')
elif os.getenv('username') == 'Lucas':
    os.chdir('C:/Users/Lucas/Desktop/pnadc-reports/')



pnad = pnadc.get(3, 2020, "tmp")
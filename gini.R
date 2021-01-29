#-------------------------------------------------------------------------------
#
#  Série histórica do Índice de Gini por estado
#      - periodicidade Trimestral
#      - janela de 4 anos
#      - mapas com o plotly
#
#-------------------------------------------------------------------------------

library(PNADcIBGE)
library(convey)
library(survey)
library(tidyverse)
library(plotly)

#===============================================================================

# Altere aqui o diretório e as variáveis para o último ano e Trimestre disponíveis:

setwd('C:/Users/Lucas/Desktop/pnadc-reports')
ano = 2020
trimestre = 3


#===============================================================================













#-------------------------------------------------------------------------------

ano_inicio = ano - 4
anos_completos = (ano_inicio + 1):(ano -1)


for (t in 1:trimestre) {
  
  
  PNADc_inicio = get_pnadc(year = ano,
                           quarter = t,
                           ) %>%
                 convey_prep()
  
    
}



for (t in trimestre:4) {
  
  
  PNADc_inicio = get_pnadc(year = ano_inicio,
                           quarter = t,
                           ) %>%
                 convey_prep()
  
  
}


for (year in anos_completos) {
  
  for (t in 1:4) {
    
    
    
    
    
  }
  
}
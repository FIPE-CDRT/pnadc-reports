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
library(htmlwidgets)

#===============================================================================

# Altere aqui o diretório e as variáveis para o último ano e Trimestre disponíveis:

setwd('C:/Users/Lucas/Desktop/pnadc-reports')
ano = 2020
trimestre = 3


#===============================================================================

ano_inicio = ano - 4
anos_completos = (ano_inicio + 1):(ano -1)

gini_data <- data.frame(matrix(ncol = 4, nrow = 0))   
  colnames(gini_data) <- c('Ano', 'Trimestre', 'UF', 'Gini')
  

  
for (t in 1:trimestre) {
  
  
  pnadc = get_pnadc(year = ano,
                    quarter = t,
                    vars = c('Ano','Trimestre', 'UF', 'VD4019'))
  
  pnadc <- convey_prep(pnadc)
  
  gini_estados <- svyby(~VD4019, by = ~UF, pnadc, svygini, na.rm  =  TRUE)
    rownames(gini_estados) <- NULL
  
  gini_estados <- gini_estados %>%
                  dplyr::select(UF, VD4019) %>%
                  dplyr::rename(Gini = VD4019) %>%
                  dplyr::mutate(Ano = ano,
                                Trimestre = t) %>%
                  dplyr::relocate(Ano, Trimestre, UF, Gini)
  
  gini_data <- rbind(gini_data, gini_estados)
  
    
}


  
  
  for (year in anos_completos) {
    
    for (t in 1:4) {
      
      pnadc = get_pnadc(year = year,
                        quarter = t,
                        vars = c('Ano','Trimestre', 'UF', 'VD4019'))
      
      pnadc <- convey_prep(pnadc)
      
      gini_estados <- svyby(~VD4019, by = ~UF, pnadc, svygini, na.rm  =  TRUE)
      rownames(gini_estados) <- NULL
      
      gini_estados <- gini_estados %>%
        dplyr::select(UF, VD4019) %>%
        dplyr::rename(Gini = VD4019) %>%
        dplyr::mutate(Ano = year,
                      Trimestre = t) %>%
        dplyr::relocate(Ano, Trimestre, UF, Gini)
      
      gini_data <- rbind(gini_data, gini_estados)
      
      
    }
    
  }
  
  
  
for (t in trimestre:4) {
  
  
  pnadc = get_pnadc(year = ano_inicio,
                    quarter = t,
                    vars = c('Ano','Trimestre', 'UF', 'VD4019'))
  
  pnadc <- convey_prep(pnadc)
  
  gini_estados <- svyby(~VD4019, by = ~UF, pnadc, svygini, na.rm  =  TRUE)
    rownames(gini_estados) <- NULL
  
  gini_estados <- gini_estados %>%
                  dplyr::select(UF, VD4019) %>%
                  dplyr::rename(Gini = VD4019) %>%
                  dplyr::mutate(Ano = ano_inicio,
                                Trimestre = t) %>%
                  dplyr::relocate(Ano, Trimestre, UF, Gini)
  
  gini_data <- rbind(gini_data, gini_estados)
  
  
}


  
serie_gini <- gini_data %>%
              tidyr::pivot_wider(names_from = UF,
                                 values_from = Gini) %>%
              dplyr::arrange(Ano, Trimestre) %>%
              dplyr::mutate(Ano_Tri = paste0(Ano, 'T', Trimestre)) %>%
              dplyr::select(-Ano, -Trimestre) %>%
              dplyr::relocate(Ano_Tri)


#-------------------------------------------------------------------------------
# Plotando (jeito burro, melhorar depois esse código)
#-------------------------------------------------------------------------------

names(serie_gini) <- str_replace_all(names(serie_gini), c(" " = "." , "," = "" ))  
  
fig <- plot_ly(serie_gini,
               x = ~Ano_Tri,
               y = ~Distrito.Federal,
               name = 'DF',
               type = 'scatter',
               mode = 'lines+markers',
               line = list(color = 'rgb(192, 192, 192)', width = 2),
               marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Rio.de.Janeiro, name = 'RJ', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Espírito.Santo, name = 'ES', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Minas.Gerais, name = 'MG', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Rio.Grande.do.Sul, name = 'RS', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Santa.Catarina, name = 'SC', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Paraná, name = 'PR', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Amazonas, name = 'AM', mode = 'lines+markers',
                line = list(color = 'rgb(192, 192, 192)', width = 2),
                marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Acre, name = 'AC', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Roraima, name = 'RR', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Rondônia, name = 'RO', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Pará, name = 'PA', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Amapá, name = 'AP', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Tocantins, name = 'TO', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Bahia, name = 'BA', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Sergipe, name = 'SE', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Alagoas, name = 'AL', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Pernambuco, name = 'PE', mode = 'lines+markers',
                line = list(color = 'rgb(192, 192, 192)', width = 2),
                marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Paraíba, name = 'PB', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Rio.Grande.do.Norte, name = 'RN', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Ceará, name = 'CE', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Piauí, name = 'PI', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Maranhão, name = 'MA', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Mato.Grosso, name = 'MT', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Mato.Grosso.do.Sul, name = 'MS', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~Goiás, name = 'GO', mode = 'lines+markers',
                  line = list(color = 'rgb(192, 192, 192)', width = 2),
                  marker = list(color = 'rgb(192, 192, 192)',  size = 4)) %>%
        add_trace(y = ~São.Paulo, name = 'SP', mode = 'lines+markers',
                  line = list(color = 'rgb(64, 64, 64)', width = 4),
                  marker = list(color = 'rgb(64, 64, 64)',  size = 8)) %>%
        layout(title = 'Evolução Histórica do Índice de Gini',
               xaxis = list(title = ' '),
               yaxis = list(title = 'Gini')) 


f <- "tmp/gini.html"
saveWidget(fig,file.path(normalizePath(dirname(f)),basename(f)), selfcontained = F)
  
  
library(tidyverse)
library(PNADcIBGE)

# define o local do script como diretório!

rstudioapi::getSourceEditorContext()$path %>%
  dirname() %>%
  setwd()

dir.create("tmp")


# pipe grande que trata quase tudo de uma vez

pnadc_sp <- get_pnadc(year = 2019,
                        quarter = 4,
                        savedir = "tmp",
                        vars = c("V2007", "V2010", "V4010", "V4013","VD4017", "VD4002"),
                        design = FALSE) # %>%

pnadc_sp <- pnadc_sp %>% dplyr::filter(UF == "São Paulo" & VD4002 == "Pessoas ocupadas") %>%
                         dplyr::mutate(cod = floor(as.numeric(V4010)/100),
                                       cnae = floor(as.numeric(V4013)/1000),
                                       mulher = ifelse(V2007 == "Mulher", 1, 0),
                                       negro = ifelse(V2010 == "Preta" | V2010 == "Parda", 1, 0),
                                       salario = ifelse(VD4017 == NA, 0, VD4017))

b_ocup_setor <- pnadc_sp %>% 
                dplyr::group_by(cnae, cod) %>%
                dplyr::summarise(b_mulher = mean(mulher),
                                 b_negro = mean(negro),
                                 massa_salarial = sum(salario))

p_ocup <- pnadc_sp %>%
          dplyr::group_by(cod) %>%
          dplyr::summarise(p_mulher = mean(mulher),
                           p_negro = mean(negro))




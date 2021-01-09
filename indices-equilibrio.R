library(tidyverse)
library(PNADcIBGE)

# define o local do script como diretório!

### Falta: definir variável setorial (CNAE 2 dígitos é muito desagregado pra PNAD Trimestral)


rstudioapi::getSourceEditorContext()$path %>%
  dirname() %>%
  setwd()

dir.create("tmp")


# pipe grande que trata quase tudo de uma vez

pnadc_sp <- get_pnadc(year = 2019,
                      quarter = 4,
                      savedir = "tmp",
                      vars = c("V2007", "V2010", "V4010", "V4013","VD4017", "VD4002"),
                      design = FALSE) %>%
            dplyr::filter(UF == "São Paulo" & VD4002 == "Pessoas ocupadas") %>%
            dplyr::mutate(cod = floor(as.numeric(V4010)/100),
                                      cnae = floor(as.numeric(V4013)/1000),
                                      mulher = ifelse(V2007 == "Mulher", 1, 0),
                                      negro = ifelse(V2010 == "Preta" | V2010 == "Parda", 1, 0),
                                      salario = VD4017) %>%
            dplyr::filter(!is.na(salario))


# proporções a nível setor-ocupação

b_ocup_setor <- pnadc_sp %>% 
                dplyr::group_by(cnae, cod) %>%
                dplyr::summarise(b_mulher = mean(mulher),
                                 b_negro = mean(negro),
                                 massa_salarial = sum(salario))


# participações a nível ocupação

p_ocup <- pnadc_sp %>%
          dplyr::group_by(cod) %>%
          dplyr::summarise(p_mulher = mean(mulher),
                           p_negro = mean(negro))


indices_setor <- b_ocup_setor %>% 
                  dplyr::left_join(p_ocup) %>%
                  dplyr::mutate(ie_racial = ((b_negro - p_negro)/p_negro)*((p_negro)/(1-p_negro))^(b_negro),
                                ie_genero = ((b_mulher - p_mulher)/p_mulher)*((p_mulher)/(1-p_mulher))^(b_mulher)) %>%
                  dplyr::mutate(ie_racial = ifelse(b_negro == 0, NA, ie_racial),
                                ie_genero = ifelse(b_mulher == 0, NA, ie_genero))

racial_setor <- indices_setor %>%
                dplyr::ungroup() %>%
                dplyr::filter(!is.na(ie_racial)) %>%
                dplyr::group_by(cnae) %>%
                dplyr::summarise(ie_racial = weighted.mean(ie_racial, massa_salarial))

final_setor <- indices_setor %>%
               dplyr::ungroup() %>%
               dplyr::filter(!is.na(ie_genero)) %>%
               dplyr::group_by(cnae) %>%
               dplyr::summarise(ie_genero = weighted.mean(ie_genero, massa_salarial))



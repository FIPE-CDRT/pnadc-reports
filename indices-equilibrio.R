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
                      vars = c("V2007", "V2010", "V4010", "VD4010","VD4017", "VD4002"),
                      design = FALSE) %>%
            dplyr::filter(UF == "São Paulo" & VD4002 == "Pessoas ocupadas") %>%
            dplyr::mutate(cod = floor(as.numeric(V4010)/1000),
                          setor = VD4010,
                          mulher = ifelse(V2007 == "Mulher", 1, 0),
                          negro = ifelse(V2010 == "Preta" | V2010 == "Parda", 1, 0),
                          salario = VD4017,
                          count = 1) %>%
            dplyr::filter(!is.na(salario))



# proporções a nível setor-ocupação

b_ocup_setor <- pnadc_sp %>% 
                dplyr::group_by(setor, cod) %>%
                dplyr::summarise(b_mulher = mean(mulher),
                                 b_negro = mean(negro),
                                 massa_salarial = sum(salario),
                                 n = sum(count))



# participações a nível ocupação

p_ocup <- pnadc_sp %>%
          dplyr::group_by(cod) %>%
          dplyr::summarise(p_mulher = mean(mulher),
                           p_negro = mean(negro))


indices_setor <- b_ocup_setor %>% 
                 dplyr::left_join(p_ocup) %>%
                 dplyr::ungroup() %>%
                 dplyr::mutate(ie_racial = ((b_negro - p_negro)/p_negro)*((p_negro)/(1-p_negro))^(b_negro),
                               ie_genero = ((b_mulher - p_mulher)/p_mulher)*((p_mulher)/(1-p_mulher))^(b_mulher)) %>%
                 dplyr::group_by(setor) %>%
                 dplyr::summarise(ie_racial = weighted.mean(ie_racial, massa_salarial),
                                  ie_genero = weighted.mean(ie_genero, massa_salarial)) %>%
                 dplyr::filter(setor != "Atividades mal definidas")
                  


#================================ Plotando =====================================


dir.create("output")


ggplot(indices_setor) + 
  geom_bar(aes(x = ie_racial, y = reorder(setor, -ie_racial)), stat = 'identity') +
  xlab("Índice de Equilíbrio Racial") +
  theme_bw() +
  theme(axis.title.y = element_blank(),
        axis.text.y = element_text(size = 4))

ggsave(file = "output/ie_racial.png", dpi = 600, width = 16, height = 9, units = "cm")


ggplot(indices_setor) + 
  geom_bar(aes(x = ie_genero, reorder(setor, -ie_genero)), stat = 'identity') +
  xlab("Índice de Equilíbrio de Gênero") +
  theme_bw() +
  theme(axis.title.y = element_blank(),
        axis.text.y = element_text(size = 4))

ggsave(file = "output/ie_genero.png", dpi = 600, width = 16, height = 9, units = "cm")







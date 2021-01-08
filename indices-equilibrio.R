library(tidyverse)
library(PNADcIBGE)

# define o local do script como diretório!

rstudioapi::getSourceEditorContext()$path %>%
  dirname() %>%
  setwd()



from pandas import *

plantio_1 = [10,9,7,8,8,9,7,6,8,7]
plantio_2 = [13,6,12,11,4,6,6,7,8,6]

tabela = DataFrame({"Plantio 1":plantio_1,"Plantio 2":plantio_2})

tabela

tabela_variancia = tabela.var()
tabela_variancia

tabela["Plantio 1"].var()

tabela_desvio = tabela.std()
tabela_desvio

tabela_resumo = tabela.describe()
tabela_resumo

cv = tabela.std()/ tabela.mean()
cv

salarios = [1200, 2525, 1700.80, 2300]
idades = [18,55,30,28]
cargos = ["Auxiliar de cozinha","Contador","Guarda Municipal","Administrador"]

tabela_2 = DataFrame({"Salário":salarios,"Idade":idades,"Cargo":cargos})
tabela_2

tabela_2.std()

m = tabela_2.mean()
sd = tabela_2.std()
m

cv2 = sd/m
cv2

t_1 = tabela_2.mean()
t_2 = tabela_2.std()

tabela_3 = DataFrame({"Média":list(t_1),"Desvio padrão":list(t_2)},index=["Salário","Idade"])

tabela_3

q1 = tabela_2.quantile(0.25)
q1

q2 = tabela_2.quantile(0.75)
q2

#abs calcula o valor absoluto. mesma função módulo. Exemplo: abs(-1) = |-1| = 1; abs(1) = |1| = 1
dist = q2 - q1
dist

mediana = tabela_2.median()
mediana

tabela_4 = DataFrame({"Mediana":mediana,"Distância Interquartil":dist},index=["Salário","Idade"])
tabela_4

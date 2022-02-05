from google.colab import auth
import gspread
from oauth2client.client import GoogleCredentials
from pandas import *

auth.authenticate_user()
gc = gspread.authorize(GoogleCredentials.get_application_default())

arquivo = gc.open_by_url("https://docs.google.com/spreadsheets/d/18m4bR1e36C32iaQl9-1vjGx0Vv7000zLXJ9GuF_77v8/edit?usp=sharing")

experimento_feijao = arquivo.worksheet("Experimento_feijao")
funcionario = arquivo.worksheet("Funcionarios")
producao_oleo = arquivo.worksheet("Producao_oleo")

tabela_experimento_feijao = DataFrame.from_records(experimento_feijao.get_all_records())
tabela_funcionario = DataFrame.from_records(funcionario.get_all_records())
tabela_produto_oleo = DataFrame.from_records(producao_oleo.get_all_records())

tabela_experimento_feijao
tabela_funcionario
tabela_produto_oleo

cultivar = list(tabela_experimento_feijao["Cultivar"])
vagens = list(tabela_experimento_feijao["Vagens"])
graos = list(tabela_experimento_feijao["Graos"])

tabela1 = DataFrame({"Vagens":vagens,"Graos":graos,"Cultivar":cultivar})
tabela1

escolaridade = list(tabela_funcionario["Escolaridade"])
itens = list(tabela_funcionario["Itens"])
vendas = list(tabela_funcionario["Vendas"])
idade = list(tabela_funcionario["Idade"])
loja = list(tabela_funcionario["Loja"])

tabela2 = DataFrame({"Itens":itens,"Vendas":vendas,"Idade":idade,"Loja":loja},index=escolaridade)
tabela2

item = list(tabela_produto_oleo["Item"])
ano = list(tabela_produto_oleo["Ano"])
producao = list(tabela_produto_oleo["Producao"])

tabela3 = DataFrame({"Ano":ano,"Producao":producao,"Item":item})
tabela3

tabela_variancia = tabela2["Vendas"].var()
tabela_variancia

tabela_media = tabela2["Vendas"].mean()
tabela_media

tabela_desviopadrao = tabela2["Vendas"].std()
tabela_desviopadrao

tabela_mediana = tabela2["Idade"].median()
tabela_mediana

q1 = tabela2["Idade"].quantile(0.25)
q1
q2 = tabela2["Idade"].quantile(0.75)
q2
dist = q2 - q1
dist

tabela_media = tabela1.groupby(["Cultivar"]).mean()
tabela_media

tabela_media_ = DataFrame({"Graos":list(tabela_media["Graos"])},index=tabela_media.index)
tabela_media_

tabela_desviopadrao = tabela1.groupby(["Cultivar"]).std()
tabela_desviopadrao

tabela_desviopadrao_ = DataFrame({"Graos":list(tabela_desviopadrao["Graos"])},index=tabela_desviopadrao.index)
tabela_desviopadrao_

tabela_varianca = tabela1.groupby(["Cultivar"]).var()
tabela_varianca

tabela_varianca_ = DataFrame({"Graos":list(tabela_varianca["Graos"])},index=tabela_varianca.index)
tabela_varianca_

##cálculo do coeficiente de variação
cv = tabela_desviopadrao_ / tabela_media_
cv

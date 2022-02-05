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

tabela_experimento_feijao
tabela_funcionario
tabela_produto_oleo

cultivar = list(tabela_experimento_feijao["Cultivar"])
vagens = list(tabela_experimento_feijao["Vagens"])
graos = list(tabela_experimento_feijao["Graos"])

tabela_1 = DataFrame({"Cultivar":cultivar,"Vagens":vagens,"Graos":graos})

tabela_11 = tabela_1.groupby(["Cultivar"]).sum()
tabela_11

tabela1 = tabela_11.plot(kind="barh",
                    legend=True,
                    title="Experimento da produtividade em número de vagens e peso dos grãos por planta para diferentes cultivares de feijão caupi",
                    xlabel="Cultivar")
tabela1.set_xlabel("Gramas")
tabela1.plot()

escolaridade = list(tabela_funcionario["Escolaridade"])
itens = list(tabela_funcionario["Itens"])
vendas = list(tabela_funcionario["Vendas"])
idade = list(tabela_funcionario["Idade"])
loja = list(tabela_funcionario["Loja"])

tabela_1 = DataFrame({"Itens":itens,"Vendas":vendas,"Idade":idade,"Loja":loja},index=escolaridade)
tabela_1

tabela_21 = tabela_funcionario.groupby(["Escolaridade"]).count()
tabela_21

tabela_q_3 = DataFrame({"Funcionários":list(tabela_21["Itens"])},index=tabela_21.index)

tabela_q_3

tabela2 = tabela_21.plot(kind="pie",autopct="%1.1f%%",
                    y="Itens",
                    x="Escolaridade",
                    legend=False,
                    ylabel="",
                    title="Percentual de funcionários com cada escolaridade.")
tabela2.plot()

tabela_22 = tabela_funcionario.groupby(["Loja"]).sum()
tabela_22

tabela_222 = tabela_funcionario.groupby(["Loja"]).count()
tabela_222

item = list(tabela_produto_oleo["Item"])
ano = list(tabela_produto_oleo["Ano"])
producao = list(tabela_produto_oleo["Producao"])

tabela_3 = DataFrame({"Ano":ano,"Producao":producao},index=item)
tabela_3

tabela_4 = tabela_produto_oleo.query("Item == 'Oil, coconut (copra)' and Ano >= 2001")

tabela_44 = tabela_4.plot(kind="line",
              x="Ano",
              y="Producao",
              legend=False,
              ylabel="Producao",
              figsize=(10,5),
              title= "Produção de óleo de coco no brasil nos últimos 20 anos.",              
              style="s-",
              xticks=tabela_4["Ano"])
tabela_44.plot()

tabela_4

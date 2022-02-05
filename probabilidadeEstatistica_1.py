from pandas import *
from numpy import *

amostra = list(range(1,41))
fertilizante = list(2*(10*["Orgânico"] + 10*["Químico"]))
micro = list(20*["B. subtilis"] + 20*["T. asperellum"])
mspa = list(random.normal(6.5,0.2,10)) + list(random.normal(8,0.8,10)) + list(random.normal(7.3,0.6,10)) + list(random.normal(7.87,1.3,10)) #massa seca parte aerea
msr = list(random.normal(2.99,0.6,10)) + list(random.normal(3.75,0.3,10)) + list(random.normal(2.87,0.7,10)) + list(random.normal(3.15,0.3,10)) #massa seca raiz

tbl_crescimento = DataFrame({"Fertilizante":fertilizante,"Inóculo":micro,"MSPA":mspa,"MSR":msr},index=amostra)

tbl_crescimento.head()

medias = tbl_crescimento.groupby(["Fertilizante","Inóculo"]).describe()

medias["MSR"]

medias["MSPA"].unstack().plot(kind="bar",y="mean", yerr="std", capsize=4)

grafico_medias_std = medias["MSPA"].unstack().plot(kind="bar",y="mean",yerr="std",capsize=4,ylabel="Matéria seca da parte aérea (g)")

tabela_mspa = tbl_crescimento[["Fertilizante","Inóculo","MSPA"]]
tabela_mspa.head()

org_b = tabela_mspa.query("Fertilizante == 'Orgânico' and Inóculo == 'B. subtilis'")
org_t = tabela_mspa.query("Fertilizante == 'Orgânico' and Inóculo == 'T. asperellum'")
qui_b = tabela_mspa.query("Fertilizante == 'Químico' and Inóculo == 'B. subtilis'")
qui_t = tabela_mspa.query("Fertilizante == 'Químico' and Inóculo == 'T. asperellum'")

tbl_mspa_por_coluna = DataFrame({"Org / B. subtilis": list(org_b["MSPA"]), "Org / T. asperellum": list(org_t["MSPA"]),"Qui / B. subtilis": list(qui_b["MSPA"]), "Qui / T. asperellum": list(qui_t["MSPA"])})

tbl_mspa_por_coluna

tbl_mspa_por_coluna.plot(kind="box")

grafico_box2 = tbl_mspa_por_coluna.plot(kind="box",legend=False, rot=15)
grafico_box2.set_title("Matéria seca nos diferentes tratamentos")
grafico_box2.set_xlabel("Tratamentos")
grafico_box2.set_ylabel("Matéria seca na parte aérea (g)")
grafico_box2.plot()

grafico_medias_std = medias["MSR"].unstack().plot(kind="bar",y="mean",yerr="std",capsize=4,ylabel="Matéria seca da raiz")

tabela_msr = tbl_crescimento[["Fertilizante","Inóculo","MSR"]]
tabela_msr.head()

org_b = tabela_msr.query("Fertilizante == 'Orgânico' and Inóculo == 'B. subtilis'")
org_t = tabela_msr.query("Fertilizante == 'Orgânico' and Inóculo == 'T. asperellum'")
qui_b = tabela_msr.query("Fertilizante == 'Químico' and Inóculo == 'B. subtilis'")
qui_t = tabela_msr.query("Fertilizante == 'Químico' and Inóculo == 'T. asperellum'")

tbl_msr_por_coluna = DataFrame({"Org / B. subtilis": list(org_b["MSR"]), "Org / T. asperellum": list(org_t["MSR"]),"Qui / B. subtilis": list(qui_b["MSR"]), "Qui / T. asperellum": list(qui_t["MSR"])})
tbl_msr_por_coluna

grafico_box2 = tbl_msr_por_coluna.plot(kind="box",legend=False, rot=15)
grafico_box2.set_title("Matéria seca nos diferentes tratamentos")
grafico_box2.set_xlabel("Tratamentos")
grafico_box2.set_ylabel("Matéria seca da raiz")
grafico_box2.plot()

tbl_crescimento["Relacao_PA_R"] = tbl_crescimento["MSPA"]/tbl_crescimento["MSR"]
tbl_crescimento.head()

medias = tbl_crescimento.groupby(["Fertilizante","Inóculo"]).describe()
medias["Relacao_PA_R"]

grafico_medias_std = medias["Relacao_PA_R"].unstack().plot(kind="bar",y="mean",yerr="std",capsize=4,ylabel="Relação entre a massa seca da parte aérea da planta e da raiz")
amostra = list(range(1,31))
ponto = list(range(1,11)) + list(range(1,11)) + list(range(1,11))
coleta = 10*[1] + 10*[2] + 10*[3]
od = list(random.normal(6.5,0.8,10)) + list(random.normal(7,0.6,10))+ list(random.normal(8,1.2,10))#oxigênio dissolvido
temp_amb = list(random.normal(32,1,10)) + list(random.normal(22,0.8,10)) + list(random.normal(27,0.5,10))#temperatura ambiente
temp_amos = list(random.normal(32,0.7,10)) + list(random.normal(22.5,0.5,10)) + list(random.normal(28.3,0.7,10))#temperatura da amostra
ph = list(random.normal(7.9,0.3,10)) + list(random.normal(7.5,0.4,10)) + list(random.normal(7,0.6,10))
condutividade = list(random.normal(285,7.8,10)) + list(random.normal(228,10,10)) + list(random.normal(268,15,10))
turbidez = list(random.normal(1.5,1,10)) + list(random.normal(1.8,0.8,10)) + list(random.normal(2.7,3.5,10))


tbl_agua = DataFrame({"Ponto":ponto,"Coleta":coleta,"Temperatura Ambiente":temp_amb,"Temperatura Amostra":temp_amos,"pH":ph,"Condutividade":condutividade,"Turbidez":turbidez,"Oxigênio dissolvido":od},index=amostra)

#medias = tbl_agua.groupby(["Ponto","Coleta"]).describe()
medias = tbl_agua.groupby(["Coleta"]).describe()
medias["pH"]

grafico_medias_std = medias["pH"].plot(kind="bar",y="mean",legend=False,yerr="std",capsize=4,ylabel="Média e Desvio Padrão do pH")

tabela_msr = tbl_agua[["Coleta","Temperatura Ambiente"]]
tabela_msr.head()

grafico_box = tabela_msr.boxplot(by=["Coleta"],rot=15,grid=False,figsize=(7,6))
grafico_box.set_title("Média da Temperatura Ambiente")
grafico_box.set_xlabel("Coleta")
grafico_box.set_ylabel("Temperatura Ambiente")
grafico_box.plot()

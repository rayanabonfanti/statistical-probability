from google.colab import auth
import gspread
from oauth2client.client import GoogleCredentials
from pandas import *

auth.authenticate_user()
gc = gspread.authorize(GoogleCredentials.get_application_default())

arquivo = gc.open_by_url("https://docs.google.com/spreadsheets/d/1MzldG24TTuZsDTGZooDVIobRCP5RvoCpyGcsNrMLkHo/edit?usp=sharing")

respostas_formulario = arquivo.worksheet("respostas")

tabela_respostas_formulario = DataFrame.from_records(respostas_formulario.get_all_records())

tabela_respostas_formulario

dataHora = list(tabela_respostas_formulario["dataHora"])
curso = list(tabela_respostas_formulario["curso"])
transporte = list(tabela_respostas_formulario["transporte"])
tempoDeslocamento = list(tabela_respostas_formulario["tempoDeslocamento"])
horaEstudo = list(tabela_respostas_formulario["horaEstudo"])
idade = list(tabela_respostas_formulario["idade"])
pessoasCasa = list(tabela_respostas_formulario["pessoasCasa"])
horasForaCampus = list(tabela_respostas_formulario["horasForaCampus"])
semestre = list(tabela_respostas_formulario["semestre"])
horasBemEstar = list(tabela_respostas_formulario["horasBemEstar"])
qtdDisciplinas = list(tabela_respostas_formulario["qtdDisciplinas"])
atvdExtra = list(tabela_respostas_formulario["atvdExtra"])

tabela = DataFrame({"dataHora":dataHora,"curso":curso,"transporte":transporte,"tempoDeslocamento":tempoDeslocamento,"horaEstudo":horaEstudo,"idade":idade,"pessoasCasa":pessoasCasa,"horasForaCampus":horasForaCampus,"semestre":semestre,"horasBemEstar":horasBemEstar,"qtdDisciplinas":qtdDisciplinas,"atvdExtra":atvdExtra})
tabela

tabela_mediaHoraEstudo = tabela["horaEstudo"].mean()
tabela_mediaHoraEstudo

tabela_varianciaHoraEstudo = tabela["horaEstudo"].var()
tabela_varianciaHoraEstudo

tabela_desvioPadraoHoraEstudo = tabela["horaEstudo"].std()
tabela_desvioPadraoHoraEstudo

tabela_medianaIdade = tabela["idade"].median()
tabela_medianaIdade

tabela_distanciaInterquartilIdadeF25 = tabela["idade"].quantile(0.25)
tabela_distanciaInterquartilIdadeF25

tabela_distanciaInterquartilIdadeF75 = tabela["idade"].quantile(0.75)
tabela_distanciaInterquartilIdadeF75

resultado = tabela_distanciaInterquartilIdadeF75 - tabela_distanciaInterquartilIdadeF25
resultado

tabela.groupby(["horaEstudo"]).median()

tabela_medianaTransporte = tabela.groupby(["transporte"]).mean()
tabela_medianaTransporteHorasBemEstar = DataFrame({"horasBemEstar":list(tabela_medianaTransporte["horasBemEstar"])},index=tabela_medianaTransporte.index)
tabela_medianaTransporteHorasBemEstar

tabela_medianaTransporte1 = tabela.groupby(["transporte"]).std()
tabela_medianaTransporteHorasBemEstar1 = DataFrame({"horasBemEstar":list(tabela_medianaTransporte1["horasBemEstar"])},index=tabela_medianaTransporte1.index)
tabela_medianaTransporteHorasBemEstar1

tabelaResultado = tabela_medianaTransporteHorasBemEstar1 / tabela_medianaTransporteHorasBemEstar
tabelaResultado

tabela["horaEstudo"].mode()

tabela["transporte"].mode()

tabela_horaCurso = DataFrame({"horaEstudo":horaEstudo,"curso":curso})
tabela_horaCurso
tabelaGroup = tabela_horaCurso.groupby("curso").mean()
tabelaGroup

grafico_1 = tabelaGroup.plot(kind="pie",autopct="%1.1f%%", y="horaEstudo", legend=False, ylabel="", title="Hora de Estudo por Curso")

tabela_idadeCurso = DataFrame({"idade":idade,"curso":curso})
tabela_idadeCurso
tabela_Query = tabela_idadeCurso.query("idade >= 30 and idade <= 60")
tabelaGroup = tabela_Query.groupby("curso").mean()
tabelaGroup

grafico_1 = tabelaGroup.plot(kind="pie",autopct="%1.1f%%", y="idade", legend=False, ylabel="", title="Idade entre 30 e 60 anos por Curso")

tabela_idadeCurso = DataFrame({"idade":idade,"curso":curso})
tabela_idadeCurso
tabela_Query = tabela_idadeCurso.query("idade >= 30 and idade <= 60")
tabelaGroup = tabela_Query.groupby("curso").mean()
tabelaGroup

tabelaGroup.plot(kind="bar",title="Idade entre 30 e 60 anos por Curso")

graficoC = tabelaGroup.plot(kind="barh",
                    legend=False,
                    title="Idade entre 30 e 60 anos por Curso",
                    xlabel="Cursos")
graficoC.set_xlabel("Idade")
graficoC.plot()

medias = tabela.groupby(["curso"]).describe()
medias["idade"]

medias["idade"].plot(kind="bar",y="mean", legend=False,yerr="std", capsize=4,rot=15,title="Média de Idade por Curso")

tabela_box = tabela[["curso","idade"]]
tabela_box.head()

grafico_box = tabela_box.boxplot(by=["curso"],rot=15,grid=False,figsize=(7,6))
grafico_box.set_title("Média de Idade por Curso")
grafico_box.set_xlabel("curso")
grafico_box.set_ylabel("idade")
grafico_box.plot()


from bs4 import BeautifulSoup

html_file = open("data_in_table_2.html", mode='r', encoding="utf-8")
soup = BeautifulSoup(html_file, "html.parser")
table = soup.find_all("table")[1]
table_rows = table.find_all("tr")
print(table_rows)

dados_cursos = []

for i in table_rows:
        colunas = i.find_all("td")
        if len(colunas) > 0:
            nome_curso = colunas[0].text
            interesse = colunas[1].text
            dict_curso = {"nome": nome_curso, "interesse": interesse}
            dados_cursos.append(dict_curso)

print(dados_cursos)
import pdb; pdb.set_trace()
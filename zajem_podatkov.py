import requests
import bs4
import csv

link1 = "https://www.statbunker.com/competitions/GoalsFor?comp_id=790"
link2 = "https://www.statbunker.com/competitions/GoalsAgainst?comp_id=790"
link3 = "https://www.statbunker.com/competitions/Top10KeepersCleanSheets?comp_id=790"
link4 = "https://www.statbunker.com/competitions/TeamsGoalScorersTypeOfPlay?comp_id=790"

def prenesi_in_shrani_html(url, ime_datoteke):
    response = requests.get(url)

    if response.status_code == 200:
        print("HTML je uspešno prenesen.")
        with open(ime_datoteke, "w", encoding="utf-8") as f:
            f.write(response.text)
    else:
        print("Prišlo je do napake.")

prenesi_in_shrani_html(link1, "podatki/goals_for.html")
prenesi_in_shrani_html(link2, "podatki/goals_against.html")
prenesi_in_shrani_html(link3, "podatki/clean_sheets.html")
prenesi_in_shrani_html(link4, "podatki/goal_types.html")

def preberi_html(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as f:
        return f.read()

def imena_stolpcev_iz_tabele(tabela):
    glava = tabela.find("thead")
    naslovi = glava.find_all("th")

    imena_stolpcev = []

    for naslov in naslovi[:-1]:
        imena_stolpcev.append(naslov.text.strip())

    return imena_stolpcev

def podatki_iz_tabele(tabela, imena_stolpcev):
    vsebina_tabele = tabela.find("tbody")
    vrstice = vsebina_tabele.find_all("tr")

    podatki = []

    if len(vrstice) > 0:
        for vrstica in vrstice:
            celice = vrstica.find_all("td")

            vrednosti_vrstice = []

            for celica in celice[:-1]:
                vrednosti_vrstice.append(celica.text.strip())

            podatki.append(vrednosti_vrstice)
    else:
        celice = vsebina_tabele.find_all("td")
        st_celic = len(imena_stolpcev) + 1

        for i in range(0, len(celice), st_celic):
            vrednosti_vrstice = []

            for celica in celice[i:i + len(imena_stolpcev)]:
                vrednosti_vrstice.append(celica.text.strip())

            podatki.append(vrednosti_vrstice)

    return podatki

def podatki_iz_html(html):
    juha = bs4.BeautifulSoup(html, "html.parser")
    tabela = juha.find("table") 

    imena_stolpcev = imena_stolpcev_iz_tabele(tabela)
    podatki = podatki_iz_tabele(tabela, imena_stolpcev)

    return imena_stolpcev, podatki

def zapisi_csv(imena_stolpcev, podatki, ime_datoteke):
    with open(ime_datoteke, "w", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(imena_stolpcev)

        for vrstica in podatki:
            writer.writerow(vrstica)

def html_v_csv(html_datoteka, csv_datoteka):
    html = preberi_html(html_datoteka)
    imena_stolpcev, podatki = podatki_iz_html(html)

    zapisi_csv(imena_stolpcev, podatki, csv_datoteka) 

html_v_csv("podatki/goals_for.html", "podatki/goals_for.csv")
html_v_csv("podatki/goals_against.html", "podatki/goals_against.csv")
html_v_csv("podatki/clean_sheets.html", "podatki/clean_sheets.csv")
html_v_csv("podatki/goal_types.html", "podatki/goal_types.csv")
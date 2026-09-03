import requests
import bs4

link = "https://www.statbunker.com/competitions/GoalsFor?comp_id=790"

def prenesi_in_shrani_html(url, ime_datoteke):
    response = requests.get(url)

    if response.status_code == 200:
        print("HTML je uspešno prenesen.")
        with open(ime_datoteke, "w", encoding="utf-8") as f:
            f.write(response.text)
    else:
        print("Prišlo je do napake.")

prenesi_in_shrani_html(link, "podatki/goals_for.html")

def preberi_html(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as f:
        return f.read()

html = preberi_html("podatki/goals_for.html")

def imena_stolpcev_iz_tabele(html):
    juha = bs4.BeautifulSoup(html, "html.parser")
    tabela = juha.find("table")

    glava = tabela.find("thead")
    naslovi = glava.find_all("th")

    imena_stolpcev = []

    for naslov in naslovi[:-1]:
        imena_stolpcev.append(naslov.text.strip())

    return imena_stolpcev

def podatki_iz_tabele(html):
    juha = bs4.BeautifulSoup(html, "html.parser")
    tabela = juha.find("table") 

    vsebina_tabele = tabela.find("tbody")
    vrstice = vsebina_tabele.find_all("tr")

    podatki = []

    for vrstica in vrstice:
        celice = vrstica.find_all("td")

        vrednosti_vrstice = []

        for celica in celice[:-1]:
            vrednosti_vrstice.append(celica.text.strip())

        podatki.append(vrednosti_vrstice)

    return podatki

imena_stolpcev = imena_stolpcev_iz_tabele(html)
podatki = podatki_iz_tabele(html)
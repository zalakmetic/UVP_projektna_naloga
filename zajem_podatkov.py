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


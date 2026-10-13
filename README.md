# Projektna naloga pri predmetu Uvod v programiranje

V projektni nalogi sem analizirala podatke o reprezentancah na nogometnem svetovnem prvenstvu 2026, ki so objavljeni na spletni strani [StatBunker](https://www.statbunker.com/competitions/Sections?comp_id=790&section_id=1667).

Podatki, ki sem jih zajela, vključujejo število doseženih in prejetih golov, način doseganja golov ter statistiko vratarjev glede na število tekem brez prejetega gola.

Zajeti podatki so shranjeni v datotekah `goals_for.csv`, `goals_against.csv`, `clean_sheets.csv` in `goal_types.csv`, ki se nahajajo v mapi `podatki/`. Če želite sami ponovno prenesti podatke s spletne strani in ustvariti CSV datoteke, v terminalu poženite datoteko `zajem_podatkov.py`. Celotna analiza podatkov, izračuni in grafični prikazi so na voljo v datoteki `analiza.ipynb`.

V analizi so predstavljene reprezentance z največ doseženimi in najmanj prejetimi goli, načini doseganja golov ter uspešnost vratarjev. Primerjala sem tudi napadalno in obrambno uspešnost reprezentanc, analizirala razliko med številom zadetih in prejetih golov ter raziskala povezavo med številom odigranih tekem in uspešnostjo reprezentanc.

Za uporabo programa potrebujete nameščene knjižnice `requests`, `beautifulsoup4` in `pandas`. 
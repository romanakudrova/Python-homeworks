#Příklad 26
import pandas as pd

zam_praha = pd.read_csv("zam_praha.csv")
zam_plzen = pd.read_csv("zam_plzeň.csv")
zam_liberec = pd.read_csv("zam_liberec.csv")

#Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
zam_praha["mesto"] = "Praha"
zam_plzen["mesto"] = "Plzeň"
zam_liberec["mesto"] = "Liberec"
#print(zam_liberec)

#Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
zamestnanci = pd.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)
#print(zamestnanci)

#načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance
platy_2021_02 = pd.read_csv("platy_2021_02.csv")
zam_platy = pd.merge(zamestnanci, platy_2021_02, how="left", on=["cislo_zamestnance"])
#print(zam_platy)

#Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
zam_platy2 = zam_platy.dropna(subset=["plat"])
print(zam_platy2)

#Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.
print(zam_platy2.groupby("mesto")["plat"].mean())

#Příklad 27
import pandas as pd

tabulka = pd.read_csv("vykazy.csv")

#print(tabulka)

#Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
tabulka2 = tabulka.groupby("project")["hours"].sum()
print(tabulka2)

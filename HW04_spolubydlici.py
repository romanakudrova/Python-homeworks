import math

purchaseList = [
  {"person": "Petr", "item": "Prací prášek", "value": 399},
  {"person": "Ondra", "item": "Savo", "value": 80},
  {"person": "Petr", "item": "Toaletní papír", "value": 65},
  {"person": "Libor", "item": "Pivo", "value": 124},
  {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
  {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
  {"person": "Ondra", "item": "Toaletní papír", "value": 120},
  {"person": "Míša", "item": "Pečící papír", "value": 30},
  {"person": "Zuzka", "item": "Savo", "value": 80},
  {"person": "Pavla", "item": "Máslo", "value": 50},
  {"person": "Ondra", "item": "Káva", "value": 300}
]

#Pokud spolubydlící v našem novém slovníku ještě částku nemá, vložíme tam hodnotu aktuálního nákupu. Pokud tam nějakou částku už má, přičteme k této částce hodnotu aktuálního nákupu.
sum_per_person = {}
for item in purchaseList:
  person = item["person"]
  value = item["value"]
  if person in sum_per_person:
    sum_per_person[person] += value
  else:
    sum_per_person[person] = value

#Vypíšeme si nyní útraty jednotlivých spolubydlících a spočteme celkovou útratu. K tomu můžeme využít cyklus for. 
total_value = 0
for person, value in sum_per_person.items():
  total_value += value
  print(f"{person} utratil(a) za společné nákupy {value} Kč.")

#Určení průměrné hodnoty na osobu
average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")

#Dopiš cyklus, který projde slovník sumPerPerson a pro každého ze spolubydlících vypíše, kolik by měl doplatit (pokud utratil(a) méně než průměr), případně kolik by měl obdržet (pokud utratil(a) více než průměr).

for person, value in sum_per_person.items():
  if value in sum_per_person < average_value:
      difference_doplatit = math.floor((value - average_value))
      print(f"Spolubydlící {person} doplatí {difference_doplatit} Kč.")
  else:
    difference_dostat = math.floor((value - average_value))
    print(f"Spolubydlící {person} dostane {difference_dostat} Kč.")

from turtle import title

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

#Napiš program, který spočte celkový počet stran, které Gustav přečetl.
sum_pages = 0
for item in books:
  sum_pages += item["pages"]
print(f"Gustav celkem přečetl {sum_pages} stran.")

#Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
rate = 0
for item in books:
  if item["rating"] > 7: 
    rate += len(str(item["rating"]))
    
print(f"Počet hodnocených knih hodnotou 8 je: {rate}.")

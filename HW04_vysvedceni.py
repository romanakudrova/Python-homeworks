school_report = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělesná výchova": 3,
  "Chemie": 4,
}

# Napiš program, který spočte průměrnou známku ze všech předmětů.
values = school_report.values()
total = sum(values)
print(f"Součet všech známek je {total}.")

předměty = len(school_report)
print(f"Součet předmětů je {předměty}.")

prumer_znamek = total//předměty
print(f"Průměrná známka ze všech předmetů je {prumer_znamek}.")

# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
for key, value in school_report.items():
  if (value) < 2 :
    print(f'Student získal jedničku z předmětu {key}.')

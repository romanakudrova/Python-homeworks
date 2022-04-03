class Hromadna_doprava:
  def __init__(self, nazev, typ, bezpecnost):
    self.nazev = nazev
    self.typ = typ
    self.bezpecnost = bezpecnost

  def vypis_informace(self):
    return f"Pro typ dopravního prostředku hromadné dopravy {self.nazev} typu {self.typ} se udává bezpečnost {self.bezpecnost} mrtvých pasažérů na 1 miliardu ujetých mílích."

#Dědičnost: uhlíková stopa pro letadlo

class Letadlo(Hromadna_doprava):
  def __init__(self, nazev, typ,  bezpecnost, uhlikova_stopa):
    super().__init__(nazev, typ, bezpecnost)
    self.uhlikova_stopa = uhlikova_stopa
 
  def __str__(self):
    return f"Pro typ dopravního prostředku {self.nazev} typu {self.typ} se udává bezpečnost {self.bezpecnost} mrtvých pasažérů na 1 miliardu ujetých mílích. Ekologický parametr uhlíková stopa je {self.uhlikova_stopa}kg/100km."

autobus = Hromadna_doprava("autobus", "Carrosa", 0.11)
letadlo = Letadlo("letadlo", "A220", 0.07, 12)
print(autobus.vypis_informace())
print(letadlo)

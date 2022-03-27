import random
import string
import sys

def user_registration():
  print("Pro registraci napiš svoje jméno:")
  name = input()
  print("Uživatelské jméno je " + name + ". ")

user_registration()

#Uživatel zadá věk, pomocí výjimek bude ověřeno, že uživatel zadal číslo

age = input("Zadej vek: ")
try:
  age = int(age)
  print((age))
except (ValueError, IndexError):
  print("Zadej číslo!" + input("Zadej věk ve formátu čísla: "))

def get_random_string(length):
#Heslo s počtem znaků 8 bude obsahovat malá i velká písmena a čísla a speciální znaky
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    #Print nahodny retezec
    print("Náhodně generované heslo je:", password)

get_random_string(8)

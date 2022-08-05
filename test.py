
#PRESENTACIÓN DESARROLLADOR

word = "Desarrollado por Tabaré San Martín"
value = word.center(60, "-")
from colorama import Fore, Style, init
init(convert=True)
print(Fore.BLUE + (value))

#
word = "Prueba de edad"
value = word.center(60, "-")
print(value)
import datetime
print(datetime.date.today())

x = input("Ingresa su edad: ")
Analisis = int(x)

if Analisis < 10:
    print("Usted es un niño/a")
if Analisis >= 11 and Analisis <= 17:
    print("Usted es un adolecente")
if(not(Analisis >= 18)):
    print("NO AUTORIZADO PARA MENORES DE 18")
if Analisis >= 18:
    print("Bienvenido")



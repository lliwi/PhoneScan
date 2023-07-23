from colorama import Fore, init
init(autoreset=True)
from proceso.motor.scrapeo import *
def enviar (n):
    n = n.replace("+", "")
    n = n.replace(" ", "")
    n = n.replace("(", "")
    n = n.replace(")", "")
    n = n.replace("-", "")
    if(len(n) < 7):
        print(Fore.RED+"Le faltan numeros a este telefono.")
        return
    pais = n[0:2]
    numero = n[2:20]
    print (Fore.GREEN + "enviando...")
    scra(pais, numero)

from proceso.motor.dorkeo import *
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
init(autoreset=True)
import json

def scra(p, n):
    print(Fore.LIGHTMAGENTA_EX +"Resultados del escaneo:")
    number = p[0:3]+n
    api_key = "API_LAYER_KEY"
    url = "https://api.apilayer.com/number_verification/validate?number="+number
    headers = {"apikey": api_key}
    r = requests.get(url, headers=headers)
    j = json.loads(r.text)
    
    valid = j.get('valid', False)

    if not valid:
        print(Fore.RED + 'El numero que introduciste no es real :(')
    else:
        va = "Verdadero"
        print(Fore.LIGHTGREEN_EX + 'Numero valido: '+ va)
        print(Fore.LIGHTGREEN_EX + 'Pais del numero: '+ j['country_name'])
        print(Fore.LIGHTGREEN_EX + 'Locacion del numero:'+ j['location'])
        print(Fore.LIGHTGREEN_EX + 'Numero en formato Nacional:' + j['local_format'])
        print(Fore.LIGHTGREEN_EX + 'Numero en formato Internacional:' +j['international_format'])
        print(Fore.LIGHTGREEN_EX + 'Prefijo del pais:' +j['country_prefix'])
        print(Fore.LIGHTGREEN_EX + 'Compañia del telefono:' + j['carrier'] )
        print(Fore.LIGHTGREEN_EX + 'Tipo de numero:' +j['line_type'])
        dorkeo(p, n)
    

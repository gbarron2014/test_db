"""
Descripción de la API: Generación de nuevas appis
Autor: Castillo Aviles Jessica
Fecha de creación: 08 de noviembre 2022
"""
#DESCRIPCIÓN DE LA API
"""***********************************
Nombre de la API: Newsapi
Descripción de la API: Generación de nuevas apis
API Portal / Home Page: https://newsapi.org/?ref=apilist.fun
***********************************"""

import urllib.parse
import requests


main_api = "https://newsapi.org/v2/everything?"
key ="5b94ced77f8c4b43b1ba1e18b8ebd487"
q = 'Apple'
orig = '2022-11-10'
sortBy = 'popularity'


url = main_api + urllib.parse.urlencode({ "q": q, "apiKey":key, "from":orig})
print("URL: " + (url))


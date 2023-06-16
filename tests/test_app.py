import requests

#CONFIGURAR LA PETICION COMO SI FUERA UN NAVEGADOR, ENCABEZADO DE NAVEGADOR
user_agent = {'User-agent':'Mozilla/5.0'}
symbol = "DIS" # Ticker de Disney
url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
r = requests.get(url,headers = user_agent)

#IMPRIME TODO LO QUE TIENE EL LINK
print(r.json())

#DICCIONARIO QUE ALMACENA SOLO LOS PARAMETROS QUE NECESITAMOS DEL LINK
my_data_selection = {
    "nombre": r.json()["quoteSummary"]["result"][0]["price"]["shortName"],
    "ticker": r.json()["quoteSummary"]["result"][0]["price"]["symbol"],
    "precio": r.json()["quoteSummary"]["result"][0]["summaryDetail"]["previousClose"]["raw"]
}

#IMPRIME EL DICCIONARIO ALMACENADO
print(my_data_selection)


import requests

def currency_rates(code: str) -> float:
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    fx_data = {}
    list_cur = response.text.split('ID=')
    del list_cur[0]
    for i in list_cur:
        currency_v = i[(i.find('<Value>')+7):i.find('</Value>')]
        currency_v = float(currency_v.replace(',', '.'))
        nominal_v = int(i[(i.find('<Nominal>')+9):i.find('</Nominal>')])
        fx_data[(i[(i.find('<CharCode>')+10):i.find('</CharCode>')])] = currency_v/nominal_v
    result_value = fx_data.get(code.upper())
    return result_value


import requests

def currency_rates(code: str) -> float:
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    v_data = []
    n_data = []
    cur_data = []
    code_1 = code.upper()
    list_cur = response.text.split('ID=')
    del list_cur[0]
    for i in list_cur:
        currency_v = i[(i.find('<Value>') + 7):i.find('</Value>')]
        currency_nom = int(i[(i.find('<Nominal>') + 9):i.find('</Nominal>')])
        currency_v_2 = float(currency_v.replace(',', '.'))
        currency_name = i[(i.find('<CharCode>') + 10):i.find('</CharCode>')]
        v_data.append(currency_v_2)
        n_data.append(currency_nom)
        cur_data.append(currency_name)
    if code_1 in cur_data:
        result = v_data[cur_data.index(code_1)] / n_data[cur_data.index(code_1)]
    else:
        result = 'None'
    result_value = result
    return result_value

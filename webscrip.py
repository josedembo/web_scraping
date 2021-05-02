from bs4 import BeautifulSoup as bp
import requests
import csv


csv_file = open('./dados/fornecedores/fornecedores.csv',
                'w', newline='', encoding='utf-8')
csv_write = csv.writer(csv_file)
csv_write.writerow(['id', 'empresa', 'telefone', 'site', 'email'])

url = 'http://www.abimad.com.br/associados/pesquisar#menu-top'

r = requests.get(url)

sup = bp(r.content, 'html.parser')

todos_elementos = sup.find_all('figure')

id = 0

for elemento in todos_elementos:
    empresa = elemento.h5.text
    telefone = elemento.find(
        'i', class_='fa-phone').next_element.next_element.text
    site = elemento.find('i', class_='fa-link').next_element.next_element.text
    email = elemento.find('i', class_='fa-at').next_element.next_element.text

    csv_write.writerow([id, empresa, telefone, site, email])
    id += 1

csv_file.close()

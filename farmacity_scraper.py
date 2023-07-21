import requests
from bs4 import BeautifulSoup

def scrape_farmacity():
    url = "https://www.farmacity.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_prices = {}

    # Aquí puedes buscar los elementos HTML específicos que contienen los precios de los productos
    # Por ejemplo, si los precios se encuentran dentro de elementos <div> con una clase determinada, puedes hacer algo como:
    product_elements = soup.find_all('div', class_='product-item')
    
    for product_element in product_elements:
        product_name = product_element.find('h2', class_='product-title').text.strip()
        product_price = product_element.find('span', class_='product-price').text.strip()
        product_prices[product_name] = product_price

    return product_prices

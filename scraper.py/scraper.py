import requests
from bs4 import BeautifulSoup
import json

# URL of the ecommerce page
url = "https://cartonera-caracas.ola.click/products"

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:

    html_content = response.text
    
    # Specify the file name where you want to save the content
    file_name = 'web_response.txt'
    
    # Open the file in write mode and save the content
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product names (adjust the selector based on the website's structure)
    product_names = soup.find_all('div', class_='product-card__title-tag d-flex')  # Replace 'h2' and 'product-name' with the correct tags and classes

    # Extract and print the product names
    for product in product_names:
        print(product.text.strip())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
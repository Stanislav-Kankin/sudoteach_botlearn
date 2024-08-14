import requests
from bs4 import BeautifulSoup
number = 89139390033
url = f'https://nums.hanumi.net/api/get_info?phone={number}'

response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")


print(soup)
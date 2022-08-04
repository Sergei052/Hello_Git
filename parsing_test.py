import requests
from bs4 import BeautifulSoup



# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
# }
# req = requests.get(url, headers=headers)
# src = req.text  # получаю код страницы
# # print(src)
#
# with open("index.html", "w") as file:   # сохраняю код страницы в файл
#     file.write(src)
# так как код запроса уже не нужен, закомментирую его

with open("index.html") as file:
     src = file.read()

soup = BeautifulSoup(src, "lxml")   # создал переменную в которую передал, в качестве параметров парсер lxml и переменную src
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")  # в качестве параметра передал класс ссылок
for i in all_products_hrefs:
     i_text = i.text
     i_href = i.get('href')
     print(f"{i_text}: {i_href}")
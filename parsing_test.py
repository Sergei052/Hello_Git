import requests
from bs4 import BeautifulSoup
import json



# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}
# req = requests.get(url, headers=headers)
# src = req.text  # получаю код страницы
# # print(src)
#
# with open("index.html", "w") as file:   # сохраняю код страницы в файл
#     file.write(src)
# # так как код запроса уже не нужен, закомментирую его

# with open("index.html") as file:
#      src = file.read()
#
# soup = BeautifulSoup(src, "lxml")   # создал переменную в которую передал, в качестве параметров парсер lxml и переменную src
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")  # в качестве параметра передал класс ссылок
#
# all_categories = {}  # создал словарь, куда сохранил категории товаров и ссылки на них
# for i in all_products_hrefs:
#      i_text = i.text
#      i_href = 'https://health-diet.ru' + i.get('href')
#
#      all_categories[i_text] = i_href
#
# with open('all_categories.json', "w") as file:
#      json.dump(all_categories, file, indent=4, ensure_ascii=False)  # и сохранил словарь в json файл

with open('all_categories.json') as file:
     all_categories = json.load(file)

count = 0
for category_name, category_href in all_categories.items():

    rep = [",", " ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html", "w") as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")


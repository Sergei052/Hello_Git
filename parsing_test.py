# Собираю данные о калорийности продуктов со страниц сайта
import requests
from bs4 import BeautifulSoup
import json
import csv


# # ссылка на страницу
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# # передал Accept и User-Agent, потому что я не бот, и убери от меня эту CAPTCHA ))))
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}
# # получаю код страницы
# req = requests.get(url, headers=headers)
# # сохраняю в переменную src полученный объект, и вызываю метод text, для того что бы получить код страницы
# src = req.text
# # print(src)

# # сохраняю код страницы в файл
# with open("index.html", "w", encoding='UTF-8') as file:
#     file.write(src)
# # так как код запроса уже не нужен, закомментирую его
#
# # открываю файл и сохраняю код страницы в переменную
# with open("index.html") as file:
#      src = file.read()
#
# # создаю переменную в которую передал, в качестве параметров парсер lxml и переменную src
# soup = BeautifulSoup(src, "lxml")
# # в качестве параметра передал класс ссылок
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
#
# # создаю словарь, куда сохранил категории товаров и ссылки на них
# all_categories = {}
# for i in all_products_hrefs:
# # создаю две переменные: с названием категории и ссылкой на неё
#      i_text = i.text
#      i_href = 'https://health-diet.ru' + i.get('href')
#
#      all_categories[i_text] = i_href
#
# # и сохраняю словарь в json файл
# with open('all_categories.json', "w") as file:
#      json.dump(all_categories, file, indent=4, ensure_ascii=False)

with open('all_categories.json') as file:
     all_categories = json.load(file)
# создаю переменную которая будет считать количество страниц категорий
iteration_count = int(len(all_categories)) - 1
count = 0
print(f'Всего итераций: {iteration_count}')
# создаю цикл, на каждой итерации которой буду заходить на новую страницу категории,
# собирать с неё данные о товарах и нутриентах, и записывать всё в файл
for category_name, category_href in all_categories.items():
    # запросы на странице, для работы с ними раскомментирую заголовки
    req = requests.get(url=category_href, headers=headers)
    src = req.text
    # создаю папку data в рабочей директории, что бы сохранять туда полученные данные, а переменная count
    # будет обеспечивать нумерацию файлов, и сохраняю страницу под именем категории
    with open(f"data/{count}_{category_name}.html", "w", encoding='UTF-8') as file:
        file.write(src)
    # открываю и сохраняю код страницы в переменную src
    with open(f"data/{count}_{category_name}.html", encoding='UTF-8') as file:
        src = file.read()
    # создаю объект soup
    soup = BeautifulSoup(src, "lxml")
    # проверяю страницу на наличие таблицы, что бы не вызывать ошибку
    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue
    # собираю заголовки таблицы, так как это список, извлекаю элементы обращаясь к ним по индексам
    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    # сохраняю полученные данные в таблицу csv
    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        # объединяю аргументы в кортеж, и спомощью метода writer.writerow записываю файл в строку,
        # формируя таким образом таблицу
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    # собираю данные продуктов
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
    # создаю пустой список, в который буду добавлять данные на каждой итерации цикла, а затем записываю все в json файл
    product_info = []
    # циклом собираем td теги в tr тегах, в которых содержится нужная информация
    for item in products_data:
        product_tds = item.find_all('td')
        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text
        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )
        # запишем полученные данные в csv файл
        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
    with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)
    count += 1
    # делаю красоту)))
    print(f'Итерация № {count}. {category_name}')
    iteration_count = iteration_count - 1
    if iteration_count == 0:
        print('Работа завершена')
        break
    print(f'Осталось итераций: {iteration_count}')

# В результате работы мы имеем три файла на каждый тип продукта в папке data:
# json файл, csv таблицу, и html код страницы с таблицей


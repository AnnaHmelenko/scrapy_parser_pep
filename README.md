# [Проект scrapy_parser_pep.](https://github.com/AnnaHmelenko/scrapy_parser_pep)

## Оглавление

- [Технологии](#технологии)
- [Описание проекта](#Описание-проекта)
- [Запуск проекта](#Запуск-проекта)
- [Примеры команд](#Примеры-команд)
- [Автор](#Автор)



## Технологии:

- Python 3.12
- Scrapy 2.11.2
- Twisted 22.2.0

## Описание проекта:

Парсер документов [PEP](https://peps.python.org/) на базе фреймворка Scrapy.

### Запуск проекта:
Клонируйте [репозиторий](https://github.com/AnnaHmelenko/scrapy_parser_pep) и перейдите в него в командной строке:
```
git clone https://github.com/AnnaHmelenko/scrapy_parser_pep

cd scrapy_parser_pep
```
Создайте виртуальное окружение и активируйте его:
```
python -m venv vevn

source venv/Scripts/activate
```
Обновите pip:
```
python -m pip install --upgrade pip
```
Установите зависимости:
```
pip install -r requirements.txt
```
Проект готов к работе!

## Примеры команд
Создает в папке results два файла:

1) pep_ДатаВремя.csv - csv файл со списком всех PEP
2) status_summary_ДатаВремя.csv - csv файл с таблицей из двух колонок «Статус» и «Количество»
```
scrapy crawl pep
```




## Автор

[Анна Хмеленко](https://github.com/AnnaHmelenko)

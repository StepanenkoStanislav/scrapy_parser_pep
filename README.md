# Проект парсинга документации Python с использованием Scrapy

## Описание проекта
 Парсер документации Python собирает информацию о PEP и выводит ее в два файла:
 - pep_ДатаВремя.csv - список всех PEP: номер, название, статус.
 - status_summary_ДатаВремя.csv - сводка по статусам PEP - сколько найдено
документов в каждом статусе (статус, количество).

Результаты сохраняются в директорию _results_ в директории проекта.


## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Запуск

Находясь в директории _scrapy_parser_pep_ в терминале необходимо выполнить команду:

`scrapy crawl pep`

## Пример запуска

В директории scrapy_parser_pep в терминале

`pip install -r requirements.txt`

`scrapy crawl pep`


## Технологии

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="python" alt="python" width="40" height="40"/>&nbsp
</div>

В проекте используются следующие технологии:

- Python 3.7
- Scrapy 2.5.1

## Автор

[![Telegram Badge](https://img.shields.io/badge/StepanenkoStanislav-blue?logo=telegram&logoColor=white)](https://t.me/tme_zoom) [![Gmail Badge](https://img.shields.io/badge/-Gmail-red?style=flat&logo=Gmail&logoColor=white)](mailto:stepanenko.s.a.dev@gmail.com)

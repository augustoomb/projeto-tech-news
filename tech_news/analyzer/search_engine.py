from tech_news.database import search_news
from datetime import datetime


def str_to_date(str_iso_date):
    return datetime.strptime(str_iso_date, "%Y-%m-%d")


def format_date(obj_date):
    day = obj_date.strftime("%d")
    month = obj_date.strftime("%m")
    year = obj_date.strftime("%Y")

    return f"{day}/{month}/{year}"


def search_in_database(query):
    result = search_news(query)
    return [(news["title"], news["url"]) for news in result]


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    return search_in_database(query)


# Requisito 7
def search_by_date(date):
    try:
        obj_date = str_to_date(date)
        formated_date = format_date(obj_date)

        query = {"timestamp": {"$regex": formated_date}}
        return search_in_database(query)

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    return search_in_database(query)


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    return search_in_database(query)


# Fontes:

#     https://stackoverflow.com/questions/10610131/
#       checking-if-a-field-contains-a-string

from tech_news.database import search_news
from datetime import datetime


def str_to_date(str_iso_date):
    return datetime.strptime(str_iso_date, "%Y-%m-%d")


def format_date(obj_date):
    day = obj_date.strftime("%d")
    month = obj_date.strftime("%m")
    year = obj_date.strftime("%Y")

    return f"{day}/{month}/{year}"


# Requisito 6
def search_by_title(title):
    # query = {"title": title}
    query = {"title": {"$regex": title, "$options": "i"}}
    result = search_news(query)
    list_obj = [(news["title"], news["url"]) for news in result]
    return list_obj


# Requisito 7
def search_by_date(date):
    try:
        obj_date = str_to_date(date)
        formated_date = format_date(obj_date)

        query = {"timestamp": {"$regex": formated_date}}
        result = search_news(query)
        list_obj = [(news["title"], news["url"]) for news in result]
        return list_obj

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    result = search_news(query)
    list_obj = [(news["title"], news["url"]) for news in result]
    return list_obj


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


print(search_by_tag("Tecnologia"))

# Fontes:

#     Req6: https://stackoverflow.com/questions/10610131/
#       checking-if-a-field-contains-a-string

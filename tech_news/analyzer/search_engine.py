from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # query = {"title": title}
    query = {"title": {"$regex": title, "$options": "i"}}
    result = search_news(query)
    list_obj = [(news["title"], news["url"]) for news in result]
    return list_obj


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# print(search_by_title("bacana"))

# Fontes:

#     Req6: https://stackoverflow.com/questions/10610131/
#       checking-if-a-field-contains-a-string

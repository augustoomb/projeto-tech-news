from tech_news.database import get_collection


# Requisito 10
# https://www.mongodb.com/docs/manual/reference/method/db.collection.aggregate/
# https://pymongo.readthedocs.io/en/stable/examples/aggregation.html
# https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/
def top_5_news():
    pipeline = [
        {"$sort": {"comments_count": -1, "title": 1}},
        {"$limit": 5},
        {"$project": {"title": 1, "url": 1, "_id": 0}},
    ]

    collection = list(get_collection().aggregate(pipeline))

    return collection


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""


print(top_5_news())

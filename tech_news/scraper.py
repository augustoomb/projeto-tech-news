import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Aux requisito 4
def join_string(str):
    return "".join(str)


# Aux requisito 4
def remove_suffixes(str):
    suffixes = " "
    str_return = ""
    if str.endswith(suffixes):
        str_return = str[: -len(suffixes)]
    else:
        str_return = str
    return str_return.replace("\xa0", "")
    # try:
    #     if str.endswith(suffixes):
    #         str_return = str[: -len(suffixes)]
    #     else:
    #         str_return = str
    #     return str_return.replace("\xa0", "")
    # except ValueError:
    #     return str
    # except AttributeError:
    #     return str


# Aux requisito 4
def set_comments_count(news, selector):
    try:
        news["comments_count"] = int(
            selector.css(".post-comments h5::text").get()
        )
    except TypeError:
        news["comments_count"] = 0
    except ValueError:
        news["comments_count"] = 0


# Aux requisito 4
def set_summary(news, selector):
    paragraph = selector.css(".entry-content p").get()
    selectorParagraph = Selector(text=paragraph)
    summary_list = selectorParagraph.css("*::text").getall()
    summary_string = join_string(summary_list)
    news["summary"] = remove_suffixes(summary_string)


# Aux requisito 4
def set_tags(news, selector):
    tags = selector.css(".post-tags ul li a::text").getall()
    try:
        # news["tags"] = tags.split(" - ")
        news["tags"] = tags
    except AttributeError:
        news["tags"] = []
        pass


# Aux requisito 5
def mount_list_links(n):
    next_page_url = "https://blog.betrybe.com"
    links_news = []
    while next_page_url and (len(links_news) < n):
        content = fetch(next_page_url)
        links_news = links_news + scrape_updates(content)
        next_page_url = scrape_next_page_link(content)

    # Aqui já tenho a lista de links de noticias.
    # Há links a mais do que o pedido em n.
    # Devo acertar para o numero exato (n)
    return links_news[0:n]


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links = selector.css(".cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link_next_page = selector.css(".next::attr(href)").get()
    return link_next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    news = {}

    news["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    news["title"] = remove_suffixes(selector.css(".entry-title::text").get())
    news["timestamp"] = selector.css(".meta-date::text").get()
    news["writer"] = selector.css(".author a::text").get()
    set_comments_count(news, selector)
    set_summary(news, selector)
    set_tags(news, selector)
    news["category"] = selector.css(".category-style span.label::text").get()

    return news


# Requisito 5
def get_tech_news(n):
    list_links = mount_list_links(n)
    list_obj_news = []

    for link in list_links:
        content = fetch(link)
        list_obj_news.append(scrape_news(content))

    create_news(list_obj_news)

    return list_obj_news


# .......................................................
# TESTANDO FUNÇÕES
# .......................................................

# req1 = fetch("https://blog.betrybe.com")
# print(scrape_updates(req1))

# req1 = fetch(
#     # "https://blog.betrybe.com/noticias/bill-gates-e-cetico-sobre
# -criptomoedas-e-nfts-entenda-o-motivo/"
#     # "https://blog.betrybe.com/carreira/passos-fundamentais
# -para-aprender-a-programar/"
#     "https://blog.betrybe.com/carreira/fazer-curriculo-no-word-em-pdf/"
# )
# print(scrape_news(req1))

# get_tech_news(13)

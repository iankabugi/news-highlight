import urllib.request, json
from .models import Source, Article

# getting api key
api_key = None

# getting the source base url
base_url = None

# getting the articles base url
base_url2 = None


def configure_request(app):
    global api_key, base_url, base_url2
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    base_url2 =app.config['NEWS_API_BASE_URL2']

def get_source(newss):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(newss,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results


def process_results(source_list):
    '''
    Function  that processes the source result and transforms them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')


        if name:
            source_object = Source(id, name, description, url, category, language, country)
            source_results.append(source_object)

    return source_results


def get_article(articles):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url2.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)


    return article_results


def process_articles(article_list):
    '''
    Function  that processes the article result and transforms them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('source')
        name = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToimage = article_item.get('urlToimage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')


        if title:
            article_object = Article(id, name, author, title, description, url, urlToimage, publishedAt, content)
            article_results.append(article_object)

    return article_results

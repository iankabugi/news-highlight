class Source:
    '''
    News source class to define news source objects
    '''
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Article:
    '''
    News article class to define news article objects
    '''
    def __init__(self, id, name, author, title, description, url, urlToimage, publishedAt, content):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToimage = urlToimage
        self.publishedAt = publishedAt
        self.content = content

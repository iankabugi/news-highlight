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


class Source:
    '''
    Source class to define Objects
    '''

    def __init__(self,id,name,description):
        self.id =id
        self.name = name
        self.description = description




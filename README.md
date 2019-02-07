# News-highlight

## Description
 This is flask project that was ment for mainly people whoare busy and need a news app tha tells them whats happening around the world in just a click of the button.I have done using fkask a microframework for python.
## Author

 **Ian Kabugi** 
 
### Pre-requisites
* [Python 3.7.2](https://www.python.org/)
* preferred IDE


### Steps
* Clone the app to a directory:
    git clone https://github.com/iankabugi/news-highlight.git

* Install app dependencies:
    pip install -r requirements.txt
* Run program on terminal:
    chmod a+x start.sh
* Run script:
    ./start.sh
### User Stories

* A user should see various news sources on the homepage.
* A user should see all news articles from a selected news source.
* A user should see the image, description and time that an article was created.
* A user should be able to read the full article on the sources website.

### In addition:

* A user should be able to search for articles according to the source name.
* A user should not lose news articles snippet on relaunch of the app (flask sessions).
* A user should have a favourites section where they will be able to add their favourite news sources and store them in a browser cookie.

### BDD
|     | Behaviour    |          Input                  | Output    | 
|------| --------------------|---------------|------------------
|  1. | display a menu with navigation options    | click on home,news and try me     | redirect to relevant page     |
|  2. | display news articles | select an article and pree button go to full a....   | taken to the actual article|
|  3. | display articles from sources   | click the sources page      | redirect to artcle news sources  |


## Credits

**Powered by** [ NEWS API](https://newsapi.org/)

##licence

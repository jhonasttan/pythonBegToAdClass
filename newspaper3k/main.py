'''
    Author: Jhonasttan Regalado
    Copyright: 20180414
    Script: Quick use of Python library newspaper3k
    requirements: https://pypi.python.org/pypi/newspaper3k/0.1.5
        From the requirements site, below is a quick shortcut for OSX users (like me):
            $ brew install libxml2 libxslt
            $ brew install libtiff libjpeg webp little-cms2
            $ pip3 install newspaper3k
            $ curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3
            # for anaconda users:
                $ conda install -c conda-forge newspaper3k

'''
from newspaper import Article

url = "http://opensourceforu.com/2016/02/ionic-a-ui-framework-to-simplify-hybrid-mobile-app-development/"

article = Article(url)

#1. Download the article
article.download()

#2. Parse the article
article.parse()

#3. Fetch Author Names
print(article.authors)

#4 Fetch Publication Date
print("Article Publication Date:")
print(article.publish_date)
#5. The URL of the Major Image
print("Major Image in the article:")
print(article.top_image)

#6. Natural Language Processing on Article to fetch keywords
article.nlp()
print("Keywords in the article")
print(article.keywords)

#7. Generate article summary
print("Article Summary:")
print(article.summary)

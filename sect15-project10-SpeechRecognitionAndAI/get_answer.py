import time

from newspaper import Article

class Fetcher:
    def __init__(self, url):
        self.url = url
        self.article = Article(self.url)

    def lookup(self):
        # 1. Download the article
        self.article.download()

        # 2. Parse the article
        self.article.parse()

        # 3. Fetch Author Names
        print(self.article.authors)

        # 4 Fetch Publication Date
        print("Article Publication Date:")
        print(self.article.publish_date)
        # 5. The URL of the Major Image
        print("Major Image in the article:")
        print(self.article.top_image)

        # 6. Natural Language Processing on Article to fetch keywords
        self.article.nlp()
        print("Keywords in the article")
        print(self.article.keywords)

        # 7. Generate article summary
        print("Article Summary:")
        print(self.article.summary)
        answer = self.article.summary
        answer = answer.replace("\n", " ").replace('\r', '')
        print(type(answer))
        print(answer)
        return answer
        #return ' '.join(answer)
        #return ' '.join(word[0] for word in answer)

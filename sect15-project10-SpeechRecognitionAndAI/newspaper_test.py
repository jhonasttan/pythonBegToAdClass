from newspaper import Article

url = "https://www.google.com/search?ei=cd3jWon7GOqm_QbUpoToBw&q=what+is+a+penis&oq=what+is+a+penis"

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
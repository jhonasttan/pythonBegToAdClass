MongoDB OSX setup:
1. Installation - From terminal, run command -> 'brew install mongodb'
2. Run services -> 'brew services start mongodb'
3. To check if it is running -> 'curl http://localhost:27017'
4. MongoDB Manual Contents -> https://docs.mongodb.com/manual/contents/

Lesson 67:
In [1]: import pymongo

In [2]: from pymongo import MongoClient

In [3]: client = MongoClient()

In [4]: db = client.pytests
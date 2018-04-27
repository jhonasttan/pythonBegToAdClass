import subprocess
import os

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.response("You haven't told me your name yet.")
            else:
                self.response("My name is python commander. How are you?")

    def response(self, response):
        print(response)
        subprocess.call('say '+ response, shell=True)

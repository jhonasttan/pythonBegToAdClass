import simplejson as json #can install packages via the Pycharm project preferences window
import os

file_name = "./ages.json"

if os.path.isfile(file_name) and os.stat(file_name).st_size != 0:
    old_file = open(file_name, "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
else:
    old_file = open(file_name, "w+")
    data = {"name": "Nick", "age": 27}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))

newfile = open("newfile.txt", "w+")

string = "this is the content that will be written to the text file."

newfile.write(string)
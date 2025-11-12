import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
for index, item in enumerate(data):
    print(item["title"])
input("would you like to see the movies released after 1990? ")
x = input
if input == "yes":
    print (item["title"]) > 1990
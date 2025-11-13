import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index, item in enumerate(data):
    print(index, item["title"])

def database():
    input("would you like to see the movies released after 1990? ").lower()
    print(input)
    if (index, item["year"]) >= 1990:
        for index, item in enumerate(data):
            print(item["title"])
database()
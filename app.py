import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index, item in enumerate(data):
    print(index, item["title"])

def database():
    year = int(input("enter a year: "))
    print("movies released after", year, ":")
    for item in data:
        if item["year"] > year:
            print(item["title"])
database()

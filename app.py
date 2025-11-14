import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

## File 1:
for index, item in enumerate(data):
    print(item["title"])

## File 2 and 3:
def database():
    year = int(input("enter a year: "))
    print("movies released after", year,":")
    for item in data:
        if item["year"] > year:
            print(item["title"])
database()

def database():
    year = int(input("enter a year: "))
    print("movies released b4", year,":")
    for item in data:
        if item["year"] < year:
            print(item["title"])
database()

## File 4:
def database():
    year = int(input("enter a year: "))
    print("movies released in", year,":")
    for item in data:
        if item["year"] == year:
            print(item["title"])
database()
import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def database():

    ## File 1:
    for index, item in enumerate(data):
        print(item["title"])

      ## File 2:
    def after():
        year = int(input("enter a year: "))
        print("movies released after", year,":")
        for item in data:
            if item["year"] > year:
                print(item["title"])
    after()

    ## File 3;
    def before():
        year = int(input("enter a year: "))
        print("movies released b4", year,":")
        for item in data:
            if item["year"] < year:
                print(item["title"])
    before()

    ## File 4:
    def inyear():
        year = int(input("enter a year: "))
        print("movies released in", year,":")
        for item in data:
            if item["year"] == year:
                print(item["title"])
    inyear()

    ## File 5:
    def search():
        input("search for a movie: ")
        if any(chr in chr(input)) == (item["title"] in index):
                for index, item in enumerate(data):
                    print(item["title"])
    search()
    
    ## File 6:
    
database()
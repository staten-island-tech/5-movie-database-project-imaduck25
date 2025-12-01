import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def database():
    ## 1
    for index, item in enumerate(data):
        print(item["title"])
    ## 2
    def after():
        year = (input("enter a year: "))
        if not year.isdigit():
            return "invalid year"
        print("movies released after", year,":")
        for item in data:
            if item["year"] > year:
                print(item["title"])
    after()
    ## 3
    def before():
        year = (input("enter a year: "))
        if not year.isdigit():
            return "invalid year"
        print("movies released b4", year,":")
        for item in data:
            if item["year"] < year:
                print(item["title"])
    before()
    ## 4
    def inyear():
        year = (input("enter a year: "))
        if not year.isdigit():
            return "invalid year"
        print("movies released in", year,":")
        for item in data:
            if item["year"] == year:
                print(item["title"])
    inyear()
    ## 5
    def search():
        m = input("search for a movie: ").lower().strip()
        if not m:
            return "invalid search"
        print("search results for:", m)
        for item in data:
            if m in item["title"].lower():
                print(item["title"])
    search()
    ## 6
    def genre_search():
        g = input("enter a genre: ").lower().strip()
        if not g:
            return "invalid genre search"
        print("movies in genre:", g)
        for item in data:
          if "genre" in item and g in item["genre"].lower():
                print(item["title"])
    genre_search()  
database()
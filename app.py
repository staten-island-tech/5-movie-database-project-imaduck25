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
        while True:
            year_input = input("enter a year (after): ").strip()
            if year_input.isdigit():
                year = int(year_input)
                if 1961 <= year <= 2023:
                    break
            print("invalid year. please enter a year between 1961 and 2023.")
        print("movies released after", year, ":")
        for item in data:
            if item["year"] > year:
                print(item["title"])
    after()
    ## 3
    def before():
        while True:
            year_input = input("enter a year (b4): ").strip()
            if year_input.isdigit():
                year = int(year_input)
                if 1961 <= year <= 2023:
                    break
            print("invalid year. please enter a year between 1961 and 2023.")
        print("movies released b4", year, ":")
        for item in data:
            if item["year"] < year:
                print(item["title"])
    before()
    ## 4
    def inyear():
        while True:
            year_input = input("enter a year (in year): ").strip()
            if year_input.isdigit():
                year = int(year_input)
                if 1961 <= year <= 2023:
                    break
            print("invalid year. please enter a year between 1961 and 2023.")


        print("movies released in", year, ":")
        for item in data:
            if item["year"] == year:
                print(item["title"])
    inyear()
    ## 5
    def search():
        while True:
            m = input("search for a movie: ").lower().strip()
            if not m:
                print("invalid search")
                continue
            print("search results for:", m)
            results = []
            for item in data:
                if m in item["title"].lower():
                    results.append(item["title"])
            if results:
                for title in results:
                    print(title)
                break
            else:
                print("no movies matched your search.")
    search()
    ## 6
    def genre_search():
        while True:
            g = input("enter a genre: ").lower().strip()
            if not g:
                print("invalid genre search")
                continue
            print("movies in genre:", g)
            results = []
            for item in data:
                for genre in item.get("genres", []):
                    if g in genre.lower():
                        results.append(item["title"])
            if results:
                for title in results:
                    print(title)
                break
            else:
                print("no genres matched your search.")
    genre_search()
database()

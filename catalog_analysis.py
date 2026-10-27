import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def main():
    print("Hello from dz-catalog-analysis-pushkareva!")
    print(top_n_by_rating(movies))

def average_rating(movies):
    ttl = 0
    for movie in movies:
        ttl += movie["rating"]
    return round(ttl / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    most_old = current_year - movies[0]["year"]
    most_new = current_year - movies[0]["year"]
    med = 0

    for movie in movies:
        age = current_year - movie["year"]
        if age > most_old:
            most_old = age
        if age < most_new:
            most_new = age

        med += age
    return (most_old, most_new, math.ceil(med / len(movies)))

def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"

def rating_tier(rating):
    if rating < 5:
        return "слабо"
    # elif 6.9 >= rating >= 5:
    #     return "средне"
    # elif 8.9 >= rating >= 7:
    #     return "хорошо"
    elif rating >= 9:
        return "шедевр"

    return "средне" if 6.9 >= rating >= 5 else "хорошо"

def decade_label(year):
    match year:
        case _ if year >= 2020:
            return "новые"
        case _ if 2020 > year >= 2015:
            return "недавние"
        case _ if 2015 > year:
            return "старые"

def print_not_comedies(movies):
    for movie in movies:
        if "comedy" not in movie["genres"]:
            continue
        else:
            print(movie["title"])

def find_wow(movies):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    ttl = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            ttl += 1
    return ttl

def normalize_title(title):
    title_words = title.split()
    words = []
    for word in title_words:
        words.append(word[0].upper() + word[1:])
    return " ".join(words)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    return f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}, {duration_in_hours(movie["duration_min"])}, жанры: {" ".join(sorted(movie["genres"]))}'

def titles_sorted_by_rating(movies):
    return sorted(movies, key=lambda m: m["rating"], reverse=True)

def top_n_by_rating(movies, n=3):
    movies_top_raiting = titles_sorted_by_rating(movies)[:n]
    var = ()
    for movie in movies_top_raiting:
        var += (movie["title"], movie["rating"])
    return var

if __name__ == "__main__":
    main()

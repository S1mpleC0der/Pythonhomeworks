import requests
import random

API = '5733bcb6af90c59b5061060a5c19e4bc'
URL = 'https://api.themoviedb.org/3'
searching_URL = f"{URL}/genre/movie/list"

parametrs = {
    'api_key':API,
    'language':'en-US'
}

response = requests.get(searching_URL, params=parametrs)

genres = response.json().get("genres", [])

print("Available Genres:")
for i, genre in enumerate(genres, start=1):
    print(f"{i}. {genre['name']}")
    
try:
    genre_choice = int(input("Enter the number of your chosen genre: ")) - 1
    if genre_choice < 0 or genre_choice >= len(genres):
        print("Invalid choice. Exiting.")
except ValueError:
    print("Invalid input. Please enter a number.")
    
selected_genre = genres[genre_choice]
    
discover_url = f"{URL}/discover/movie"

discover_params = {
        "api_key": API,
        "language": "en-US",
        "with_genres": selected_genre['id'],
        "sort_by": "popularity.desc"
    }
discover_response = requests.get(discover_url, params=discover_params)

movies = discover_response.json().get("results", [])

random_movie = random.choice(movies)
print("\nRecommended Movie:")
print(f"Title: {random_movie['title']}")
print(f"Release Date: {random_movie['release_date']}")
print(f"Overview: {random_movie['overview']}")

    

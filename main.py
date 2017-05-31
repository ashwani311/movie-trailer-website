import requests
import json
from media import Movie
import fresh_tomatoes
api_key = "api_key=6a8cfaf39358e45af1c92e49770f5ba3&language=en-US"
url = "https://api.themoviedb.org/3/movie/popular?page=1&"
video_url = "https://api.themoviedb.org/3/movie/"
payload = "{}"
response = requests.request("GET", url + api_key, data=payload)
json_data = json.loads(response.text)

movies = []
it = 0  # iterator
for _ in xrange(6):
    while True:
        movie_data = json_data['results'][it]
        payload = "{}"
        if movie_data['poster_path'] \
            and movie_data['title'] \
                and movie_data['id']:
            url = video_url + str(movie_data['id']) + "/videos?" + api_key
            response = requests.request("GET", url, data=payload)
            video_data = json.loads(response.text)
            movie = Movie(movie_data['title'],
                          movie_data['poster_path'],
                          video_data['results'][-1]['key'])
            movies.append(movie)
            break
    it += 1
fresh_tomatoes.open_movies_page(movies)

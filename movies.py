import imdb
from fuzzywuzzy import fuzz

nameThreshold = 90

ia = imdb.IMDb()


def filter_by_title(title, otherTitle):
  return fuzz.token_sort_ratio(title, otherTitle) >= nameThreshold


def search_movies_by_year(title, year):
  searchedMovies = ia.search_movie(title)
  movies = []
  for movie in searchedMovies:
    if movie['year']==year and filter_by_title(title, movie['title']):
      movies.append(movie)
  return movies


def search_movies_by_keyword(keyword):
  movies = ia.get_keyword(keyword)
  return movies
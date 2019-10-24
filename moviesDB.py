from pony.orm import *

db = Database()


class Movie(db.Entity):
  title      = Required(str)
  year       = Required(int)
  genre      = Optional('Genre')
  imdbLink   = Optional(str)
  imdbCover  = Optional(str)
  timePeriod = Optional(str)


class Genre(db.Entity):
  name  = PrimaryKey(str)
  movies = Set('Movie')


def bind_db(provider, path):
    db.bind(provider, path, create_db=True)
    db.generate_mapping(create_tables=True)


def parse_and_populate_with_raw_data(rawData, withGenre=True):
  for rawMovie in rawData.splitlines():
    movie = rawMovie.split(' - ')
    if withGenre:
      add_movie(movie[2], movie[1], movie[0])
    else:
      add_movie(movie[1], movie[0])


@db_session
def add_movie(title, year, genre=None):
  if genre != None:
    if not Genre.exists(lambda genreDB: genreDB.name == genre):
      Genre(name=genre)
    Movie(title=title, year=year, genre=Genre[genre])
    else:
      Movie(title=title, year=year)
    commit()
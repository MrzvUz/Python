# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
title = input("Enter the movie title: ")
director = input("Enter the movie director: ")
year = input("Enter the movie release year: ")

movies.append({
    'title': title,
    'director': director,
    'year': year
})


# Create other functions for:
#   - listing movies
#   - finding movies


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        pass
    elif selection == "l":
        pass
    elif selection == "f":
        pass
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!



# The Solution No 1:

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movies():
  title = input("Enter the movie title: ")
  director = input("Enter the movie director: ")
  year = input("Enter the movie release year: ")

  movies.append({
    'title': title,
    'director': director,
    'year': year
  })


def show_movies():
  for movie in movies:
    print_movie(movie)


def print_movie(movie):
  print(f"Title: {movie['title']}")
  print(f"Director: {movie['director']}")
  print(f"Release Year: {movie['year']}")


def find_movies():
  search_title = input("Please, enter the movie title that you are looking for: ")

  for movie in movies:
    if movie["title"] == search_title:
      print_movie(movie)


user_option = {
  "a" : add_movies,
  "l" : show_movies,
  "f" : find_movies
}


def menu():
  selection = input(MENU_PROMPT)
  while selection != 'q':
    if selection in user_option:
      selected_function = user_option[selection]
      selected_function()
    else:
      print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


menu()

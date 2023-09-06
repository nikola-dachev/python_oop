from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def check_if_movie_liked(self, username, title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == title:
                        return True
                return False

    def register_user(self, username: str, age: int):
        if self.check_if_user_exists(username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if not self.check_if_user_exists(username):
            raise Exception("This user does not exist!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if self.check_if_movie_exists(movie.title):
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.append(movie)
                return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.check_if_movie_exists(movie.title):
            raise Exception("The movie {movie_title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if not self.check_if_movie_exists(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)

        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.remove(movie)
                return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if self.check_if_movie_liked(username, movie.title):
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1

        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.append(movie)
                return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        if not self.check_if_movie_liked(username, movie.title):
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1

        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.remove(movie)
                return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        return '\n'.join([movie.details() for movie in sorted_movies])

    def __str__(self):

        if self.users_collection:
            result = "All users: " + ', '.join([user.username for user in self.users_collection]) + "\n"
        else:
            result = "All users: No users.\n"

        if self.movies_collection:
            result += "All movies: " + ', '.join([movie.title for movie in self.movies_collection])
        else:
            result += "All movies: No movies."

        return result


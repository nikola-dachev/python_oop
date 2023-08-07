from project.user import User
from project.library import  Library


class Registration:

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)

        else:
            return f"User with id = {user.user_id} already registered in the library!"


    def remove_user(self, user: User, library: Library):

        if user in library.user_records:
            library.user_records.remove(user)

        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user = next(filter(lambda x: x.user_id == user_id, library.user_records))

        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username: # user. is instance we located from try / except above
            return f"Please check again the provided username - it should be different than the username used so far!"

        try: # we are changing username in the library_rented_books as well, overwritting the existing user recond, popping the info from the old username and creating new username
            library.rented_books[new_username] = library.rented_books.pop(user.username)

        except KeyError: # this will happen if this user is not currently at the dictionary rented_books does not have a book rented at the moment
            pass

        user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
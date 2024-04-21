import hashlib
from database import Database


class Users(Database):
    """
    Class for working with user-related operations, in particular registration and authentication.

    Attributes
    ----------
    username : str
        The name of the user.
    password : str
        The password of the user.
    place_of_departure : str
        The place of departure for the taxi order.
    destination : str
        The place of arrival for the taxi order.
    time : str
        Time of the taxi order creation in the format "DD/MM/YYYY XX:XX".

    Methods
    -------
    register_user(username, password)
        Registers new user with given username and password. Password is hashed. Returns tuple (bool, str).
    authenticate_user(username, password)
        Authenticates user by checking given username and password(comparison of hashes), makes request to Database.
        Returns tuple (bool, str).

    """
    def __init__(self, username=None, password=None, place_of_departure=None, destination=None, time=None) -> None:
        super().__init__(username, password, place_of_departure, destination, time)

    # регистрация пользователя
    def register_user(self, username, password):
        """
        Registers new user with given username and password, makes request to Database. Password is hashed.
        Returns tuple (bool, str).

        Parameters
        ----------
        username : str
            The name of the new user.
        password : str
            The password of the new user.

        Returns
        -------
        tuple
            The tuple containing a boolean indicating that the user was successfully registered and message about this.
        """
        # здесть должны быть строчки с хешированием пароля!!!!!
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # запрос в database.py о добавлении ногово пользователя
        super().register_user_database(username, hashed_password)
        return True, "Пользователь успешно зарегестрирован"


    # аунтефикация пользователя
    def authenticate_user(self, username, password):
        """
        Authenticates user by checking given username and password(comparison of hashes), makes request to Database.
        Returns tuple (bool, str).

        Parameters
        ----------
        username : str
            The name of the user to authenticate.
        password : str
            The password of the user to authenticate.

        Returns
        -------
        tuple
            The tuple containing a boolean indicating whether the user was successfully authenticated and message about
            this.
        """
        # проверка на наличие имени
        if super().check_users(username)[0]:
            return False, "Пользователь с таким именем не существует"
        
        # здесть должны быть строчки с хешированием пароля!!!!
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # запрос в database.py о возможности входа
        if not super().authentication_user_database(username, hashed_password):
            return False, "Неверный пароль"
        else:
            return True, "Успешная аутентификация"
        
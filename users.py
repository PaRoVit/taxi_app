import hashlib
from database import Database


class Users(Database):
    def __init__(self, username=None, password=None, place_of_departure=None, destination=None, time=None) -> None:
        super().__init__(username, password, place_of_departure, destination, time)

# регистрация пользователя
    def register_user(self, username, password):

        # здесть должны быть строчки с хешированием пароля!!!!!
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # запрос в database.py о добавлении ногово пользователя
        super().register_user_database(username, hashed_password)
        return True, "Пользователь успешно зарегестрирован"


    # аунтефикация пользователя
    def authenticate_user(self, username, password):
        # проверка на наличие имени
        if super().check_users(username)[0]:
            return False, "Пользователь с таким именем не существует"
        
        # здесть должны быть строчки с хешированием пароля!!!!
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # запрос в database.py о возможности входа
        if not super().authentication_user_database(username, hashed_password):
            return False, "Неверный пароль"
        else :
            return True, "Успешная аутентификация"
        
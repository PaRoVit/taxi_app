import hashlib
import database as db


# регистрация пользователя
def register_user(username, password):

    # здесть должны быть строчки с хешированием пароля!!!!!
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # запрос в database.py о добавлении ногово пользователя
    db.register_user_database(username, password)
    return True, "Пользователь успешно зарегестрирован"


# аунтефикация пользователя
def authenticate_user(username, password):
    # проверка на наличие имени
    if db.check_users(username)[0]:
        return False, "Пользователь с таким именем не существует"
    
    # здесть должны быть строчки с хешированием пароля!!!!
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # запрос в database.py о возможности входа
    if not db.authentication_user_database(username, password):
        return False, "Неверный пароль"
    else :
        return True, "Успешная аутентификация"
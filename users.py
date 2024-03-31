import bcrypt

# Пример базы данных пользователей (может быть заменена на использование реальной БД)
users_database = {}


def register_user(username, password):
    if username in users_database:
        return False, "Пользователь с таким именем уже существует"

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users_database[username] = hashed_password
    return True, "Пользователь успешно зарегистрирован"


def authenticate_user(username, password):
    if username not in users_database:
        return False, "Пользователь не найден"

    stored_password = users_database[username]
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        return True, "Успешная аутентификация"
    else:
        return False, "Неверный пароль"

# Другие функции для работы с пользователями (например, изменение пароля, удаление пользователя и т. д.)

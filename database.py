import json


class Database():
    def __init__(self, username = None, password = None, place_of_departure = None, destination = None, time = None) -> None:
        self.username = username
        self.password = password
        self.data_file = "database.js"
        self.place_of_departure = place_of_departure
        self.destination = destination
        self.time = time

    # выгрузка базы данных из файла
    def load_database(self):
        try:
            with open(self.data_file, "r") as f:
                # если файл существует, то возвращает его
                return json.load(f)
        except FileNotFoundError:
            # иначе возращает такую структуру
            return {"users": []}


    # загрузка базы данных в файл
    def save_database(self, database):
        with open(self.data_file, "w") as f:
            json.dump(database, f, indent=4)


    # проверка наличия имени в базе данных
    def check_users(self, username):
        database = self.load_database()
        for user in database["users"]:
            if user["username"] == username:
                # если такое имя уже есть в базе
                return False, "Пользователь с таким именем уже существует"
        # если этого имени в базе нет
        return True, "Пользователь может пройти регистрацию"


    # регистрация пользователя
    def register_user_database(self, username, password):
        database = self.load_database()
        # добавление в базу
        database["users"].append({"username": username, "password": password})
        self.save_database(database)
        return True, "Пользователь успешно зарегестрирован"


    # аутентификация пользователя
    def authentication_user_database(self, username, password):
        database = self.load_database()
        for user in database["users"]:
            # поиск по базе пользователя
            # решить проблему с хешированными паролями, потому что один и тот же пароль задан разным хешем(м.б. какое то условие надо или что то такое)
            if user["username"] == username and user["password"] == password:
                # если такой пользователь найден
                return True
        # иначе 
        return False


    # создание заказа
    def create_order_database(self, username, place_of_departure, destination, time):
        database = self.load_database()
        for user in database["users"]:
            # проверка имени
            if user["username"] == username:
                # проверка, были ли уже заказы
                if "trips" not in user:
                    # если не было, то добавляется ключ "trips" и заказ в формате строки
                    user["trips"] = [[place_of_departure, destination, time]]
                else:
                    # если заказы уже были, то в список добавляем новый заказ
                    user["trips"].append([place_of_departure, destination, time])
                self.save_database(database)
                return True, "Заказ успешно создан. Ожидайте"
        return False, "Ошибочка"


    # просмотр истории заказов
    def get_user_orders(self, username):
        database = self.load_database()
        for user in database["users"]:
            # если всё выполняется нормально
            try:
                # проверка имени
                if user["username"] == username:
                    # возвращаю историю заказов
                    return user["trips"]
            # если вылезла ошибка
            except KeyError:
                return "История заказов пуста"


import json


class Database():
    """
    Class for working with JSON database(database.js).

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
    check_users(username)
        Checks if the given username exists in the database and prints message. Returns tuple (bool, str).
    register_user_database(username, password)
        Registers new user and saves it in the database. Returns tuple (bool, str).
    authentication_user_database(username, password)
        Authenticates the user by checking their username and password. Returns boolean value.
    create_order_database(username, place_of_departure, destination, time)
        Creates new order for existing user and saves it in the database. Returns tuple (bool, str).
    get_user_orders(username)
        Gets list of all the taxi orders for user or throws an exception.
    """
    def __init__(self, username=None, password=None, place_of_departure=None, destination=None, time=None) -> None:
        """
        Initializes all the necessary attributes for the taxi order and database path(database.js).

        Parameters
        ----------
        username : str, optional
            The name of the user.
        password : str, optional
            The password of the user.
        place_of_departure : str, optional
            The place of departure for the taxi order.
        destination : str, optional
            The place of arrival for the taxi order.
        time : str, optional
            Time of the taxi order creation in the format "DD/MM/YYYY 00:00".
        """
        self.username = username
        self.password = password
        self.data_file = "database.js"
        self.place_of_departure = place_of_departure
        self.destination = destination
        self.time = time

    # выгрузка базы данных из файла
    def load_database(self):
        """
        Loads the database from the JSON(database.js) and returns it as a Python dictionary.

        Returns
        -------
        dict
            The dictionary with users data.

        Raises
        ------
        FileNotFoundError
            If the database file does not exist, then returns {"users": []}.
        """
        try:
            with open(self.data_file, "r") as f:
                # если файл существует, то возвращает его
                return json.load(f)
        except FileNotFoundError:
            # иначе возращает такую структуру
            return {"users": []}


    # загрузка базы данных в файл
    def save_database(self, database):
        """
        Converts the dictionary with users data into JSON(database.js).

        Parameters
        ----------
        database : dict
            The dictionary with users data.
        """
        with open(self.data_file, "w") as f:
            json.dump(database, f, indent=4)


    # проверка наличия имени в базе данных
    def check_users(self, username):
        """
        Checks if the given username exists in the database and prints message. Returns tuple (bool, str).

        Parameters
        ----------
        username : str
            The username to check.

        Returns
        -------
        tuple
            The tuple containing a boolean indicating whether the user was registered or no and message about this.
        """
        database = self.load_database()
        for user in database["users"]:
            if user["username"] == username:
                # если такое имя уже есть в базе
                return False, "Пользователь с таким именем уже существует"
        # если этого имени в базе нет
        return True, "Пользователь может пройти регистрацию"


    # регистрация пользователя
    def register_user_database(self, username, password):
        """
        Registers new user and saves it in the database. Returns tuple (bool, str).

        Parameters
        ----------
        username : str
            The username to register.
        password : str
            The new user password to register.

        Returns
        -------
        tuple
            The tuple containing a boolean indicating that the user was registered and message about this.
        """
        database = self.load_database()
        # добавление в базу
        database["users"].append({"username": username, "password": password})
        self.save_database(database)
        return True, "Пользователь успешно зарегестрирован"


    # аутентификация пользователя
    def authentication_user_database(self, username, password):
        """
        Authenticates the user by checking their username and password. Returns boolean value.

        Parameters
        ----------
        username : str
            The username to authenticate.
        password : str
            The user password to authenticate.

        Returns
        -------
        bool
            True if the user was authenticated, False otherwise.
        """
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
        """
        Creates new order for existing user and saves it in the database. Returns tuple (bool, str).

        Parameters
        ----------
        username : str
            The username who is creating taxi order.
        place_of_departure : str
            The place of departure for the taxi order.
        destination : str
            The place of arrival for the taxi order.
        time : str
            Time of the taxi order creation in the format "DD/MM/YYYY XX:XX".

        Returns
        -------
        tuple
            The tuple containing a boolean indicating whether the order was successfully created and message about this.
        """
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
        """
        Gets list of all the taxi orders for user or throws an exception.

        Parameters
        ----------
        username : str
            The name of the user for getting taxi orders.

        Returns
        -------
        list or str
            The list of all the taxi orders for user.

        Raises
        ------
        KeyError
            User does not exist, will display message that order history is empty.
        """
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

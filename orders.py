# Пример базы данных заказов (может быть заменена на использование реальной БД)
orders_database = []


class TaxiOrder:
    def __init__(self, destination, time):
        self.destination = destination
        self.time = time


def create_taxi_order(destination, time):
    order = TaxiOrder(destination, time)
    orders_database.append(order)
    return "Заказ такси успешно создан"


def get_user_orders():
    # Предположим, что текущий пользователь уже аутентифицирован
    # и его имя пользователя сохранено в переменной current_user
    user_orders = [order for order in orders_database if hasattr(order, 'destination')]
    return user_orders

# Другие функции для работы с заказами (например, отмена заказа, получение списка всех заказов и т. д.)

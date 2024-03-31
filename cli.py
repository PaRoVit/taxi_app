import argparse
import getpass
import users
import orders


def register_user():
    username = input("Введите имя пользователя: ")
    password = getpass.getpass("Введите пароль: ")
    confirm_password = getpass.getpass("Повторите пароль: ")

    if password != confirm_password:
        print("Пароли не совпадают")
        return

    success, message = users.register_user(username, password)
    print(message)


def login():
    username = input("Введите имя пользователя: ")
    password = getpass.getpass("Введите пароль: ")

    success, message = users.authenticate_user(username, password)
    if success:
        print(message)
        return username
    else:
        print(message)
        return None


def create_order(username):
    destination = input("Введите место назначения: ")
    time = input("Введите время (в формате HH:MM): ")

    message = orders.create_taxi_order(destination, time)
    print(message)


def view_orders(username):
    user_orders = orders.get_user_orders()
    if user_orders:
        print("Ваши заказы:")
        for order in user_orders:
            print(f"- Место назначения: {order.destination}, Время: {order.time}")
    else:
        print("У вас пока нет заказов")


def main():
    parser = argparse.ArgumentParser(description='CLI-приложение для заказа такси')
    parser.add_argument('-r', '--register', action='store_true', help='Регистрация нового пользователя')
    parser.add_argument('-l', '--login', action='store_true', help='Вход в систему')
    parser.add_argument('-o', '--order', action='store_true', help='Создание заказа такси')
    parser.add_argument('-v', '--view', action='store_true', help='Просмотр истории заказов')

    args = parser.parse_args()

    if args.register:
        register_user()
    elif args.login:
        username = login()
        if username:
            if args.order:
                create_order(username)
            elif args.view:
                view_orders(username)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

import argparse
import sys
import getpass
import users
import database as db
import datetime


# регистрация пользователя
def register_user():
    username = input("Введите имя пользователя: ")
    # проверка наличия пользователя в базе данных
    success, message = db.check_users(username)
    # если имя есть, то сообщение об этом
    if not success:
        print(message)
        return False
    # иначе продолжение регистрации пользователя с введением пароля
    elif success:
        password = getpass.getpass("Введите пароль: ")
        confirm_password = getpass.getpass("Повторите пароль: ")

        # проверка что пароли совпадают
        if password != confirm_password:
            print("Пароли не совпадают")
            return False

        # запрос в users.py о добалении нового пользователя
        success, message = users.register_user(username, password)
        print(message)
        return True


# вход в систему
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
    

# создание заказа
def create_order(username):
    place_of_departure = input("Введите место отправления: ")
    destination = input("Введите место назначения: ")
    # запись времени из онлайн
    time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    # запрос на создание нового заказа
    success, message = db.create_order_database(username, place_of_departure, destination, time)
    if success:
        print(message)
    else:
        print(message)


# просмотр истоиии заказов
def view_orders(username):
    # вытягиваю история заказов из базы
    orders = db.get_user_orders(username)
    # узнаю тип переменной, чтобы понять список там или строка
    if type(orders) is str:
        print(orders)
        return
    else:
        print("Ваша история заказов:")
        for value in orders:
            # печать истории заказов в формате: местро отпр. -> место приб., время
            print(f"{value[0]} -> {value[1]}, {value[2]}")


def main():
    # здесь находятся ключи для дальнейшего запуска проги
    parser = argparse.ArgumentParser(description='CLI-приложение для заказа такси', add_help=False)
    parser.add_argument('-r', '--register', action='store_true', help='Регистрация нового пользователя')
    parser.add_argument('-l', '--login', action='store_true', help='Вход в систему')
    parser.add_argument('-e', '--exit', action='store_true', help='Выход из системы')
   

    args, unknown = parser.parse_known_args()

    # если введён ключ -h, то покажет все возможные ключи что есть
    if '-h' in unknown or '--help' in unknown:
        parser.print_help()
        return
    
    # если запуск без ключа, то выведется строка о помощи
    if not any(vars(args).values()):
        print("Не указаны аргументы командной строки. Используйте -h или --help для справки.")
        sys.exit()

    # если ключ -r
    if args.register:
        while True:
            if register_user():
                break
            else:
                answer = input("Желаете продолжить регистрацию?\nДа/Нет\n")
                if answer == "нет" or answer == "Нет":
                    break
    # если ключ -l
    elif args.login:
        while True:
            username = login()
            if username:
                while True:
                    print("Выберите дальнейшее действие:")
                    print("1. Вызвать такси     2. Посмотреть историю поездок       3. Выход из системы")
                    action = int(input())
                    if action == 1:
                        create_order(username)
                    elif action == 2:
                        view_orders(username)
                    elif action == 3:
                        break
            else:
                print("Желаете продолжить вход в систему?\nДа/Нет\n")
                if answer == "нет" or answer == "Нет":
                    break
            if action == 3:
                break
    # если ключ -e
    elif args.exit:
        sys.exit()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

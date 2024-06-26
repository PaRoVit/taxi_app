<a id="anchor"></a>
# CLI-приложение для службы такси 
***

[Ссылка на доску Miro с архитектурой проекта.](https://miro.com/app/board/uXjVKMZ3lDQ=/)
[Ссылка на Notion с задачами команды.](https://www.notion.so/bcfcc5f123a94bbfa7761a0eed4fd46d?v=4b08f9fe033d4a30bb780cf4af78f9c6=/)
![Screenshot2](screen2.png)
***
>
## Описание проекта.
Данное приложение служит для заказа такси.
При помощи него можно зарегестрироваться или войти в локальную базу данных, создать заказ или посмотреть их историю.
Работа с приложением реализовывается через командную строку.
***

## Инструкции по работе с приложением.
Основная работа с приложеним происходит через [cli.py](cli.py)

Запустить приложение можно через команду ```python cli.py -[ключ]```
- Ключ __-h (--help)__ показывает все возможные ключи
![Screenshot2](/img/demo.gif)
- Ключ __-r (--register)__ позволяет зарегестрировать нового
пользователя, после чего завершает выполнение приложения
![Screenshot3](/img/R_demo.gif)
- Ключ __-l (--login)__ позволяет пользователю войти в систему
![Screenshot3](/img/L_demo.gif)
- Ключ __-e (--exit)__ завершает работу приложения

При регистрации Вас попросит ввести ваше имя и пароль. Ввод пароля скрыт от глаз пользователя.
Когда пользователь смог войти в систему, перед ним появится меню с дальнейшим выбором действия:
- Создание заказа такси (ввод точки отправления и точки прибытия)
- Просмотр вашей истории заказов (появится список поездок, где в каждой указано место отправления, прибытия
и время, в которое было заказано такси)
- Завершение работы приложения
![Screenshot3](/img/LProcess_demo.gif)
***

[Вверх](#anchor)

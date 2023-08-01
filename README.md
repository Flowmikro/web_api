# web_api
Веб-приложение на Django, которое отображает список пользователей и их посты, а также позволять добавлять и удалять посты.

Создано:\
Несколько API-конечных пунктов. Первый возвращает список всех пользователей, второй - список всех постов конкретного пользователя,
третий - добавление нового поста, четвертый - удаление существующего поста.\
Аутентификация и авторизация.\
Пользовательский интерфейс
# Стек
Python, Django, Django REST, HTML/CSS, Docker
# Установка
git clone https://github.com/Flowmikro/web_api.git \
cd web_api\
docker-compose build\
docker-compose up \
команды docker-compose run --rm web-app sh -c "python manage.py <ваша команда>"



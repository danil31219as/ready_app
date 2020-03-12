from data.users import User
from data import db_session

user = User()
user.name = "Пользователь 1"
user.about = "биография пользователя 1"
user.email = "email@email.ru"
user.hashed_password = '12345'
db_session.global_init("db/blogs.sqlite")
session = db_session.create_session()
session.add(user)
session.commit()
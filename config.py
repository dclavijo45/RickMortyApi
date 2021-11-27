from os import getenv as env
import random
import string

#App
SECRET_KEY = ''.join(random.
    choice(f"{string.ascii_uppercase}{string.punctuation}{string.ascii_letters}") 
    for i in range(20))

DEBUG = int(env('DEBUG', '1'))

#Server
PORT = int(env('PORT', 8100))
HOST = env('HOST', '0.0.0.0')

#MySQL
MYSQL_HOST = env('mysql_host', 'localhost')
MYSQL_USER = env('mysql_user', 'pwd')
MYSQL_PASSWORD = env('mysql_password', 'pwd')
MYSQL_DB = env('mysql_db', 'db_rick_morty')
from API.dbHandler import db
from Singleton import Singleton
from encodePassword import encodePassword

def login():
    data = Singleton()
    print(data.DB)
    sql = db(
        data.HOST,
        data.USER,
        data.PASS,
        data.DB
    )

    user = False

    while not(user):
        Username = str(input("Masukkan username : "))
        Password = str(input("Masukkan password : "))
        user = sql.login(Username, encodePassword(Password))
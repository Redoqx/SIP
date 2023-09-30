from API.dbHandler import db
from encodePassword import encodePassword

def login(data):
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
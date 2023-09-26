import os
from dotenv import load_dotenv

from dbHandler import db
from encodePassword import encodePassword

load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USR')
PASS = os.getenv('PASS')
DB = os.getenv('DB')

sql = db(HOST,USER,PASS,DB)

user = False

while not(user):
    Username = str(input("Masukkan username : "))
    Password = str(input("Masukkan password : "))
    user = sql.login(Username, encodePassword(Password))
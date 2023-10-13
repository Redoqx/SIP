import os
from dotenv import load_dotenv

# from API.dbHandler import db
from Singleton.Singleton import Singleton
from API.loginHandler import login
# from createUser import createUser
# from createUser import createAdmin


data = Singleton()
data.set_value()


# createUser(data=data)
# createAdmin(data=data)
login()

# user = False

# while not(user):
#     Username = str(input("Masukkan username : "))
#     Password = str(input("Masukkan password : "))
#     user = sql.login(Username, encodePassword(Password))
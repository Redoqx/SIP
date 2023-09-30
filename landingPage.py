import os
from dotenv import load_dotenv

# from API.dbHandler import db
from loginHandler import login
# from createUser import createUser
# from createUser import createAdmin

load_dotenv()

# HOST = os.getenv('HOST')
# USER = os.getenv('USR')
# PASS = os.getenv('PASS')
# DB = os.getenv('DB')

class Singleton:
    _instance = None  # Class variable to store the single instance

    def __new__(cls):
        # Check if an instance already exists
        if cls._instance is None:
            # If not, create a new instance
            cls._instance = super(Singleton, cls).__new__(cls)
            cls.USER = os.getenv('USR')
            cls.PASS = os.getenv('PASS')
            cls.HOST = os.getenv('HOST')
            cls.DB = os.getenv('DB')
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
data = Singleton()

# createUser(data=data)
# createAdmin(data=data)
login(data=data)
# sql = db(HOST,USER,PASS,DB)

# user = False

# while not(user):
#     Username = str(input("Masukkan username : "))
#     Password = str(input("Masukkan password : "))
#     user = sql.login(Username, encodePassword(Password))
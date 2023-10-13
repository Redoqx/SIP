import os
import sys

from directoryInfo import getDirectory
from dotenv import load_dotenv

load_dotenv()

class Singleton:
    _instance = None  # Class variable to store the single instance

    def __new__(cls):
        # Check if an instance already exists
        if cls._instance is None:
            # If not, create a new instance
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.USER = ""
            cls._instance.PASS = ""
            cls._instance.HOST = ""
            cls._instance.DB = ""
            cls._instance.username = ""
            cls._instance.nama = ""
            cls._instance.admin = ""
            # cls._instance.PATH = ""
        return cls._instance

    def set_value(self):
        self.USER = os.getenv('USR')
        self.PASS = os.getenv('PASS')
        self.HOST = os.getenv('HOST')
        self.DB = os.getenv('DB')
        # self.PATH = getDirectory()
    
    def set_username(self, data):
        self.username = data[0]
        self.nama = data[1]
        self.admin = data[2]

    def get_value(self):
        return self.USER
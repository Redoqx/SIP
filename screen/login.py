# import os
# from dotenv import load_dotenv
# load_dotenv()

# import sys
# sys.path.insert(1,os.getenv("PATH_CODE"))

from API.loginHandler import loginHandler
from encodePassword import encodePassword
from Singleton.Singleton import Singleton

def login():
    data = Singleton()
    data.set_value()  
      
    logintry = 0
    while(logintry<3 and not(data.username)):
        username = str(input("Masukkan username: "))
        password = str(input("Masukkan password: "))
        catch = loginHandler(
            username=username, 
            password=encodePassword(password),
            logintry=logintry
            )
        if catch:
            data.set_username(catch)
        else:
            logintry+=1

    print(data.nama)
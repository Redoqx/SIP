import os
from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.insert(1,os.getenv("PATH_CODE"))

from Singleton.Singleton import Singleton
from screen.login import login

data = Singleton()
data.set_value()

login()

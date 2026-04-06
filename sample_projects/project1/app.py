import utils
from db import Database

class App:
    def __init__(self):
        self.db = Database()
    
    def run(self):
        utils.helper()
        self.db.connect()
        print("App running...")


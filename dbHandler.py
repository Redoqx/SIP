import mysql.connector

class db():
    def __init__(self, HOST, USER, PASS, DB):
        # Create a connection to the MySQL database
        self._conn = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASS,
            database = DB
        )
        # self.cursor = self._conn.cursor()
        self.logintry = 0
    
    def commit(self):
        self._conn.commit()

    def closeAll(self):
        self.cursor.close()
        self._conn.close()

    def execute(self, command:str, params:None, multi: bool=False):
        self.cursor.execute(command,params=params,multi=multi)
    
    def checkTable(self):
        # for checking connection to database
        self.cursor.execute("SHOW TABLES")
        tables = self.cursor.fetchall()
        for table in tables:
            print(table[0])

    def login(self, username, password:str):
        try:
            self.cursor = self._conn.cursor()
            if self.logintry<3:
                self.cursor.execute(f"SELECT id_peminjam FROM peminjam WHERE id_peminjam = \'{username}\' AND password = \'{password}\'")
                result = self.cursor.fetchone()
                self.cursor.close()
                if result:
                    print(f"Berhasil masuk!\nSelamat datang {username}")
                    return username
                else:
                    self.logintry+=1
                    print(f"Username atau password salah!\nPercobaan ke:{self.logintry}")
                    return False

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
import mysql.connector
from Singleton.Singleton import Singleton


def loginHandler(username, password, logintry):
    data = Singleton()
    conn = mysql.connector.connect(
        host = data.HOST,
        user = data.USER,
        password = data.PASS,
        database = data.DB
    )
    try:
        cursor = conn.cursor()

        if logintry < 3:
            query = """ 
                    SELECT id_pegawai,nama,Admin 
                    FROM pegawai 
                    WHERE id_pegawai = %s AND password = %s
                    """
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            print(result)
            if result:
                print(f"Berhasil masuk!\nSelamat datang {username}")
                return result
            else:
                logintry += 1
                print("Username atau password salah!")
                return False

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
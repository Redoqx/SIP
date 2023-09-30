from API.dbHandler import db
from encodePassword import encodePassword

def createUser(data):
    sql = db(
        data.HOST,
        data.USER,
        data.PASS,
        data.DB
    )

    id = str(input("Masukkan id : "))
    nama_lengkap = str(input("Masukkan nama lengkap : "))
    password = str(input("Masukkan password : "))
    if password == input("Masukkan password kembali : "):
        command = "INSERT INTO peminjam (id_peminjam, nama, password) VALUES (%s, %s, %s)"
        sql.execute(command=command, params=(id, nama_lengkap, encodePassword(password=password)))

def createAdmin(data):
    sql = db(
        data.HOST,
        data.USER,
        data.PASS,
        data.DB
    )

    id = str(input("Masukkan id : "))
    nama_lengkap = str(input("Masukkan nama lengkap : "))
    password = str(input("Masukkan password : "))
    if password == input("Masukkan password kembali : "):
        command = "INSERT INTO peminjam (id_peminjam, nama, password, Admin) VALUES (%s, %s, %s, \"1\")"
        sql.execute(command=command, params=(id, nama_lengkap, encodePassword(password=password)))

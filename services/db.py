import mysql.connector


db = mysql.connector.connect(
    host  = 'localhost',
    user = 'root',
    password='',
    database='mini_market'
    
)

print(db.is_connected())

def insert_item(kode_barang, nama_barang,harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang,harga_barang, stok_barang) VALUES (%s,%s,%s,%s)", (kode_barang, nama_barang,harga_barang, stok_barang))
    db.commit()
    if cursor.rowcount > 0:
        print("Data Berhasil dimasukan")
    else:
        print("Data Gagal di Insert")
        
        

def fecth_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    return cursor.fetchall()
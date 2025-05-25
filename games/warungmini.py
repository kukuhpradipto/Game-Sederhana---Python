from time import sleep
from games.goa_main_game import exit_program
from services import db

def add ():
    kode_barang = input("Kode Barang : ")
    nama_barang = input("Nama Barang : ")
    harga_barang = int(input("Harga Barang : "))
    stok_barang = int(input("Stok Barang :"))
    
    print("\n")
    
    db.insert_item(kode_barang, nama_barang,harga_barang,stok_barang)

def check():
    items = db.fecth_item()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        
        print(f'''Kode : {kode_barang}, Nama : {nama_barang}, Harga : {harga_barang}, Stok : {stok_barang}''')
        # print(item)

def warung_mini_main ():
    print("\nSelamat Datang di Warung Apps")

    while True:
        menu_warung_apps = int(input('Menu\n1. Tambah Barang\n2. Check Barang\n3. Kembali\n'))
        
        if menu_warung_apps == 1:
            add()
        elif menu_warung_apps == 2:
            check()
        elif menu_warung_apps ==3:
            warung_mini_main()
        else:
            exit()
      

        
        # harga = int(input('Total harga: '))
        
        # if harga == 0:
        #     exit_program()
            
            
            
if __name__ == '__main__':
    warung_mini_main()
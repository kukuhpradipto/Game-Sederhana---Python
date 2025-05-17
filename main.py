import random

welcome_message = "Selamat datang di games"

print("*-----------------*")
print(f"** {welcome_message} **")
print("*-----------------*")

   
nama_pengguna = input("Masukan nama anda:")
while nama_pengguna == '' :
    nama_pengguna = input("Nama Anda belum dimasukan, silahkan untuk di isi dulu..")

posisi_kelinci = random.randint(1,4)
bentuk_goa = "|_|"

goa_kosong = [bentuk_goa]* 4
goa = goa_kosong.copy()
goa[posisi_kelinci -1] = "|0_0|"

goa_tampa_array = " ".join(goa)
goa_kosong_tampa_array = " ".join(goa_kosong)

print(f'''
      Halo {nama_pengguna}! Coba perhatkan goa dibawah ini
            {goa_kosong_tampa_array}
          ''') 
pilihan_user = input("menurut kamu dimanakah orangnya? [1/2/3/4] ")
while pilihan_user.isdigit() != True : 
    pilihan_user = input("Data tidak valid, ....")

while int(pilihan_user) not in (1,2,3,4):
            pilihan_user = input("Masukan sesuai dengan pilihan yang ada...")
print(f"Pilihan kamu adalah {pilihan_user}")

konfirmasi_user = input(f"Apakah kamu yakin dengan jawab kamu {pilihan_user}? [Y/N]") 
if konfirmasi_user in ["Y","y"] : 
    if int(pilihan_user) == posisi_kelinci : 
                    print(f"Yaup betul sekali, cuy ada di {posisi_kelinci}")
                    print(goa_tampa_array)
    else: 
                    print(f"Sorry masih belum sesuai, cuy ada di {posisi_kelinci} ")
                    print(goa_tampa_array)
elif konfirmasi_user in ["N","n"] : 
                print("Baiklah kamu tidak yakin. Program di hentikan")
                exit()
else: 
                print("Inputan tidak sesuai")
                exit()


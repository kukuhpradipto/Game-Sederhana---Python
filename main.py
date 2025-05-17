import random

welcome_message = "Selamat datang di games"

print("*-----------------*")
print(f"** {welcome_message} **")
print("*-----------------*")

   
nama_pengguna = input("Masukan nama anda:")
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
if pilihan_user.isdigit() == True : 
    print(f"Pilihan kamu adalah {pilihan_user}")

    if int(pilihan_user) in [1,2,3,4] :
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
    else :
            print("Masukan sesuai dengan pilihan yang ada")
            exit()
else : 
    print("Masukan sesuai dengan pilihan yang ada, Angka dan bukan Huruf")
    exit()


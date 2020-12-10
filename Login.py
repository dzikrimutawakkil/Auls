"""Program login dengan 3x percobaan"""

print("======PROGRAM LOGIN GAME======")
print("SELAMAT DATANG")
username = input("Masukkan Username :")
password = input("Masukkan Password :")
if username == "admin":
    if password == "admin":
        print('='*10)
        print("ANDA BERHASIL LOGIN")
    else:
        print('='*10)
        i = 1
        while i <= 3:
            print("PASSWORD SALAH")
            print("SILAHKAN LOGIN KEMBALI")
            password = input("Masukkan Password :") 
            print('='*10)
            if password == "admin":
                print("ANDA BERHASIL LOGIN")
                break
            i += 1
        else:
            print("ANDA TELAH MENCOBA 3X") 

        
else:
    print('='*10)
    j = 1
    while j <= 3:
        print("USER TIDAK TERDAFTAR")
        username = input("Masukkan Username :")
        print('='*10)
        if username == "admin":
            password = input("Masukkan Password :")
            if password == "admin":
                print('='*10)
                print("ANDA BERHASIL LOGIN")
            else:
                print('='*10)
                k = 1
                while k <= 3:
                    print("PASSWORD SALAH")
                    print("SILAHKAN LOGIN KEMBALI")
                    password = input("Masukkan Password :") 
                    print('='*10)
                    if password == "admin":
                        print("ANDA BERHASIL LOGIN")
                        break
                    k += 1
                else:
                    print("ANDA TELAH MENCOBA 3X") 
            break
        j += 1
    else:
        print("ANDA TELAH MENCOBA 3X")
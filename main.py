import attendance_face_recognition as attd

selectOption = 0
print("Pilihan Opsi: ")
print("1. Registrasi Wajah Baru")
print("2. Login Member Face Recognition")
print(" ")
selectOption = int(input("Pilih Opsi : "))

if selectOption == 1:
    input_name = input("Masukkan Nama Yang Didaftarkan : ")
    attd.register(input_name)
elif selectOption == 2:
    attd.login()

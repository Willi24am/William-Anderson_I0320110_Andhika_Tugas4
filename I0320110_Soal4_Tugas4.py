usia = int(input("Berapa usia kamu :"))
lulus = input("Apakah anda sudah lulus ujian kualifikasi (Y/T)?:")

if (usia>=21) and (lulus == "Y") :
    print ("Anda dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar kursus")
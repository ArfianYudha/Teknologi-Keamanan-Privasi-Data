def enkripsi_text(plaintext,shift):
    result = ""

    for i in range(len(plaintext)):
        huruf = plaintext[i]
        
        if huruf==" ":
            result+=" "
        # Memeriksa jika character huruf besar lalu melakukan enkripsi
        elif (huruf.isupper()):
            result += chr((ord(huruf) + shift-65) % 26 + 65)

        # Memeriksa jika character huruf kecil lalu melakukan enkripsi
        else:
            result += chr((ord(huruf) + shift-97) % 26 + 97)
    
    return result

plaintext = input("Masukkan Teks :")
# Shift 1 karena NIM 201
shift = 1
print("Plain Text : " + plaintext)
print("Shift : " + str(shift))
print("Enkripsi Teks : " + enkripsi_text(plaintext,shift))

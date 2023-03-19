def generateKey(teks, key): 
  key = list(key) 
  if len(teks) == len(key): 
    return(key) 
  else: 
    for i in range(len(teks) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def enkripsi(teks, key): 
  enkripsi_teks = [] 
  for i in range(len(teks)): 
    x = (ord(teks[i]) +ord(key[i])) % 26
    x += ord('A') 
    enkripsi_teks.append(chr(x)) 
  return("" . join(enkripsi_teks)) 
def deskripsi(enkripsi_teks, key): 
  orig_text = [] 
  for i in range(len(enkripsi_teks)): 
    x = (ord(enkripsi_teks[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 
if __name__ == "__main__": 
  teks = input("Masukkan Teks: ")
  keyword = "201"
  print("Key: ", keyword)
  key = generateKey(teks, keyword) 
  enkripsi_teks = enkripsi(teks,key) 
  print("Encrypted message:", enkripsi_teks) 
  print("Decrypted message:", deskripsi(enkripsi_teks, key)) 

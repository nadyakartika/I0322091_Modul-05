#buatlah list hari dalam seminggu
#buat perulangan yang menyatakan pergi belanja kecuali di hari minggu
#daftar belanja = [gula, garam, beras, kecap, saus]
#print masing masing daftar dalam setiap baris

hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu"]
daftar_belanja = ["gula", "garam", "beras", "kecap", "saus"]

i = 0 
for j in hari:
    if j == "minggu" :
        print("Tidak belanja")
        continue
    print(j , "=", daftar_belanja[i])
    i = i+1 
    if i == 5:
        i = 0



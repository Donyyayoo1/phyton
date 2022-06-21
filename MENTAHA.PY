garispendek=("----------------------------------------")
garispanjang=("------------------------------------------------------------------------")

kameraC=("===========CANON==========")
kameraS=("===========SONY===========")
kameraN=("===========NIKON==========")
kameraF=("=========FUJIFILM=========")
print(kameraC)
print(kameraS)
print(kameraN)
print(kameraF)

print(" ")
print(" ")
print(" ")



#list harga
menu=input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")
menu = "y" or "Y"
while menu == "y" or "Y":
   
    print(garispendek)
    print("kode       jenis kamera       harga/jam")
    print(garispendek)
    print("01             CANON           5000.000 ")
    print("02             SONY            6000.000")
    print("03             NIKON           6000.000")
    print("04             FUJIFILM        6000.000")
    print(garispendek)
    data = str(input("Mau sewa kamera apa? ketik kode kamera : "))
    berapajam = int(input("berapa jam? : "))




#deklarasi variabel list
listKK = []
listBK = []

#input
for x in range(data):
    print ("\data ke - ", x-1)
    kdk = input("kode kamera [C|S|N|F] : ")
    listKK.append(kdk)
    #bkk = int(input("berapa jam :"))
    #listBK.append(bkk)
    print(garispendek)
    jeniskamera = "CANON"
    harga = (5000)
    totalharga = (harga*berapajam)
    print(totalharga)

    print(" ------------------------------")
    print("=====Menu :",jeniskamera)
    print("=====perjam :", berapajam)
    print("=====Harga :", harga)
    print(" ------------------------------")
    print("=====Total Pembayaran :", totalharga)
    print(" ------------------------------")
    menu=input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")
    if menu == "y" or "Y":
        print(garispendek)
        print("kode       jenis kamera       harga/jam")
        print(garispendek)
        print("01             CANON           5000.000")
        print("02             SONY            6000.000")
        print("03             NIKON           6000.000")
        print("04             FUJIFILM        6000.000")
        print(garispendek)
        data = str(input("Mau sewa kamera apa? ketik kode kamera : "))
        berapajam = int(input("ingin sewa berapa jam? : "))
        if data == '01':
            jeniskamera = "CANON"
            harga = 5000
            totalharga = harga*berapajam
            print(" ------------------------------")
            print("=====nama pembeli : ", namapembeli)
            print("=====Kamera    :",jeniskamera)
            print("=====Lama Sewa :", berapajam)
            print("=====Harga     :", harga)
            print(" ------------------------------")
            print("=====Total Pembayaran :", totalharga)
            print(" ------------------------------")
        elif data == '02':
            jeniskamera = "SONY"
            harga = 6000
            totalharga = harga*berapajam
            print(" ------------------------------")
            print("=====nama pembeli : ", namapembeli)
            print("=====Kamera    :",jeniskamera)
            print("=====Lama Sewa :", berapajam)
            print("=====Harga     :", harga)
            print(" ------------------------------")
            print("=====Total Pembayaran :", totalharga)
            print(" ------------------------------")
        elif data == '03':
            jeniskamera = "NIKON"
            harga = 6000
            totalharga = harga*berapajam
            print(" ------------------------------")
            print("=====nama pembeli : ", namapembeli)
            print("=====Kamera    :",jeniskamera)
            print("=====Lama Sewa :", berapajam)
            print("=====Harga     :", harga)
            print(" ------------------------------")
            print("=====Total Pembayaran :", totalharga)
            print(" ------------------------------")
        elif data == '04':
            jeniskamera = "FUJIFILM"
            harga = 6000
            totalharga = harga*berapajam
            print(" ------------------------------")
            print("=====nama pembeli : ", namapembeli)
            print("=====Kamera    :",jeniskamera)
            print("=====Lama Sewa :", berapajam)
            print("=====Harga     :", harga)
            print(" ------------------------------")
            print("=====Total Pembayaran :", totalharga)
            print(" ------------------------------")
        else:
            print("Kode yang Anda input salah")
    else:
        print(" ------------------------------")
        print("=====nama pembeli : ", namapembeli)
        print("=====Kamera    :",jeniskamera)
        print("=====Lama Sewa :", berapajam)
        print("=====Harga     :", harga)
        print(" ------------------------------")
        print("=====Total Pembayaran :", totalharga)
        print(" ------------------------------") 
    if menu == "n" or "N": 
        print(" ------------------------------")
        print("=====nama pembeli : ", namapembeli)
        print("=====Kamera    :",jeniskamera)
        print("=====Lama Sewa :", berapajam)
        print("=====Harga     :", harga)
        print(" ------------------------------")
        print("=====Total Pembayaran :", totalharga)
        print(" ------------------------------")












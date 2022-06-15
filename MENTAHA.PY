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









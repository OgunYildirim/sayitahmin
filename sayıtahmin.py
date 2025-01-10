print("Sayı tahmin oyunu oynayacağız ( 1 ile 40 arasında)")



import random

tahmin_hakkınız = 7 

bilgi_seçimi =random.randint(1,40)

while True :
    sayı=int(input("1 ile 40 arasında bir sayı seçiniz :"))

    if sayı > bilgi_seçimi :
        print("Sayınızı küçültünüz .")
        tahmin_hakkınız = tahmin_hakkınız - 1

    elif sayı <  bilgi_seçimi :
        print("Sayınızı büyültünüz :")
        tahmin_hakkınız  = tahmin_hakkınız - 1
    elif sayı == bilgi_seçimi :

        print("Tebrikler sayıya ulaştınız ! Sayınız ",bilgi_seçimi)
        break


    if tahmin_hakkınız == 0 :
        print("Tahmin hakkınız doldu çıkış yapılıyor ...")
        print("bilgisayarın şeçimi :",bilgi_seçimi)
        break








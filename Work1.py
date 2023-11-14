import random

b1 = 1
b2 = 10

c = ["Leyla", "Ali", "Murat"]

while True:

    a = int(input("Rakam Oyunu İçin 2 isim tahmin etmece için 1 isimleri veya rakam limiti değiştirmek için 0 yazınız. Çıkmak için ise -1 yazın"))


    if a == 2:
        while True:
            
            b = random.randint(b1,b2)

            print("rakamın başlangıcı:", b1, "rakamın limiti", b2)

            userN = int(input("rakam bulunuz. Çıkmak Için -1 yazabilirsiniz"))

            if userN == b:
                print("Doğru!")
            
            elif userN == -1:
                break
            else:
                print("yanlış. Numara:", b)
    elif a == 1:
        while True:
            l = random.choice(c)
            print("listede şu isimler var:")

            print(c)

            userNa = input("Ne İsim Düşünüyorsun? Çıkmak İçin -1 yazabilirsiniz")

            if userNa == l:
                print("İsmi Buldunuz!")
            elif userNa == "-1":
                break
            else:
                print("maalesef bulamadınız. Ad:", l)
    elif a == 0:
        userchoice = int(input("rakam için 1, ad için 2"))

        if userchoice == 1:
            userB1 = int(input("Başlangıç rakamı yazın (0 yanlızca)"))
            b1 = userB1
            userB2 = int(input("Limitli rakamı yazın"))
            b2 = userB2
            print("rakamlar sorunsuzca değiştirilmiştir!")
        elif userchoice == 2:
            userAd = input("Ne ad yazmak istiyorsunuz?")
            c.append(userAd)
            print("Ad Sorunsuzca Eklendi!")

    elif a == -1:
        print("bu pencereyi kapatmak şimdi güvenli.")
        break               



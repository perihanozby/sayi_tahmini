from random import randint
rand=randint(1, 100)
say=0

while True:
    say +=1
    sayi=int(input("1 ile 100 arasinda deger girin(0 cikis):"))
    if(sayi==0):
        print("Oyunu iptal ettiniz")
        break
    elif sayi < rand:
        print("Daha yuksek bir sayi girin.")
        continue
    elif sayi> rand:
        print("Daha dusuk bir sayi girin.")
        continue
    else:
        print("Rastgele secilen sayi{0}!".format(rand))
        print("Tahmin sayiniz{0}".format(say))


sayı=input("lütfen bir sayı giriniz")
while True:
    if(sayı=="q"):
        print("programı sonlandır")
        sayı = int(sayı)
        break

    else:
        sayı = int(sayı)
        faktöriyel=1
        for i in range(2,sayı+1):
            faktöriyel*=i
        print("faktöriyel",faktöriyel)
        break
#Bir önceki sorudaki örneğe dayanarak if-elif-else yapılarını kullanarak aşağıdaki soruları
#cevaplayınız (20p).
#a) Eğer uzaylı rengi yeşil ise "Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız",
#b) Eğer uzaylı rengi sarı ise "Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız",
#c) Eğer uzaylı rengi kırmız ise "Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız"
#şeklinde çıktı veren programı yazınız

uzaylinin_rengi = input("Uzaylının rengi (kırmızı|yeşil|sarı): ")

if uzaylinin_rengi == "yeşil":
    print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız :)")
elif uzaylinin_rengi == "sarı":
    print("Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız :)")
elif uzaylinin_rengi == "kırmızı":
    print("Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız :)")
else:
    print("Geçersiz bir renk girdiniz, lütfen geçerli bir renk giriniz!!!")

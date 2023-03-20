#İçinde uzaylı olan bir oyun geliştirdiğinizi düşünün. uzaylı_rengi isminde bir değişken oluşturun
#ve bu değişken string türünde değerler alsın. Bu değişkene kırmızı, yeşil ya da sarı
#değerlerinden birini klavyeden veriniz. Eğer uzaylının rengi yeşilse “Tebrikler, yeşil uzaylıya ateş
#ettiğiniz için 5 puan kazandınız” şeklinde bir çıktı veriniz. Eğer rengi yeşil değilse "Tebrikler, yeşil
#olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız" şeklinde çıktı veriniz. Senaryoya ait
#programı yazınız (20p).
uzaylinin_rengi = input("Uzaylının rengi (kırmızı|yeşil|sarı): ")

if uzaylinin_rengi == "yeşil":
    print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız :)")
else:
    print("Tebrikler, yeşil olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız :)")
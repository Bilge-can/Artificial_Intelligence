#if-elif-else yapılarını kullanarak bir insanın yaşam evreleri ile ilgili programı oluşturunuz. int
#türünde, yaş isminde bir değişken oluşturup, bu değişken için gerekli olan değeri kullanıcıdan
#isteyiniz (20p).
#a) Eğer bir insanın yaşı 2 yaşından küçük ise, "Bu kişi bebektir",
#b) Eğer bir insanın yaşı 2 ile 4 arasındaysa (2 dâhil) "Bu kişi yeni yürümeye başlayan çocuktur",
#c) Eğer bir insanın yaşı 4 ile 13 arasındaysa (4 dâhil) "Bu kişi çocuktur",
#d) Eğer bir insanın yaşı 13 ile 20 arasındaysa (13 dâhil) "Bu kişi ergendir",
#e) Eğer bir insanın yaşı 20 ile 65 arasındaysa (20 dâhil) "Bu kişi yetişkindir",
#f) Eğer bir insanın yaşı 65 ve üstü ise (65 dâhil) "Bu kişi yaşlıdır" şeklinde çıktı veriniz.


yas = int(input("Lütfen yaşınızı giriniz: "))
if yas < 2:
    print("Bu kişi bebektir.")
elif yas <= 4:
    print("Bu kişi yeni yürümeye başlayan çocuktur.")
elif yas <= 13:
    print("Bu kişi çocuktur.")
elif yas <= 20:
    print("Bu kişi ergendir.")
elif yas <= 65:
    print("Bu kişi yetişkindir.")
else:
    print("Bu kişi yaşlıdır.")

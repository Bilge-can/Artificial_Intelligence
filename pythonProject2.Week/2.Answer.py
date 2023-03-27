sayi = int(input("Lütfen bir sayı girin: "))

# Sayının basamak sayısını bulma
basamak_sayisi = 0
while sayi != 0:
    sayi //= 10
    basamak_sayisi += 1

# Sonucu ekrana yazdırma
print("Girilen sayı", basamak_sayisi, "basamaklıdır.")
a = int(input("Lütfen bir tam sayı giriniz (a): "))
b = int(input("Lütfen bir tam sayı giriniz (b): "))
c = int(input("Lütfen bir tam sayı giriniz (c): "))

# a (dahil) ve b (dahil) arasında kaç sayının c'ye bölünebildiğini hesapla
sayac = 0
for i in range(a, b+1):
    if i % c == 0:
        sayac += 1

# Sonucu ekrana yazdır
print("Girilen aralıkta", sayac, "adet sayı", c, "sayısına tam olarak bölünebilir.")






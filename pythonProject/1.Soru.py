#Kullanıcıdan 3 adet integer türünde değer alınız. Almış olduğunuz bu değerler bir üçgenin
#açılarını ifade edecektir. Bu açı değerlerine göre bu üçgenin dik, geniş ya da dar üçgen olup
#olmadığını belirleyen programı yazınız

# Kullanıcıdan açıları alıyoruz
a = int(input("1. açıyı giriniz: "))
b = int(input("2. açıyı giriniz: "))
c = int(input("3. açıyı giriniz: "))

# Aldığımız açıların toplamını hesaplıyoruz
aci_toplam = a + b + c

# Üçgenin geniş, dar ya da dik olup olmadığını belirliyoruz
if aci_toplam == 180:
    if a == 90 or b == 90 or c == 90:
        print("Bu üçgen bir dik üçgendir.")
    elif a > 90 or b > 90 or c > 90:
        print("Bu üçgen bir geniş üçgendir.")
    else:
        print("Bu üçgen bir dar üçgendir.")
else:
    print("Üçgen oluşturmak için toplam açı 180 derece olmalıdır.")
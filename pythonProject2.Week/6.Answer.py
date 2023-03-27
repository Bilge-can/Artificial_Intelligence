ip = input("Lütfen bir IP adresi giriniz: ")

# IP adresini noktalara göre parçala
parcalar = ip.split(".")

# Sonraki 5 değeri bul
for i in range(1, 6):
    # Sonraki değeri hesapla
    sonraki_deger = int(parcalar[3]) + i

    # Eğer sonraki değer 255'ten büyükse 0'a sıfırla
    if sonraki_deger > 255:
        sonraki_deger = 0
        parcalar[2] = str(int(parcalar[2]) + 1)
        if int(parcalar[2]) > 255:
            parcalar[2] = "0"
            parcalar[1] = str(int(parcalar[1]) + 1)
            if int(parcalar[1]) > 255:
                parcalar[1] = "0"
                parcalar[0] = str(int(parcalar[0]) + 1)
                if int(parcalar[0]) > 255:
                    parcalar[0] = "0"

    # IP adresinin sonraki değerini ekrana yazdır
    print(parcalar[0], parcalar[1], parcalar[2], sonraki_deger)

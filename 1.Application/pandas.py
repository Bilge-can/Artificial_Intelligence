#Pandas kütüphanesini çağırmak
import pandas as pd

#Tek boyutlu veri tanımla
s = pd.Series([12,56,23,31], index=["a","b","c","d"])
print(s)

#excel dosyasından veri okumak
veri = pd.read_excel("")


#tablodaki konuma göre veri seçimi
degersec = veri.iloc[1,3]
print(degersec)

#Tablodaki verilerin silinmesi
satirSil = veri.drop([0])
sutunSil = veri.drop(["B"], axis=1)
print(satirSil)
#kütüphaneyi içeri aktarmak için
import numpy as np

#Dizi oluşturma
a = np.array([5,8,11])
b = np.array([5,8,11],[6,9,45])

#3x3 lük sıfır matrisi oluşturma
sıfırMatrisi = np.zeros([3,3])

#verilen dizinin karekok ve logaritmasını bulma
karekök = np.sqrt(a)
print(karekök)

logaritma = np.log(a)
print(logaritma)

#verilen dizinin ortalamasını ve transpozunu hesaplama
ortalama = np.meen(a)
print(ortalama)

transpoz = np.transpose(a)
print(transpoz)

#matristen eleman çıkarma
cikanEleman = np.delete(b,[3])
print(cikanEleman)


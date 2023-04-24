#Gerekli Kütüphanelerin Sisteme Eklenmesi
from random import choice
from experta import *

class Dis(Fact):
    "Diş ağrısı ile ilgili genel bilgiler"
pass

class DisHastaliklari(KnowledgeEngine):
        @Rule(Dis(hastalik="diş eti kanaması"))
        def dis_eti_kanamasi(self):
          print("Diş hastalığın var diş hekimine başvur")

        @Rule(Dis(hastalik="uzun süreli diş eti kanaması"))
        def uzun_sureli_dis_eti_kanamasi(self):
          print("Diş eti çekilmesi var diş hekimine başvur")

        @Rule(Dis(hastalik="diş eti çekilmesi var ve diş kökü görünüyor"))
        def dis_eti_cekilmesi(self):
          print("Dolgu yaptır")

        @Rule(Dis(hastalik="dişte yiyecek ve içeceklerden oluşan renk değişimi var"))
        def renk_degisimi(self):
          print("Dişleri temizlet")

        @Rule(Dis(hastalik="yeni diş çıkarken morarma varsa"))
        def morarma(self):
          print("Diş hekimine başvur")

        @Rule(Dis(hastalik="dişte ağrı yapmayan çürük varsa"))
        def cürük(self):
           print("Dolgu yaptır")

        @Rule(Dis(hastalik="dişteki çürük ileri derecedeyse"))
        def ileri_derece_cürük(self):
           print(" kanal tedavisi ve dolgu yaptır")


uzman=DisHastaliklari()
uzman.reset()
uzman.declare(Dis(hastalik=choice(["diş eti kanaması", "uzun süreli diş eti kanaması", "diş eti çekilmesi var ve diş kökü görünüyor", "dişte yiyecek ve içeceklerden oluşan renk değişimi var", "yeni diş çıkarken morarma varsa", "dişte ağrı yapmayan çürük varsa", "dişteki çürük ileri derecedeyse"])))
uzman.run()
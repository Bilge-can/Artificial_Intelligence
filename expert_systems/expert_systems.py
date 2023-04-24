#Gerekli Kütüphanelerin Sisteme Eklenmesi

from random import choice
from experta import *

class Isik(Fact):
    "Trafik ışıklarıyla ilgili genel bilgiler"
pass

class KarşıdanKarşıyaGeçme(KnowledgeEngine):
    @Rule(Isik(renk="yeşil"))
    def yeşil_ışık(self):
        print("Yeşil ışık yandığı için yürüyebilirsiniz.")

    @Rule(Isik(renk="kırmızı"))
    def kırmızı_ışık(self):
        print("Kırmızı ışık yandığı için bekleyin.")

    @Rule(Isik(renk="sarı"))
    def sarı_ışık(self):
            print("Sarı ışık yandığı için dikkatli olun.")

uzman=KarşıdanKarşıyaGeçme()
uzman.reset()
uzman.declare(Isik(renk=choice(["yeşil", "sarı", "kırmızı"])))
uzman.run()
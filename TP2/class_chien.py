#coding:utf-8
#Class mère
#Initialisation de notre class
from class_animal import Animal
#Heritage (classe fille)
class Chien(Animal):
    def __init__(self, c_nom, c_age):
        super().__init__(c_nom, c_age)
        self.type="Chien"
        self.sound="ouaf"
    def cri(self):
        return super().cri(self.sound)
        

# print("LES CHIIENS DE NOTRE FERME")
# #Programme principal
# chien1 = Chien("Loulou", 2)
# chien1.cri()

# chien2 = Chien("Métan", 4)
# print(chien2.aboit)




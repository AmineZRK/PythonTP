#coding:utf-8
#Class mère
   #Initialisation de notre class
from class_animal import Animal
#Heritage (classe fille)
class Chat(Animal):
     def __init__(self, c_nom, c_age):
          super().__init__(c_nom,c_age)
          self.type="Chat"
          self.sound="Miaou"
          
     def cri(self):
          return super().cri(self.sound)
        
# #Programme principal
# print("LES CHATS DE NOTRE FERME")
# chat1 = Chat("Ben", 5)
# chat1.cri()

# chat1 = Chat("Métan", 3)
# chat1.cri()



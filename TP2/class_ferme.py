#coding:utf-8
from class_chien import Chien
from class_chat import Chat
from utils import *
class Ferme():
     animaux=[]
     def __init__(self):
          print("ANIMAUX DE LA FERME")
          self.animaux
         
     #Création de nos méthodes (Simple, de classe et Statique)
     #Methode simple (stantard)
     def ajouter_animal(self, add):
          print("le {} {} est ne".format(add.type, add.nom))
          self.animaux.append(add)
         
     def crier(self):
          for i in self.animaux:
               i.cri()

     def tuer(self,nom):
          exist=False
          for i in self.animaux:
               if i.nom==nom:
                    self.animaux.remove(i)
                    print("le {} {} est mort".format(i.type, i.nom))
                    exist=True
          return exist
     def __str__(self) -> str:
          return f'Ma ferme a {len(self.animaux)} animaux'
               
         

#CREATION DE NOS OBJETS
f1 = Ferme()

#Appel de la methode simple
# f1.ajouter_animal(Chat('cho',2))
# f1.ajouter_animal(Chien('lolo',3))
# f1.crier()
# print(f1.animaux)
n=True
while n:
     menu=input("\n1- Ajouter un animal \n2- Lancer le cri de tous les animaux de la ferme. \n3- Tuer un animal \n4- consulter la ferme\n5- Quitter le programme\n")
     menu = int(menu)
     if menu ==1:
        ajouter(f1)
     elif menu ==2:
        Crier(f1)
     elif menu==3:
        Tuer(f1)
     elif menu ==4:
        nombre(f1)
     elif menu==5:
          n=False
     else:
          menu=input("\n1- Ajouter un animal \n2- Lancer le cri de tous les animaux de la ferme. \n3- Tuer un animal \n4- consulter la ferme\n5- Quitter le programme\n")

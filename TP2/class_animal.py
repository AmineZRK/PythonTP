#coding:utf-8
class Animal():

     #Initialisation de notre class
     def __init__(self, c_nom, c_age):
         #self cible l'objet que nous avons crée
        #  print("Création d'un Animal...")
         self.nom = c_nom
         self.age = c_age
         
     #Création de nos méthodes (Simple, de classe et Statique)
     #Methode simple (stantard)
     def cri(self, message):
         #print("{} : {}".format(self.nom, self.age))
         print("Le cri de {} : {}".format(self.nom, message))
         
print("LANCEMENT DU PROGRAMME...")

# #CREATION DE NOS OBJETS
# a1 = Animal("Ben", 5)

# #Appel de la methode simple
# a1.cri("ahahahahahhahahahahahahwouwouwouwouwou !")


class Player:
    def __init__(self,nature,prenom,logo) -> None:
        self.nature=nature
        self.prenom=prenom
        self.point =0
        self.nbr_choisie=0
        self.liste_nbr_choisie= []
        self.logo =logo
        self.nbr_choisie_to_check=set()
    def gagner_point(self,point=5):
        self.point+=point
        print(f"Excellent ! le {self.nature} {self.prenom} a {self.point} pts Bravo 👏👏")
    def perdre_point(self,point=5):
        self.point-=point
        print(f"Oh non.... ! Je me suis fait arrèté par 👮 ")
    def choisir_nbr(self,message=" choisie une position entre 1 et 9:  "):   
        while True: #gere l'entre d'utilisateur pour le nombre de la table et ajoute a la liste
            try:
                nbr = int(input("le "+self.nature+" "+self.prenom+message))
                if 1<=nbr<=9:
                    self.liste_nbr_choisie.append(nbr)
                    self.nbr_choisie_to_check.add(nbr)
                    break
                print("Un chiffre compris entre 1 et 9 😓")
            except ValueError:
                print("😊 vous devez entre un chiffre compris entre 1 et 9")
    def __gt__(self,player:object):
        return self.point >player.point
class Voleur(Player):
    nature = "Voleur"
    def __init__(self,prenom, logo) -> None:
        super().__init__(self.nature, prenom, logo)
    def check_escape(self):
        liste_to_win =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for win_type in liste_to_win:
            if self.nbr_choisie_to_check.issuperset(win_type):
                print("Bien jouer tu t'ai enfuis ----✈ ------------✈ --------------✈ ---------------✈")
                self.gagner_point()

class Game:
    def __init__(self) -> None:
        self.run = True
    def __str__(self) -> str:
        return "\n--------------------------BIENVENUE DANS LE JEU 💻 DE Morpion-----------------------------------------\n"
    def afficher_regle(self):
        return print(""" vous avez tous jouer au jeu de morpion dans l'enfance 👶 je vous explique
        
        1.Le jeu se joue entre deux joueurs chacun son tour
        2.Vous disposer de deux truc 👮 le police pour le joueur 1 et 🙈 le voleur pour le joueur 2
        3.Vous etes dans un carre de 3x3 (une cote de 3 partie)
            POUR GaGner 🙌 
        4.Il faut trouver un chemin de sortie sans se faire Arreter par le policier
            Perdu 🙍
        5.Si vous vous faite arreter avant de sortir de la zone des policiers 👮👮👮👮👮

        NB: A chaque manche si vous gagner vous recevez 2 pts sinon on soutira -2 pts même à Zero vous 5 manche
                            
                            
                        -----BONNE CHANCE-----

        """)
    @property
    def runnig(self): #pour effectuer la boucle du jeu   
        return self.run
    @runnig.setter
    def runnig(self,donne:str):
        self.run = False if donne==2 else True
        
    def turn(self,player:Player): 
        joueur= player
        print("-------------------c'est le tour du ",player.nature,player.prenom)
        return joueur

    def check_winner(self,player1,player2):
        if player1 >player2:
            print("         Ooooooh GAME OVER 💣") 
            player1.gagner_point() 
        else:
            print("     WINNER !           🙌🙌🙌")

class Table:
    def __init__(self,x:int,y:int) -> None:
        self.x =x
        self.y =y
        self.liste = list(range(1,11))
    def table(self):
        x=0
        print("  ",end=""),print("________"*self.x)   
        for y in range(1,self.y+1):
            print(y,end=" |")
            for _ in range(1,self.x+1):
                print(f"__{self.liste[x]}__|",end="")
                x+=1
            print()
    def update(self,player:Player):
        while not type(self.liste[player.liste_nbr_choisie[-1]-1])== int: 
            player.choisir_nbr()   
            print("     ❎ Quelqu'un a dejà passé par ici")
        self.liste[player.liste_nbr_choisie[-1]-1]=player.logo
                #verifier si le voleur c'est enfuit
        self.table()


#----------------------------------MENU-----------------------------------------------------------
#creation des objets
game = Game() # le jeu
player1,player2=Player("Policier","Mc man","O"),Voleur("venard","X") #les joueurs
new_table = Table(3,3)

print(game) # pour presenter le nom du jeu
game.afficher_regle()

#afficher la table morpion
new_table.table()
print(),print()
#creer la boucle du jeu
while game.runnig:
    player2.choisir_nbr(" choisie une position de depart compris entre 1 et 9: ")
    new_table.update(player2)
    game.turn(player1)
    for _ in range(4):
        player1.choisir_nbr()
        new_table.update(player1)
        game.turn(player2)
        player2.choisir_nbr()
        new_table.update(player2)
        player2.check_escape() #verifier s'il est enfuit
        game.turn
    game.check_winner(player1,player2)
    print("---"*30)
        
    demande_runnig = int(input("\n                🙆  REJOUER ? Appuyer sur:\n            1 pour rejouer\n            2 pour Quitter\n        ^_^: "))
    if demande_runnig in [1,2]:
        game.runnig = demande_runnig

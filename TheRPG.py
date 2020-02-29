from random import randint
import time

class Slime:
    """
    Classe qui représente un slime.
    """
    def __init__(self):
        self.name = "Slime"
        self.life = 5
        self.strengh = 2


class Hero:
    """
    Classe représentant le personnage.
    """
    def __init__(self):
        self.gender = askGender()
        self.name = askName(self.gender)
        self.level = 1
        self.experience = 0
        self.life = 10
        self.mana = 5
        self.strengh = 1
        self.intelligence = 1
        self.chance = 1
        self.vitality = 1
        self.precision = 1

    def manageStat(self, stat_pt):
        """
        Fonction qui permet d'ameiliorer les statistiques de notre personnage.
        """
        while stat_pt > 0:
            print("Tu as", stat_pt,"points à placer")
            answer = grepAnswer()
            if answer == "for":
                self.strengh += 1
                print("+1 en Force\n")
                stat_pt -= 1
            if answer == "int":
                self.intelligence += 1
                print("+1 en Intelligence\n")
                stat_pt -= 1
            if answer == "cha":
                self.chance += 1
                print("+1 en Chance\n")
                stat_pt -= 1
            if answer == "vit":
                self.vitality += 1
                print("+1 en Vitalité\n")
                stat_pt -= 1
            if answer == "pre":
                self.precision += 1
                print("+1 en Précision\n")
                stat_pt -= 1
    
    def showStat(self):
        """
        La fonction montre les statistiques du personage.
        """
        print("Force :", self.strengh)
        print("Intelligence :", self.intelligence)
        print("Chance :", self.chance)
        print("Vitalité :", self.vitality)
        print("Précision :", self.precision)
        print("Vie :", "<3 "*self.life)
        print("Magie :", "@ "*self.mana)
        print("Niveau :", self.level)
        print("Xp :", self.experience, "\n")
            

def grepAnswer():
    """
    La fonction collecte les entrées clavier du joueur.
    """
    answer = input()
    return answer

def askGender():
    """
    La fonction pose la question homme ou femme.
    Elle renvoie le genre du personage.
    """
    while(1):
        print("Bonjour à toi aventurier, avant de commencer ton époppé présente toi.Est-tu un homme ou une femme? [H/F]")
        gender = grepAnswer()
        if gender == "F" or gender == "H":
            return gender

def askName(gender):
    """
    La fonction demande le prénom du personage.
    Elle renvoie le prenom du personage.
    gender : chaîne de caractère.
    """

    if gender == "F":
        print("Si tu es prête à devenir une légende dit moi ton nom FEMME!")
        name = grepAnswer()
    elif gender == "H":
        print("Si tu es prêt à devenir une légende dit moi ton nom CHIEN!")
        name = grepAnswer()
    return name
    
def introStat():
    """
    La fonction présente les diffenrentes statistique du joueur.
    Elle renvoie 5.
    """
    print("Bon par défaut t'as 1 partout de vraies statistiques de gros noob.")
    print("Je suis gentil je t'offre 5 points de talent, places les judicieusement.")
    print("Tes statistiques sont les suivantes :")
    print("Force (for), ça sert à casser des bouches plus fort.")
    print("Intelligence (int), pratique pour augmenter la puissance du barbeuc de mob.")
    print("Chance (cha), ça évite que le dé de la DESTINY OF DOOM APOCALYPTIQUE te bolosse de trop.")
    print("Vitalité (vit), plus t'en as moins t'as mal.")
    print("Précision (pre), avec ça tu deviens le roi des sniper.\n")
    return 5

def rollTheDice():
    """
    Fait un lancer de dé 100.
    """
    return randint(1, 101)

def statOnDice(dice, stat, op):
    """
    Modifie la valeur d'un dé en fonction d'une statistique du perso.
    renvoie la valeur de dé modifié.
    dice: entier
    stat: entier
    op: + ou -
    >>> statOnDice(56, 18, "+")
    66
    >>> statOnDice(95, 18, "-")
    78
    """
    dice = float(dice)
    impact = dice/100 * float(stat)
    if op == "+":
        dice += impact
    if op == "-":
        dice -= impact
    return round(dice)



def initiative(player, monster):
    """
    Renvoie True si le joueur réussi le jet d'initiave.
    False si c'est le monstre.
    """
    #jet de dé sans les stats joueur/monstre.
    player_dice = rollTheDice()
    print("Jet de", player.name,":", player_dice)
    monster_dice = rollTheDice()
    
    #ajout des stats joueur sur son lancé.
    player_dice = statOnDice(player_dice, player.chance, "+")
    print("Jet de", player.name,":", player_dice)
    print("Jet de", monster.name,":", monster_dice, "\n")
    if monster_dice > player_dice:
        return False
    return True

def attack(turn, player, monster):
    """
    gère le tour d'attaque en fonction du monstre ou du joueur.
    renvoie True si c'est le tour du monstre, False si c'est celui du joueur.
    turn : booléen qui représente soit le tour du monstre soit celui du joueur.
    """
    if turn == True:
        print(player.name, "prépares ton attaque")
        attack_dice = rollTheDice()
        print(player.name, "tu as fait un", attack_dice)
        attack_dice = statOnDice(attack_dice, player.precision, "-")
        print(player.name, "tu as fait un", attack_dice)
        if attack_dice <= 50:
            print("lancé réussi")
            monster.life -= player.strengh
            print("PV", monster.name, ":", monster.life, "\n")
        else:
            print("lancé échoué\n")
        return False
    elif turn == False:
        print(monster.name, "prépare son attaque")
        attack_dice = rollTheDice()
        print(monster.name, "a fait un", attack_dice)
        if attack_dice <= 50:
            print("lancé réussi")
            if player.vitality < monster.strengh:
                attack_monster = monster.strengh - player.vitality
                player.life -= attack_monster
                print("PV :", player.life, "\n")
            else:
                print(monster.name, "ne vous a fait aucun dégat.")  
        else:
            print("lancé échoué\n")
        return True

def fight(player, monster):
    """
    La fonction gère les combats entre le joueur et un monstre.
    renvoie le vainqueur.
    """
    turn = initiative(player, monster)
    while player.life > 0 or monster.life > 0 :
        turn = attack(turn, player, monster)
        if player.life <= 0:
            return monster.name
        elif monster.life <= 0:
            return player.name
        
def winFight(winner, player):
    """
    Affiche qui à gagner le combat.
    """
    print(winner, "a gagné le combat")
    if winner == player.name:
        print("Bravo")

def loseFight(winner, player):
    """
    Affiche si le personnage à perdu le combat
    winner : chaîne de caractère.
    """
    if winner != player.name:
        print("Bouhhh")
        

    
    


if __name__=="__main__":

    player = Hero()
    
    stat_pt = introStat()
    
    player.manageStat(stat_pt)
    
    player.showStat()

    monster = Slime()

    winner = fight(player, monster)

    winFight(winner, player)

    loseFight(winner, player)



    













    import doctest
    doctest.testmod()
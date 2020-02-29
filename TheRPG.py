


class Personnage:
    """Classe représentant le personnage"""

    def __init__(self):
        self.sexe = askGender()
        self.name = askName(self.sexe)
        self.level = 1
        self.experience = 0
        self.life = 10
        self.mana = 5
        self.strengh = 1
        self.intelligence = 1
        self.dexterity = 1
        self.chance = 1
        self.vitality = 1
        self.precision = 1

    def manageStat(self, stat_pt):
        while stat_pt > 0:
            print("Tu as", stat_pt,"points à placer")
            answer = grepAnswer()
            if answer == "for":
                self.strengh += 1
                print("+1 en Force")
                stat_pt -= 1
            if answer == "int":
                self.intelligence += 1
                print("+1 en Intelligence")
                stat_pt -= 1
            if answer == "dex":
                self.dexterity += 1
                print("+1 en Dextérité")
                stat_pt -= 1
            if answer == "cha":
                self.chance += 1
                print("+1 en Chance")
                stat_pt -= 1
            if answer == "vit":
                self.vitality += 1
                print("+1 en Vitalité")
                stat_pt -= 1
            if answer == "pre":
                self.precision += 1
                print("+1 en Précision")
                stat_pt -= 1
    
    def showStat(self):
        """
        La fonction montre les statistiques du personage.
        """
        print("\nForce :", self.strengh)
        print("Intelligence :", self.intelligence)
        print("Dextérité :", self.dexterity)
        print("Chance :", self.chance)
        print("Vitalité :", self.vitality)
        print("Précision :", self.precision)
        print("Vie :", "<3 "*self.life)
        print("Magie :", "@ "*self.mana)
        print("Niveau :", self.level)
        print("Xp :", self.experience)
            

def grepAnswer():
    """
    La fonction collecte les entrées clavier du joueur.
    """
    answer = input()
    return answer

def askGender():
    """
    La fonction pose la question homme ou femme.
    Elle renvoie le sexe du personage.
    """
    while(1):
        print("Bonjour à toi aventurier, avant de commencer ton époppé présente toi.\nEst-tu un homme ou une femme? [H/F]")
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
    print("\nBon par défaut t'as 1 partout de vraies statistiques de gros noob.")
    print("Je suis gentil je t'offre 5 points de talent, places les judicieusement.")
    print("Tes statistiques sont les suivantes :")
    print("Force (for), ça sert à casser des bouches plus fort.")
    print("Intelligence (int), pratique pour augmenter la puissance du barbeuc de mob.")
    print("Chance (cha), ça évite que le dé de la DESTINY OF DOOM APOCALYPTIQUE te bolosse de trop.")
    print("Dextérité (dex), tu pensais pouvoir utiliser les armes comme tu veux? BAH NON!")
    print("Vitalité (vit), plus t'en as moins t'as mal.")
    print("Précision (pre), avec ça tu deviens le roi des sniper.")
    return 5
    

if __name__=="__main__":

    player = Personnage()
    stat_pt = introStat()
    player.manageStat(stat_pt)
    player.showStat()













    import doctest
    doctest.testmod()
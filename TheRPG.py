# _____Modules_____

from random import randint
import time

from language.fr import FrTexts
from language.en import EnTexts

# _____Classes_____


def writeText(s):
    print(s)


class Slime:
    def __init__(self):
        """Constructeur de la classe Slime"""

        self.name = "Slime"  # Nom
        self.life = 5  # Points de vie
        self.strengh = 2  # Points de force (= puissance d'attaque)


class Hero:
    def __init__(self):
        """Constructeur de la classe Hero"""

        self.texts = askLanguage()
        self.name = askName()  # Nom
        self.level = 1  # Niveau
        self.experience = 0  # Expérience
        self.life = 10  # Points de vie
        self.mana = 5  # Points de magie
        self.strengh = 1  # Points de force (= puissance d'attaque)
        self.intelligence = 1  # Points d' intelligence, augmente la chance de caster un sort
        self.chance = 1  # Points de chance, augmente la chance sur un lancé de dé hors combat
        self.vitality = 1  # Points de vitalité, défense naturelle du personnage
        self.precision = 1  # Points de précision, augmente la chance de faire une attaque physique

    def manageStat(self, tal_point):
        """Fonction qui permet d'améliorer les statistiques de notre personnage.

        self (Hero)
        tal_point (entier) : points de statistique à attribuer 
        """

        while tal_point > 0:  # La boucle finit quand il n'y a plus de points de statistique à attribuer

            print(self.texts.getPointsText(tal_point))
            answer = grepAnswer()  # Récupération du choix de l'utilisateur

            if answer == "for":  # Amélioration de la force

                self.strengh += 1  # Incrémentation de la statistique
                print("+1 en Force\n")
                tal_point -= 1  # Décrémentation du nombre de tal_point

            if answer == "int":  # Amélioration de l'intelligence

                self.intelligence += 1
                print("+1 en Intelligence\n")
                tal_point -= 1

            if answer == "cha":  # Amélioration de la chance

                self.chance += 1
                print("+1 en Chance\n")
                tal_point -= 1

            if answer == "vit":  # Amélioration de la vitalité

                self.vitality += 1
                print("+1 en Vitalité\n")
                tal_point -= 1

            if answer == "pre":  # Amélioration de la précision

                self.precision += 1
                print("+1 en Précision\n")
                tal_point -= 1

    def showStat(self):
        """La fonction affiche les statistiques du personnage."""

        print("Force :", self.strengh)
        print("Intelligence :", self.intelligence)
        print("Chance :", self.chance)
        print("Vitalité :", self.vitality)
        print("Précision :", self.precision)
        print("Vie :", "<3 "*self.life)
        print("Magie :", "@ "*self.mana)
        print("Niveau :", self.level)
        print("Xp :", self.experience, "\n")


# _____Fonctions_____

def grepAnswer():
    """La fonction récupère les entrées au clavier, puis les renvoies."""

    answer = input()

    return answer


def askName():
    """La fonction demande le prénom du personage, puis le renvoie."""

    print("Si tu es prêt à devenir une légende dit moi ton nom CHIEN!")
    name = grepAnswer()

    return name


def introStat():
    """La fonction présente les diffenrentes statistiques du joueur, puis renvoie des points de talent (= tal_point)."""

    print("Bon par défaut t'as 1 partout de vraies statistiques de gros noob.")

    print("Tes statistiques sont les suivantes :")
    print("Force (for), ça sert à casser des bouches plus fort.")
    print("Intelligence (int), pratique pour augmenter la puissance du barbeuc de mob.")
    print("Chance (cha), ça évite que le dé de la DESTINY OF DOOM APOCALYPTIQUE te bolosse de trop.")
    print("Vitalité (vit), plus t'en as moins t'as mal.")
    print("Précision (pre), avec ça tu deviens le roi des sniper.\n")

    print("Je suis gentil je t'offre 5 points de talent, places les judicieusement.")
    tal_point = 5

    return tal_point


def rollTheDice():
    """Émule un lancer de dé 100."""

    return randint(1, 101)


def statOnDice(dice, stat, op):
    """Modifie la valeur d'un dé en fonction d'une statistique, puis renvoie la valeur du dé modifié.

    dice (entier) : un dé
    stat (entier) : statistique (= force, chance, intelligence, etc...)
    op (chaîne de caractère) : "+" ou "-", change par rapport à l'action du dé

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
    """La fonction détermine qui du joueur ou du monstre à l'initiative. Elle renvoie True pour le joueur, False sinon.

    player (classe)
    monster (classe)
    """

    player_dice = rollTheDice()  # Lancé de dé du joueur
    monster_dice = rollTheDice()  # Lancé de dé du monstre
    # Ajout de la statistique de chance sur le dé du joueur
    player_dice = statOnDice(player_dice, player.chance, "+")

    print("Jet de", player.name, ":", player_dice)
    print("Jet de", monster.name, ":", monster_dice, "\n")

    if monster_dice > player_dice:  # Comparaison du score des deux dés

        return False  # Dé du monstre qui à le plus gros score

    # Dé du joueur qui à le plus gros score ou égalité entre les deux dés.
    return True


def attack(turn, player, monster):
    """La fonction gère le tour d'attaque en fonction du monstre ou du joueur, puis renvoie True si c'est le tour du monstre, False si c'est celui du joueur.

    turn (booléen) : Représente soit le tour du monstre soit celui du joueur.
    player (classe)
    monster (classe)
    """

    if turn == True:  # Tour du joueur

        print(player.name, "prépares ton attaque")
        # Lancement du dé qui détermine si le joueur réussi à lancer une attaque
        attack_dice = rollTheDice()
        print(player.name, "tu as fait un", attack_dice)
        # Augmentation de la précision de l'attaque, de la chance qu'elle soit éxécutée
        attack_dice = statOnDice(attack_dice, player.precision, "-")
        print(player.name, "tu as fait un", attack_dice)

        if attack_dice <= 50:  # L'attaque est lancée

            print("lancé réussi")
            # Le monstre reçoit autant de dégat que le joueur a de force
            monster.life -= player.strengh
            print("PV", monster.name, ":", monster.life, "\n")

        else:  # L'attaque échoue

            print("lancé échoué\n")

        return False  # Au tour du monstre de tenter une attaque

    elif turn == False:  # Tour du monstre

        print(monster.name, "prépare son attaque")
        # Lancement du dé qui détermine si le monstre réussi à lancer une attaque
        attack_dice = rollTheDice()
        print(monster.name, "a fait un", attack_dice)

        if attack_dice <= 50:  # L'attaque est lancée

            print("lancé réussi")

            if player.vitality < monster.strengh:  # Si l'attaque du monstre est plus haute que la vitalité du joueur

                # L'attaque du monstre est égale à la force du monstre moins la vitalité du joueur
                attack_monster = monster.strengh - player.vitality
                # L'attaque du monstre détermine le nombre de dégat mis au joueur
                player.life -= attack_monster
                print("PV :", player.life, "\n")

            else:  # La défense du joueur est trop haute, le joueur ne reçoit pas de dégat

                print(monster.name, "ne vous a fait aucun dégat.")

        else:  # L'attaque échoue

            print("lancé échoué\n")

        return True  # Au tour du joueur de tenter une attaque


def fight(player, monster):
    """La fonction gère le déroulé d'un combats entre le joueur et un monstre, puis renvoie le nom du vainqueur.

    player (classe)
    monster (classe)
    """

    turn = initiative(player, monster)  # Détermine qui commence à attaquer

    while player.life > 0 or monster.life > 0:  # Tant qu'il n'en reste pas qu'un

        # Le combat au tour par tour commence
        turn = attack(turn, player, monster)

        if player.life <= 0:  # Si le joueur meurt

            return monster.name  # On renvoie le nom du monstre

        elif monster.life <= 0:  # Si le monstre meurt

            return player.name  # On renvoie le nom du joueur


def winFight(winner, player):
    """Affiche qui a gagné le combat."""

    print(winner, "a gagné le combat")

    if winner == player.name:

        print("Bravo")


def loseFight(winner, player):
    """Affiche si le personnage à perdu le combat.

    winner (chaîne de caractère) : Le nom de celui qui à gagné le combat
    player (classe)
    """

    if winner != player.name:  # Si le gagnat n'est pas le joueur

        print("Bouhhh")  # SHAME ON YOU


# _____Main_____

if __name__ == "__main__":

    player = Hero()

    tal_point = introStat()

    player.manageStat(tal_point)

    player.showStat()

    monster = Slime()

    winner = fight(player, monster)

    winFight(winner, player)

    loseFight(winner, player)

    import doctest
    doctest.testmod()

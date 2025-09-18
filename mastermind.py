import os
import random as r
fr_color=["Rouge","Vert","Bleu","Jaune","Mauve","Noir"]
color=["Red","Green","Blue","Yellow","Purple","White"]
new_color=[]


#partie initialisation fichier:

nbParties=".nbParties"
score=".score"
def initialisation_fichier():
    if not os.path.exists(score):
        with open(score, 'w') as s:
            s.write("0")
    if not os.path.exists(nbParties):
        with open(nbParties, 'w') as nb:
            nb.write("0")


#partie extraction valeur de test:
def lire_score(ajout):







#fonction qui liste les couleurs:
def couleur(liste):                           
    print("Voici les couleurs possible :")    #
    for color in liste:                       # prends toutes les valeurs de la liste de couleur connue
        print("-",color)

#fonction qui renvoie une liste des initiales des couleurs :
def create_couleur(l):                        
    premiere_lettre=[]                     
    for col in l:                             #prend chaque couleurs de la liste et la boucle prend la premiere lettre du mot
        premiere_lettre.append(col[0])
    return premiere_lettre 

# fonction qui crée le code initial
def create_code(l_color):                     #mettre liste avec seulement les premieres lettres
    code=[]
    for i in range(4):                        # pour plus tard changer ici pour modifier le nombre de couleur du code final
        code.append(l_color[r.randint(0,len(l_color)-1)])   #ajoute a la liste code une couleur  au hazard 
    return code

#foncion qui demande la langue voulue pour les couleurs
def choix_color():
    print("Voulez vous les couleurs en Francais ou en Anglais?")
    choix=int(input("Indiquez 1 pour Francais et 2 pour Anglais: "))
    if choix==1: return fr_color
    elif choix==2: return color
    else: return new_color


#fonction "test" qui cherche les valeurs corrects et partiellement correct
def test(val,code):               #val est la liste du code de la personne
    correct=0
    partiel=0
    i=0
    pop=[]                        #retiens les indices qu'on va pop
    while i<len(code):
        if code[i]==val[i]:       #compare valeur (pour valeur exacte)
            correct+=1
            code.pop(i)
            val.pop(i)
        else:
            i+=1
    i=0                           #indice pour parcourir val
    j=0                           #indice pour parcourir code
    boo=True
    while i<len(val):             #boucle qui depend de la taille de val (car elle va varier)
        boo=True
        j=0
        while boo and j<len(code):# boucle qui elle depend de la taille de code et d'un booléen
            if val[i]==code[j]:   #si valeur égale l'enlever
                code.pop(j)
                val.pop(i)
                partiel+=1
                i-=1             #j'enleve 1 car j'en rajoute un obligatoirement apres et pas besoin de changer d'indice
                boo=False
            j+=1
        i+=1
    return correct,partiel         #je laisse écrire la phrase dans le main





def main():
    #lancement des fonctions de bases
    langue=choix_color()                 
    ini_langue=create_couleur(langue)
    final=create_code(ini_langue)
    print("final code=",final)
    fin=12
    essai=0
    gagne=True
    print("Bienvenue dans Mastermind !")
    print("Devinez le code de 4 couleurs parmi celles proposées.") 
    couleur(langue)
    print("Entrez les initiales des couleurs, exemple : RGYP (respecter les lettres affichées)")
    while essai < fin and gagne:
        reponse=input("Entrez votre réponse: ").upper()

        reponse = list(reponse)

        correct,partiel=test(reponse,final)
        print(f"Correct : {correct} | Partiel : {partiel}")
        essai+=1
        print(type(correct))
        
        if correct == 4:
            gagne = True
            print(f"Bravo ! Vous avez trouvé le code en {essai} tentative(s) 🎉")
            print(f"Score final : {fin - essai}")
        elif essai == fin:
            print("Dommage, vous avez épuisé tous vos essais 😞")
            print("Le code était :", ''.join(final))





main()


"""

Si vous souhaitez changer les couleurs soit ajouter ou supprimer une couleur dans la langue Francaise 
aller ligne 2 et  rajouter votre langue en suivant l'exmple ci-dessous:

exemple: vous souhaitez ajouter gris dans-----> fr_color=["Rouge","Vert","Bleu","Jaune","Mauve","Noir"] 
rajoutez le en ecrivant-> ,"gris"      cela donnera: fr_color=["Rouge","Vert","Bleu","Jaune","Mauve","Noir","Gris] 
faites de meme a la ligne 3 si vous souhaitez modifier les couleurs en anglais


Cependant si vous voulez crée votre propre code couleur, il est mis a votre disposition ligne 4 new_color=[]
qui est vide ainsi vous pouvez ajouter autant de couleur souhaitez dans la langue de votre choix suivant le
même schema d'éxécution que ci dessus


si vous souhaitez modifié la longueur du code final, il vous suffira:
-de regarder la ligne 22:
                for i in range(4)     et modifier le 4 par la taille du code final que vous souhaitez
-modifier le chiffre 4 de la ligne 92 par la taille choisie


Pour ce qui est du nombre de tentative si vous souhaitez le modifier, il vous suffira d'aller a la ligne 75 
et de modifier le chiffre 12 par le nombre de tentative souhaité
"""
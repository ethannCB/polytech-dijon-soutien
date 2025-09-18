import random as r
fr_color=["Rouge","Vert","Bleu","Jaune","Mauve","Noir"]
color=["Red","Green","Blue","Yellow","Purple","White"]


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

def create_code(l_color):    #mettre liste avec seulement les premiere lettres
    code=[]
    for i in range(4):              # pour plus tard changer ici pour modifier le nombre de couleur du code final
        code.append(l_color[r.randint(0,len(l_color)-1)])   #ajoute a la liste code une couleur  au hazard 
    return code

def choix_color():
    print("Voulez vous les couleurs en Francais ou en Anglais?")
    choix=int(input("Indiquez 1 pour Francais et 2 pour Anglais: "))
    if choix==1: return fr_color
    else: return color

def test(val,code):    #val est la liste du code de la personne
    correct=0
    partiel=0
    i=0
    pop=[]                        #retiens les indices qu'on va pop
    while i<len(code):
        if code[i]==val[i]:
            correct+=1
            code.pop(i)
            val.pop(i)
        else:
            i+=1
    i=0                         #indice pour parcourir val
    j=0                         #indice pour parcourir code
    boo=True
    while i<len(val):
        boo=True
        j=0
        while boo and j<len(code):
            if val[i]==code[j]:
                code.pop(j)
                val.pop(i)
                partiel+=1
                i-=1                             #j'enleve 1 car j'en rajoute un obligatoirement apres et pas besoin de changer d'indice
                boo=False
            j+=1
        i+=1
    return correct,partiel    #je laisse écrire la phrase dans le main





def main():
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
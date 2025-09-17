import random as r
fr_color=["Rouge","Vert","Bleu","Jaune","Mauve","Noir"]
color=["Red","Green","Blue","Yellow","Purple","White"]

def couleur(liste):
    print("Voici les couleurs possible :")
    for color in liste:
        print("-",color)

def create_couleur(l):
    premiere_lettre=[]
    for col in l:
        premiere_lettre.append(col[0])
        print(col[0])
    return premiere_lettre 

def create_code(l_color):
    code=[]
    for i in range(4):              # pour plus tard changer ici pour modifier le nombre de couleur du code final
        code.append(l_color[r.randint(0,len(l_color)-1)])   #ajoute a la liste code une couleur  au hazard 
    return code

def main():



print(create_couleur(color))
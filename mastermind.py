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

print(create_couleur(color))
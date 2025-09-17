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

def test(val,code):
    correct=0
    partiel=0
    i=0
    pop=[]                        #retiens les indices qu'on va pop
    while i<len(code):
        #print(i)*
        print(code[i],val[i])
        if code[i]==val[i]:
            print("ok")
            print(code,val)
            correct+=1
            code.pop(i)
            val.pop(i)
        else:
            i+=1
    #for j in range(len(code)):





#def main():




test(["A","B","C","D"],["A","B","D","C"])
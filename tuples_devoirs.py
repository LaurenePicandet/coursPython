

#Écrire un programme qui compte le nombre de fois qu’un élément est répété dans un tuple (méthode count()).

t = (1,2,3,4,5,5,5,5,6,8,9)
def countRepetitions(t, e):
    return t.count(e)

print(countRepetitions(t,5))

#Écrire un programme qui supprime un élément d’un tuple.

#on ne peut pas modifier un tuple ! Je crée donc une liste en recopiant tous les éléments du tuple à conserver,
#puis je la convertis en tuple

t = (1,2,3,4,5,5,5,5,6,8,9)

def supprElement(t,e):
    t2=[]
    for i in range(len(t)):
        print(t[i])
        if t[i] != e:
            t2.append(t[i])
    return t2

print(supprElement(t,8))



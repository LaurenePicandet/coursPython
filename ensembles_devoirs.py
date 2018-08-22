
#Écrire un programme qui renvoie l’intersection de 2 ensembles.


set1 = {1,2,3,'a',4,5}

set2 = {'a','b',12,3}

def interSet(s1,s2):
    return(s1 & s2)  # return(s1.intersection(s2)) marche aussi

print(interSet(set1,set2))


#Écrire un programme qui renvoie l’union de 2 ensembles.

def uniSet(s1,s2):
    return(s1 | s2)

print(uniSet(set1,set2))


#Écrire un programme qui renvoie le minimum et le maximum d’un ensemble.

#attention ! les fonctions max et min ne marchent pas sur un mélange d'entiers et de lettres


def MinMax(s):
    l = list(s)  # conversion de l'ensemble en liste pour avoir des indexs
    for i in range(len(l)):  # pourquoi ici ne faut-il pas mettre "len(l)-1 ?
        l[i] = str(l[i])  # conversion de tous les éléments en strings pour
                           # pouvoir les comparer selon l ordre ASCII

        # print("i",i)
        # print('l[i]', l[i])
        # print(type(l[i]))
    # print(l)

    return (min(l), max(l))


print(MinMax(set1))

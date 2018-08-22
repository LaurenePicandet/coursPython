
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


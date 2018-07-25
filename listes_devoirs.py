list_A = ['abc', 'xyz', 'aba', '1221']

#Écrire un programme qui retourne le nombre de chaîne de caractère de longueur supérieure à 2
# ET dont le premier caractère est égal au dernier. Avec la liste fournie, un tel programme retournerait 2.


def count_items(list1):
    n = 0
    for i in range(len(list_A)):  # pourquoi ici il ne faut pas mettre len(list_A)-1 ? 
        print(list_A[i])
        if  list_A[i][0] == list_A[i][-1]:
            n = n +1
    return(n)

print(count_items(list_A))
#print(list_A[3][-1])

#len(list_A[i]) > 2 and
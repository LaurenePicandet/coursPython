

# Écrire un programme permettant de concaténer 3 dictionnaires en un.

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50,6:60}



def concat_dict(dict1,dict2,dict3):
    list_keys = list(dict1.keys()) + list(dict2.keys()) + list(dict3.keys())
    list_values = list(dict1.values()) + list(dict2.values()) + list(dict3.values())
    dict_final = dict(zip(list_keys, list_values))
    return (dict_final)

print(concat_dict(dict1,dict2, dict3))





############################################################
############################################################

#Écrire un programme additionnant les valeurs de deux dictionnaires dans un nouveau dictionnaire.
#  Attention : les deux dictionnaires d’entrées peuvent être de tailles différentes...

dict1 =  {1:10, 2:20}
dict2 = {3:30, 4:40, 5:50}
#dict3 = {1:40, 2:60, 3:50}   est-ce bien ça qui est attendu ?


#fonction longue, peut certainement être simplifiée !!
#ne marche que si les valeurs sont des nombres, il faut ajouter une vérification


def add_dict(dict1, dict2):

    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())

    values1 = list(dict1.values())
    values2 = list(dict2.values())

    #définir un nouveau dictionnaire
    dict3 = {}


    #definir quel dictionnaire d'entrée est le plus long --> dict_max

    if(len(keys1) > len(keys2)):
        dict_max = dict1
        dict_min = dict2
    else:
        dict_max = dict2
        dict_min = dict1


    #le nombre de clés du nouveau dictionnaire est le meme que le nb de clés du dict d'entrée le plus long

    new_keys = []
    for i in range(len(dict_max.keys())):
        new_keys.append(i+1)
        print(i+1)

    #pour les clés communes à dict1 et dict2, les valeurs de dict3 sont les sommes des valeurs de dict1 et dict2 sur les
    #clés correspondantes


    for i in range(len(dict_min.keys())):
        dict3[i+1] = values1[i] + values2[i] #i+1 sur la clé pour avoir les clés qui commençent à 1


    for i in range(1,2):
        print(i)

    #pour les clés présentes uniquement dans le dict le plus long, les valeurs du nouveau dictionnaire sont celles du
    #dictionnaire le plus long

    nb_keys_to_add = len(dict_max) - len(dict_min)

    last_key = len(dict3)

    for i in range(last_key, last_key + nb_keys_to_add):
        print("key to add : ",i+1)  #i+1 car range fait partir de 0 et on veut que les clés partent de 1
        dict3[i+1]= list(dict_max.values())[i] #transtypage en liste pour pouvoir utiliser l'index


    #retourner le nouveau dictionnaire

    return(dict3)


print(add_dict(dict1,dict3))


#test1

dict1 =  {1:10, 2:20, 3:50, 4:12, 5:2}
dict2 = {3:30, 4:40, 5:50}
print(add_dict(dict1,dict2))    # {1: 40, 2: 60, 3: 100, 4: 12, 5: 2}  OK



#test2

dict1 =  {1:10, 8:20, 3:50, 12:12, 5:2}
dict2 = {3:30, 4:40, 5:50, 8:2, 'a':5}
print(add_dict(dict1,dict2))     #{1: 40, 2: 60, 3: 100, 4: 14, 5: 7} OK


#test3

dict1 =  {1:10, 8:20, 3:50, 12:12, 5:2}
dict2 = {3:30, 4:40, 5:50, 8:2.5, 'a':5}
print(add_dict(dict1,dict2))   #{1: 40, 2: 60, 3: 100, 4: 14.5, 5: 7} OK

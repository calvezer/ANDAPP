# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import os.path
import os

##############################
# Recup data avec Memoire_UID.csv
##############################

# Open Excel
excel = open("Memoire_UID.csv", "r")
contenu = excel.read()
excel.close()

# Supprimer titres des colonns
cut = contenu.split("Matiere")
cut.pop(0)

# Séparer chaque ligne
splitfor = cut[0]
splitfor = splitfor.split('\n')
splitfor.pop(0)
print(splitfor)


final = []
dic_uid = dict()

nbr = len(splitfor)


for x in range(1, nbr):

    Arg = splitfor[0].split(';')
    print("Arg3 =" + Arg[2])
    if(Arg[2] != ""):
        y = str(x)
        final.append(splitfor[0])
        dic_uid[Arg[1]] = Arg[2]

    splitfor.pop(0)


print(dic_uid)

##############################
# Recup data avec planning.ics
##############################

mon_fichier = open("D:\Telechargement\planning.ics", "r")
contenu = mon_fichier.read()
# print(contenu)
mon_fichier.close()

contenu = contenu.split("BEGIN")
print(contenu)
# premier event commence à l'élément 2
final_content = contenu[0]
contenu.pop(0)
final_content = final_content + contenu[0]
contenu.pop(0)

size = len(contenu)
print(size)
#size = int(size)

print(contenu)


for k in range(0, size):
    if "SUMMARY" in contenu[k]:
        print("Summary present")

        contenu[k] = contenu[k].replace("\\n", "")
        contenu[k] = contenu[k].replace("Ã©", "é")
        contenu[k] = contenu[k].replace("Ã¨", "è")
        contenu[k] = contenu[k].replace("Ã¢", "â")
        print(contenu[k])

        final_content = final_content + "BEGIN" + contenu[k]

    else:
        var = contenu[k]
        pos = var.find("UID")
        print(pos)
        UID = var[pos + 4:pos + 8]
        print(UID)
        value = dic_uid.get(UID)

        # UID not in Excel file
        if value == None:
            print("Summary not present but not in excel")

            contenu[k] = contenu[k].replace("\\n", "")
            contenu[k] = contenu[k].replace("Ã©", "é")
            contenu[k] = contenu[k].replace("Ã¨", "è")
            contenu[k] = contenu[k].replace("Ã¢", "â")
            print(contenu[k])

            final_content = final_content + "BEGIN" + contenu[k]

        # UID in Excel file
        else:

            print(value)
            pos = var.find("DESCRIPTION")
            print(pos)
            new_contenu = var[:pos - 1] + "\nSUMMARY:" + value + var[pos - 1:]

            new_contenu = new_contenu.replace("\\n", "")
            new_contenu = new_contenu.replace("Ã©", "é")
            new_contenu = new_contenu.replace("Ã¨", "è")
            new_contenu = new_contenu.replace("Ã¢", "â")

            print(new_contenu)
            final_content = final_content + "BEGIN" + new_contenu

print(final_content)


########################
# Modifier planning.ics
########################

f = open("D:\Telechargement\planning.ics", "w")
f.write(final_content)
f.close()

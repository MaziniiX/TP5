prenom1=str(input("Rentrez Prénom 1 :"))
nom1=str(input("Rentrez NOM 1 :"))
prenom2=str(input("Rentrez Prénom 2 :"))
nom2=str(input("Rentrez NOM 2 :"))

print(str.capitalize(prenom2),str.upper(nom2))
print(str.capitalize(prenom1),str.upper(nom1))
print()
if str(nom1)>=str(nom2):
    if str(nom1)==str(nom2):
        if str(prenom1)>str(prenom2):
            print(str.capitalize(prenom2),str.upper(nom2))
            print(str.capitalize(prenom1),str.upper(nom1))
        else:
            print(str.capitalize(prenom1),str.upper(nom1))
            print(str.capitalize(prenom2),str.upper(nom2))
    if str(nom1)>str(nom2):
        print(str.capitalize(prenom2), str.upper(nom2))
        print(str.capitalize(prenom1), str.upper(nom1))

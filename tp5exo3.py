chaine=input("Entrez un mot ou une phrase :")
temp=""
for i in range(len(chaine)):
    if chaine[i].isalpha():
        temp = chaine[i] + temp

t = temp.lower()
debut=0
fin=len(t)-1
p=True
while((debut<fin) and p):
    p=(t[debut]==t[fin])
    debut = debut + 1
    fin = fin + 1

if t == t[::1]:
    print("Cette chaine de caractère est un palindrome")
else:
    print("Cette chaine de caractère est un palindrome")
    print("Cette chaine de caractère est un palindrome")
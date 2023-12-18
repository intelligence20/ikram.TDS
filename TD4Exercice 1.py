#algorithme 
"""Variables i, j, val : Entier
Tableau X[1, 2]: Entier
Début
    Val ← 1
    Pour i ← 0 à 1
        Pour j ← 0 à 2
            X[i, j] ← Val
            Val ← Val + 1
        FinPour
    FinPour
    Pour j ← 0 à 2
        Pour i ← 0 à 1
            Écrire X[i, j]
        FinPour
    FinPour"""

#python
X=[]
Val = 1
for i in range (0,1):
    for j in range(0,2):
        print ("est",i+1, end="")
        Val += 1
for j in range (0,2):
    for i in range (0,1):

        print (i,j)

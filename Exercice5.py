#algorithm 
"""1)fonction v_f (n:entier)
debutfonction 
        variable a:char
            si(n='o'ou n='O')
                ecrire ("true")
            sinon
                ecrire ("false")
            return a
finfonction
ecrire ("saisier un nbre: ")
lire (a)"""

"""2)fonction multiple_9 (n:entier)
debutfonction 
        variable i,n:entier
            pour i allant de 1 a 9 faire:
                ecrire (i,"*",n,"=",i*n)
                i=i+1
            return 
finfonction
ecrire (multiple_9(8)) """

"""fonction multiple(n:entier)
debutfonction 
        variable i,n:entier
            pour i allant de 1 a 9 faire:
                ecrire (i,"*",n,"=",i*n)
                i=i+1
            return 
finfonction
ecrire("saisier un nbr:" )
ecrire (multiple(n))) """

"""1)def v_f (n):
    if (n=='o'or n=='O'):
        print("true")
    else:
        print("false")
    return 
n=input("saisie: ")
print(v_f(n))"""

"""2)def multiple_9(n):
    for i in range(1,10):
        print(i,"*",n,"=",i*n)
        i=i+1
    return 
print (multiple_9(9))"""

def multiple(n):
    for i in range(1,10):
        print(i,"*",n,"=",i*n)
        i=i+1
    return 
n=int (input("saisier: "))
print (multiple(n))
#algorithm
"""fonction somme_nbrs (n,n1,s,s1:entier)
debutfonction 
    variable i :entier
    s=0
        pour i allant de 0 a 1 faire:
            ecrire("saisie le 1er el 2eme nombre: ")
            lire(n ,n1)
            s=0
            s1=n+ n1
            s=s1+ s
        retourn s
finfonction"""

"""fonction fact (f ,n:entier)
debutfonction 
    variable i :entier
    f=1
        pour i allant de 0 a f faire:
            f=f*i
        retourn f
finfonction
ecrire ("saisier un number ")
lire(f(n))"""

"""fonction divise (n:entier)
debutfonction 
    variable i ,A,B:entier
    s=0
        pour i allant de 0 a 1 faire:
            ecrire("saisie le 1er el 2eme nombre: ")
            lire(A,B)
        si (B Mod A=0)
            ecricre("true")
        sinon 
            ecricre("false")
        retourn n
finfonction
ecricre(divise (2))"""

"""fonction QuoRest (n:entier)
debutfonction
    variable d,n1,n2,r :entier
        ecrire("saisie le 1er el 2eme nombre: ")
            lire(n2 ,n1)
            d=n1 div n2
            r=n1 Mod n2
        retourn d ,r
finfonction
ecrire(QuoRest(2))"""

"""fonction voyelle (n:entier)
debutfonction 
    variable n:entier
        si (n='a' ou n='e' ou n='i' ou n='u' ou n='o' ou n='y')
            ecrire("est un voyelle")
        sinon
            ecrire(" n'est pas un voyelle")
        retourn 
finfonction
ecrire("saisie un alphabet")
lire(n)
ecrire (voyelle (n))"""

"""fonction echange (e:entier)
debutfonction 
    variable T1,T2,g:entier
        T1['a','b','c']
        T2['d','e','f']
        g=T1
        T1=T2
        T2=g
        return T1,T2
finfonction
ecrire(echange(e))"""

"""fonction absolu (a:entier)
debut 
    variable a,val_abs:entier
        si (a<0)
            val_abs=abs(a)
        sinon
            
        return a
ecrire("saisie un nbre")
lire (a)"""


#python
"""def somme(n):
    for i in range (0,1):
        n1=int(input("saisir un nbr :"))
        N=int(input("saisir un nbr :"))
        s=0
        S=N+ n1
        s=S+ s
    return s

print(somme(2))"""

"""def fact(f):
    fact =1
    for i in range (1,f+1):
        fact*=i
    return fact

n=int(input("saisi un nbr:"))
print(fact(n))"""

"""def divise(n):
    for i in range(1,2):
        a=int(input("saisie a:"))
        b=int(input("saisie b:"))
    if (b%a==0):
        print("true")
    else:
        print("false")
    return n
print(divise(2))"""

"""def Quorest(n):
    n1=int (input("saisie a:"))
    n2=int (input("saisie a:"))
    d=n1 / n2
    r=n1 %n2
    return d,r
print(Quorest(2))"""

"""def voyelle(n):
    if (n=='a' or n=='e' or n=='i' or n=='u' or n=='o' or n=='y'):
        print("est un voyell")
    else:
        print("nesr pas  un voyell")
    return 
n=input("saisie: ")
print (voyelle (n))"""

"""def echange (e):
    l1=['a','b','c']
    l2=['d','e','f']
    g=l1
    l1=l2
    l2=g
    return l1,l2
print( echange (1 ))"""

"""def abslu(a):
    if (a<0):
        val_absl=abs(a)
        print("absolu",val_absl)
    else:
        print (a)

n=int (input("saisie: "))
print(abslu(n))"""
#algorithm max_min_range
"""variable i, max,min ,range:reel
tableau [100]:reel
debut 
max =tableau [0]
min =tableau [0]
range =1
n=0
    pour i allant 0 à 99 fair :
        ecrire("T[" ,i+1,"] =" ,end="")
        pour n à tableau[]
            si n>max
                n =max
            si n<min
                min =n 
            range =range +1

ecrire ("le nombre maximal est", max)
ecrire ("le nombre minimal est", min)
ecrire ("leur range est", range)"""

#python 
T=[]

for i in range (0,99):
    print("T[",i+1,"] = " ,end=" ")
    T.append(float(input()))
    
print ( "le nombre maximal est :" ,max(T) , "et le minimal est:" ,min(T))

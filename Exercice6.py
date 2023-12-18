#algorithm le moyenne
"""variable i,j,m,sum1,sum2:reels
T [30]:reel
debut 
sum1←0
sum2←0
    pour i allant de 1 a 30 fair :
        ecricr ("saisie la note de  1er DS", end =" " )
        lire (T[i])
        sum1←sum1+1
    pour j allant de 1 a 30 fair :
        ecricr ("saisie la note de  1er DS", end =" " )
        lire (T[j])
        sum2 ←sum2 +1 
    m=(sum1 +sum2)div 2"""

#python
l=[]
count=0
for i in range (30):
    print(" la note de 1er DS :",i+1 ,end =" ") 
    l.append(int(input()))
for j in range (30):
    print(" la note de 1er DS :",j+1 ,end =" ") 
    l.append(int(input()))
M=sum (l)/2


print ("le moyen est", M )
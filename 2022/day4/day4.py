import AoCutils
import os


lines= AoCutils.start_puzzle(day=4,dir=os.path.dirname(__file__))


counter1=0
counter2=0
for pair in lines:
    
    s1=list(map(lambda x:int(x),pair.split(",")[0].split("-")))
    sn1=set([x for x in range(s1[0],s1[1]+1)])
    s2=list(map(lambda x:int(x),pair.split(",")[1].split("-")))
    sn2=set([x for x in range(s2[0],s2[1]+1)])
    if (sn1.issubset(sn2)) or (sn2.issubset(sn1)):     
        counter1+=1
    if (len(sn1.intersection(sn2))>0):     
        counter2+=1
print(counter1)
print(counter2)

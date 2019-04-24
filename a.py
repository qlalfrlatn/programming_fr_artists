import maya.cmds as mc
import random
s = [i for i in range(0,1000)]
#random.seed(12955)


#print(s)

for rad in s:  
    random.seed(rad + 123)
    d = random.uniform(1,7)
    x = random.uniform(1,6)
    q = random.uniform(-6, 6)
    myString = "avikSphere" + str(rad) 
    mc.polySphere(name=myString, radius = 0.1)     
    mc.move(x, d, q, myString )

print(d)

allSelect = mc.ls('avikSphere*')
if len(allSelect)>0:
    mc.delete(allSelect)

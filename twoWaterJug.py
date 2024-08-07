capa=4
capb=3
def fill(a, capacity):
    return capacity
   
def empty(a):
    return 0
   
def transfer(a, b, capa, capb):
    if(a>capb-b):
        return a-(capb-b),capb
    return 0,b+a
   
juga=0
jugb=0
juga = fill(juga, capa)
print("Fill jug A : ",juga,",",jugb)

juga,jugb = transfer(juga,jugb,capa,capb)
print("Tarnsfer A to B : ",juga,",",jugb)

jugb = empty(jugb)
print("Empty B : ", juga,",",jugb)

juga,jugb = transfer(juga,jugb,capa,capb)
print("Tarnsfer A to B : ",juga,",",jugb)

juga = fill(juga, capa)
print("Fill jug A : ",juga,",",jugb)

juga,jugb = transfer(juga,jugb,capa,capb)
print("Tarnsfer A to B : ",juga,",",jugb)

jugb = empty(jugb)
print("Empty B : ", juga,",",jugb)

juga,jugb = transfer(juga,jugb,capa,capb)
print("Tarnsfer A to B : ",juga,",",jugb)

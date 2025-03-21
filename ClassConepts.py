class GiftBox:    #class creation
    height=0      #height & width are member variables
    width=0

g1=GiftBox()      #g1 object creation
g1.height=20      #value assigning
g1.width=30

print(f"g1->height={g1.height},width={g1.width}")  

g2=GiftBox()      #g2 object creation
g2.height=200
g2.width=300

print(f"g2->height={g2.height},width={g2.width}")

g3=GiftBox()     
g3=g1            #g1 store g3

g1=g2            #g1 override g2

print(f"g1->height={g1.height},width={g1.width}")
print(f"g2->height={g2.height},width={g2.width}")
print(f"g3->height={g3.height},width={g3.width}")
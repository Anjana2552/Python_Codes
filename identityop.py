class Giftbox:
    height=0
    width=0
g1=Giftbox()
g1.height=20
g1.width=30

g2=Giftbox()
g2.height=200
g2.width=300

g3=Giftbox()

g3=g1

if g1 is g3:
    print("g1 is g3 true")

g1=g2

if g1 is g2:
    print("g1 is g2 true")

if g1 is not g3:
    print("g1 is not equal to g3")
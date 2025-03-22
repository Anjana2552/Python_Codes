class GiftBox:
    height=0
    width=0

def __init__(self,height,width):
    self.height=height
    self.width=width

def assemble(self):
    print("Height is"+str(self.height))
    print("Width is"+str(self.width))

g1=GiftBox(20,30)
g1.assemble()
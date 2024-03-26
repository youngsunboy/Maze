#node类型用来储存每个拓展结点索引及其前驱结点的索引
class nodes:
    def __init__(self,pos,pre):
        self.pos=pos
        self.pre=pre
    
    def getPos(self):
        return self.pos
    
    def getPre(self):
        return self.pre


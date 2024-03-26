from numpy import numpy

#栈类型
class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.push(item)
        return True

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

#结点class
class nodes:
    def __init__(self,pos,pre):
        #结点的索引
        self.pos=pos
        #结点的前驱结点的索引
        self.pre=pre
    def getPos(self):
        return self.pos
    
    def getPre(self):
        return self.pre

#A*算法类型
class A_star:
    def __init__(self,maze):
        self.maze=maze
        #迷宫的长度,宽度
        self.MAZE_H=len(self.maze)
        self.MAZE_W=len(self.maze[1])
        #起点
        self.start=[0,0]
        #目标结点的索引
        self.tar=[self.MAZE_H-1,self.MAZE_W-1]
    
    def inspire(self):
        #代价函数
        pass

    def expandNodes(self,cur,pre):
        pass

    def search(self):
        self.cur=self.start
        self.OPEN=Stack()
        self.CLOSED=Stack()
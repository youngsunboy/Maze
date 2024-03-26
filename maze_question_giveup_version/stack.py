#列表的尾端作为栈顶的栈类

class stack():
    def __init__(self):
        self.items=[]

    def isempty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return (len(self.items))

    def all(self):
        return self.items

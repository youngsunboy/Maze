from nodes import nodes
from stack import stack

def printPath(CLOSED):
    #CLOSED是CLOSED表中所有元素

    #tar是目标位置索引

    #如果tar结点的左边结点或者上边结点在CLOSED表中则证明问题已解
    res=[]
    last=CLOSED.pop()
    pre=last.getPre()
    res.append(last)
    for i in CLOSED.reverse():
        if i.getPre()!=pre:
            continue
        else:
            pre=i.getPre()
            res.append(i)
    print("走出迷宫的路径为:")
    for i in range(len(res)):
        if i!=len(res)-1:
            print(i.getPos(),"->")
        elif i.getPre()==-1:
            break
        else:
            print(i.getPos())


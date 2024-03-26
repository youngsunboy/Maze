#使用numpy中的ndarray对象来表示迷宫
import numpy as np

#其中[0,0]元素为起点,对角元素为终点

#导入自己编写的栈类型
from stack import stack

#拓展结点函数导入
#canWiden函数接受两个参数,第一个参数是当前位置的索引,第二个参数是ndarray对象,即迷宫
from canWiden import canWiden

from printPath import printPath

from nodes import nodes

#主函数
def main(x):
    #参数x就是迷宫

    #OPEN表,CLOSED表
    OPEN=stack()
    CLOSED=stack()

    #当前结点索引
    cur=nodes([0,0],-1)

    #目标位置索引,目标结点有两种可能前驱
    tar1=nodes([np.shape(x)[0]-1,np.shape(x)[1]-1],[np.shape(x)[0]-1-1,np.shape(x)[1]-1])
    tar2=nodes([np.shape(x)[0]-1,np.shape(x)[1]-1],[np.shape(x)[0]-1,np.shape(x)[1]-1-1])
    

    #开始深度优先搜索
    #起点索引放入OPEN表
    OPEN.push(cur)

    while tar1 not in OPEN.all() and tar2 not in OPEN.all():#all()函数以列表形式返回OPEN表中所有元素
        #OPEN为空时不再遍历
        if OPEN.isempty():
            break
        
        #OPEN表第一个元素放入CLOSED表中
        cur=OPEN.pop().getPos()
        CLOSED.push(cur)

        #将可拓展结点放入OPEN表
        wideNodes=canWiden(cur,x)
        for i in wideNodes:
            OPEN.push(i)
            
    printPath(CLOSED)

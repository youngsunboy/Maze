import numpy as np
from nodes import nodes

def canWiden(cur,arr):
    #cur是一个列表,包含两个元素,第一个元素是当前位置行索引,第二个元素是列索引

    #需要返回的可拓展结点索引的列表
    res=[]
    
    #arr的行数,列数
    row=np.shape(arr)[0]
    col=np.shape(arr)[1]

    #起点也标记为-1
    arr[0,0]=-1
    
    #按照向右,向下,向左,向上的顺序拓展结点,并将可拓展结点标记为-1
    #此外还需要将可拓展结点加入列表res
    if cur[1]+1<col and arr[cur[0],cur[1]+1]==0:
        node=nodes([cur[0],cur[1]+1],cur)
        res.append(node)
        arr[cur[0],cur[1]+1]=-1
        
    if cur[0]+1<row and arr[cur[0]+1,cur[1]]==0:
        node=nodes([cur[0]+1,cur[1]],cur)
        res.append(node)
        arr[cur[0]+1,cur[1]]=-1
        
    if cur[1]-1>=0 and arr[cur[0],cur[1]-1]==0:
        node=nodes([cur[0],cur[1]-1],cur)
        res.append(node)
        arr[cur[0],cur[1]-1]=-1
        
    if cur[0]-1>=0 and arr[cur[0]-1,cur[1]]==0:
        node=nodes([cur[0]-1,cur[1]],cur)
        res.append(node)
        arr[cur[0]-1,cur[1]]=-1

    return res

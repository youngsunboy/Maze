import numpy as np
import tkinter as tk

x=np.array([[0,0,1,0],[1,0,0,0],[1,0,1,0],[1,1,0,0],[0,0,0,0]])

#全局变量
UNIT=40#每格的像素
MAZE_H=np.shape(x)[0]#迷宫的高度
MAZE_W=np.shape(x)[1]#迷宫的宽度
geometry=max(MAZE_H,MAZE_W)

class Maze(tk.Tk,object):
    def __init__(self,start,wall):
        super().__init__()#继承tk.Tk()类的初始化方法
        self.action_space=['u','d','l','r']#移动操作的集合
        self.n_actions=len(self.action_space)
        self.geometry('{0}x{1}'.format(geometry*UNIT,geometry*UNIT))#设置窗口大小
        self.title('maze')
        self.start=[(start[0]-1)*UNIT+20,(start[1]-1)*UNIT+20]#start为迷宫class接收的外部参数,表示迷宫的起点
        self.wall=wall
        self._build_maze()#初始化时调用_build_maze函数进行初始化迷宫

    def _build_maze(self):
        self.canvas=tk.Canvas(self,bg='white',height=MAZE_H*UNIT,width=MAZE_W*UNIT)#设置画布的背景,宽度与高度
        #划分网格
        for i in range(0,MAZE_W*UNIT,UNIT):
            #每隔UNIT的长度画一条竖线
            x0,y0=i,0
            x1,y1=i,MAZE_H*UNIT
            self.canvas.create_line(x0,y0,x1,y1)

        for i in range(0,MAZE_H*UNIT,UNIT):
            #每隔UNIT的高度画一条横线
            x0,y0=0,i
            x1,y1=MAZE_W*UNIT,i
            self.canvas.create_line(x0,y0,x1,y1)

        #在起点创建红色移动块
        self.red=self._set_start()

        #创建墙体
        self._build_wall()
        #显示所画所有对象
        self.canvas.pack()
    
    #def _build_single_wall(self):
    #    x=[0,2]
    #    x[0]=(x[0]+1)*20
    #    x[1]=(x[1]+1)*20
    #    self.canvas.create_rectangle(x[0]-20,x[1]-20,x[0]+20,x[1]+20,fill='black')

    def _set_start(self):
        #设置起点
        start=np.array(self.start)
        self.canvas.create_rectangle(start[0]-15,start[1]-15,start[0]+15,start[1]+15,fill='red')

    def _build_wall(self):
        self.canvas_wall=tk.Canvas(self,bg='white',height=MAZE_H*UNIT,width=MAZE_W*UNIT)#设置画布的背景,宽度与高度
        for i in range(MAZE_H):
            for j in range(MAZE_W):
                if self.wall[i,j]==1:
                    self.canvas.create_rectangle(j*UNIT,i*UNIT,(j+1)*UNIT,(i+1)*UNIT,fill='black')
        

start=list(map(int,input("请输入起点的横坐标和纵坐标:").split()))
maze=Maze(start,x)
maze.mainloop()
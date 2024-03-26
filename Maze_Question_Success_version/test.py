import tkinter as tk
maze=[
        [0,0,1,1,0],
        [1,0,0,0,1],
        [1,0,1,1,0],
        [0,0,0,0,0],
        [1,0,1,1,0]
    ]
root=tk.Tk()
canvas=tk.Canvas(root,height=len(maze)*40,width=len(maze[0])*40)

    #划分网格
for i in range(0,len(maze)*40,40):
    x0,y0=0,i
    x1,y1=len(maze[0])*40,i
    canvas.create_line(x0,y0,x1,y1)
for j in range(0,len(maze[0]*40),40):
    x0,y0=j,0
    x1,y1=j,len(maze)*40
    canvas.create_line(x0,y0,x1,y1)
canvas.pack()
canvas.mainloop()

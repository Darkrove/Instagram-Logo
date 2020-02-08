from tkinter import *


root = Tk()
mycanvas = Canvas(root,bg='white', height=600,width=800)
mycanvas.pack()
#300,300
mycanvas.create_oval(5,5,595,595,fill='black')

rec=mycanvas.create_polygon(100,150,500,150,500,450,100,450,fill='white')
mycanvas.create_polygon(100,100,200,100,100,200,fill='white',smooth=True)
mycanvas.create_polygon(400,100,500,100,500,200,fill='white',smooth=True)
mycanvas.create_polygon(400,500,500,500,500,400,fill='white',smooth=True)
mycanvas.create_polygon(100,400,100,500,200,500,fill='white',smooth=True)
mycanvas.create_polygon(150,100,450,100,450,500,150,500,fill='white')

rec=mycanvas.create_polygon(140,190,460,190,460,410,140,410,fill='black')
mycanvas.create_polygon(140,240,140,140,240,140,fill='black',smooth=True)
mycanvas.create_polygon(360,140,460,140,460,240,fill='black',smooth=True)
mycanvas.create_polygon(460,360,460,460,360,460,fill='black',smooth=True)
mycanvas.create_polygon(140,360,140,460,240,460,fill='black',smooth=True)
mycanvas.create_polygon(190,140,410,140,410,460,190,460,fill='black')

#x=300,y==300,r=110
mycanvas.create_oval(190,190,410,410,fill='white')
#x=300,y==300,r=70
mycanvas.create_oval(230,230,370,370,fill='black')
#x=420,y==180,r=30
mycanvas.create_oval(390,150,450,210,fill='white')
#x=300,y=550
mycanvas.create_text(700,300,text='INSTAGRAM',font=('AR BERKLEY',25),fill='black',width=3)
root.mainloop()
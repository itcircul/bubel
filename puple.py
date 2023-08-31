import pygame
from tkinter import *
import random
import time
import math
from tkinter import messagebox
def create_buble():
    x =600
    y=random.randint(0,500)
    r=random.randint(1,80)
    idl=c.create_oval(x-r,y-r,x+r,y+r,outline='white')
    bub_id.append(idl)
    bub_r.append(r)
    bub_speed.append(random.randint(1,3))

def move_buble():
    for i in range(len(bub_id)): 
        c.move(bub_id[i],-bub_speed[i],0)





def move_ger(event):
   
   
   if event.keysym == 'Up':
        c.move(ship,0,-5)
           
   if event.keysym == 'Down':
        c.move(ship,0,5)
           
   if event.keysym == 'Right':
        c.move(ship,5,0)
           
   if event.keysym == 'Left':
        c.move(ship,-5,0)
def coll():
    ball=0
    for bub in range(len(bub_id)-1,-1,-1):
        x1,y1=c.coords(ship)
        pos = c. coords(bub_id[bub])
        x2=(pos[0]+pos[2])/2
        y2=(pos[1]+pos[3])/2
        if math.sqrt((x2-x1)**2+(y2-y1)**2)<50+bub_r[bub]:
            ball+=1
            so = pygame.mixer.Sound('C:\\Users\\User\\Desktop\\pupel\\a.wav')
            so.set_volume(0.8)
            so.play()
            del bub_r[bub]
            del bub_speed[bub]
            c.delete(bub_id[bub])
            del bub_id[bub]
            time.sleep(0.1)
            so.stop()
    return ball
    
def show_score(score):
    c.itemconfig(score_text,text = str(score))

def show_time(time):
    c.itemconfig(time_text,text = str(time))
#переменные 
score=0
end = time.time()+30
bub_id=list()
bub_r=list()
bub_speed=list()


pygame.init()
#sound = pygame.mixer.Sound('C:\\Users\\User\\Desktop\\pupel\\sponge.wav')
#sound.set_volume(0.1)
#sound.play()


root = Tk()
root.title('ловец пузыриков')
c = Canvas(root,width=600,height=500,bg='blue')
c.pack()
img = PhotoImage(file='C:\\Users\\User\\Desktop\\pupel\\osminog.png')
ship = c.create_image(300,200,image=img)
c.create_text(50,50,text="Время",fill='white')
c.create_text(150,50,text="Счёт",fill='white')
time_text=c.create_text(50,30,text='00',fill='white')
score_text = c.create_text(150,30,text=str(score),fill='white')





c.bind_all('<Key>',move_ger)
#оснавная программа
while time.time()<end:
    if random.randint(1,50)== 1:
        create_buble()
    move_buble()
    score+=coll()
    show_time(int(end-time.time()))
    show_score(score)
    root.update()
messagebox.ERROR('geme end')
root.mainloop()
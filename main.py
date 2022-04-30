from tkinter import *
from tkvideo import tkvideo
from contact import helpline_numbers
from location import locshow
from surlist import surlist
import time

root=Tk()
root.title("SANCTURIT")
root.state('zoomed')

imglbl=Label(root)
imglbl.place(x=0, y=0, relwidth=1, relheight=1)
player = tkvideo("C:/Users/DELL/Documents/VS/HACKATHONS/SANCTURIT/backvid1.mp4", imglbl,loop = 1, size = (1920,1080))
player.play()

frame0=Frame(root,highlightbackground="#000000", highlightthickness=1.5)
frame0.place(x=760,y=150,anchor='center')

labelt = Label(frame0, font=("Boulder", 25, 'bold'), bg="#8859d9", fg="#ffffff", bd=25) 
labelt.grid(row=0, column=0)

def digital_clock(): 
        time_live = time.strftime("%I:%M:%S %p")
        labelt.config(text=time_live) 
        labelt.after(200, digital_clock)
digital_clock()

frame1=Frame(root,bg='#2E0063', relief=RAISED)
frame1.place(x=760,y=285,anchor='center')
sendbtn=Button(frame1,text="SHOW\nEMERGENCY\nSERVICES",command=locshow)
sendbtn.grid(row=0,column=0,columnspan=2,ipady=30,ipadx=50)

frame2=Frame(root,bg='#2E0063', relief=RAISED)
frame2.place(x=760,y=420,anchor='center')
sendbtn=Button(frame2,text="ITEM LIST\nFOR SURVIVAL",command=surlist)
sendbtn.grid(row=0,column=0,columnspan=2,ipady=35,ipadx=45)

frame3=Frame(root,bg='#2E0063', relief=RAISED)
frame3.place(x=760,y=750,anchor='center')
sendbtn=Button(frame3,text="DONATE",bg="red",font=("arial",15))
sendbtn.grid(row=0,column=0,columnspan=2,ipady=30,ipadx=70)

frame4=Frame(root,bg='#2E0063', relief=RAISED)
frame4.place(x=760,y=550,anchor='center')
sendbtn=Button(frame4,text="CONTACT",command=helpline_numbers)
sendbtn.grid(row=0,column=0,columnspan=2,ipady=30,ipadx=50)

root.mainloop()
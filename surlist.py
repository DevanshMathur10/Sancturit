from tkinter import *

info="""Survival Items:
⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃
•Sleeping Bag
•Matting
•Backpacks
•Toiletries
•Clothes
•Headwear"""

info2="""Goals, Tasks, and Items for Escaping Homelessness:
⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃
If you are homeless, a survival kit can help you accomplish your goals:

•Getting a regular job.
•Keeping a regular job.
•Conserving enough money to get an apartment or rent a room.

To accomplish your goals you must be:

•Clean
•Well-groomed
•Rested
•Fed

To accomplish your goals you must have:

•An address
•A phone number
•An alarm clock or watch
•A place to bathe
•A clean place to sleep, or a way to stay clean when you sleep
•Clean clothes
•Food"""

def surlist():
    root1=Toplevel()
    root1.geometry("360x640")
    root1.title("SURVIVAL")

    bg=PhotoImage(file="C:/Users/DELL/Documents/VS/HACKATHONS/SANCTURIT/backimg.png")
    imglbl=Label(root1,image=bg)
    imglbl.place(x=0, y=0, relwidth=1, relheight=1)

    frame=Frame(root1,bg='#2E0063', relief=RAISED)
    frame.place(x=180,y=90,anchor='center')

    list_display=Text(frame,height=6,width=15,font=("HelvLight",15,"bold"),bg='#35afc4',fg='#2a2f30')
    list_display.insert(INSERT,info)
    list_display.grid(row=3,column=0)
    list_display.configure(state='disabled')

    frame_1=Frame(root1,bg='#2E0063', relief=RAISED)
    frame_1.place(x=180,y=300,anchor='center')

    list_display=Text(frame_1,height=10,width=20,wrap=WORD,font=("Consolas",15),bg='#8ab7bf',fg='#2a2f30')
    list_display.insert(INSERT,info2)
    list_display.grid(row=3,column=0)
    list_display.configure(state='disabled')
    
    root1.mainloop()
#surlist()
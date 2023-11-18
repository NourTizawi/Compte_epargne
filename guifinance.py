from tkinter import *

import calendar

from tkinter import filedialog
from tkinter.filedialog import asksaveasfile


info=calendar.calendar(2023)

def help():
    h="ce programme permet de réaliser des calculs financières simples,il s'agit d'un mini projet pour le modul *Introduction aux Systèmes Financiers & Bancaires* au cours de l' année universitaire 2022-2023"
    hel=Tk()
    hel.title("informations")
    label=Label(hel,text=h)
    label.pack()
    hel.pack()




def browseFiles(label_file_explorer=None):
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))


    label_file_explorer.configure(text="File Opened: " + filename)


def save():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)







def tauxeffectifglobal():

    wind=Tk()
    wind.iconbitmap("Business-Finance-logo-design-premium-vector-PNG (1).ico")
    wind.title("taux effectif global")
    wind.config(background="#FFFBEB")
    line1=Label(wind,text="quel est le taux d interet",font=40)
    line1.grid(row=0,column=0)
    e1=Entry(wind)
    e1.grid(row=0,column=1)

    line2 = Label(wind,text="quel est le nombre de jours", font=40)
    line2.grid(row=2, column=0)
    e2 = Entry(wind)
    e2.grid(row=2, column=1)

    def gety():
        i=DoubleVar(value=e1.get())
        n=DoubleVar(value=e2.get())
        teg = i/(1-i*n/360)
        answer=Label(wind,textvariable=teg).grid(row=5,column=0)



    p=Button(wind,text="ok",font=40,command=gety)
    p.grid(row=3,column=1)
    wind.pack()










def tauxmoyen():
    print("de combien de capital s'agit il\n")
    nombre=int(input())
    d=0
    num=0
    for i in range(nombre):
        print("saisissez le capital",i+1)
        c=int(input())
        print("entrez le nombre de jours pour le capital",i+1)
        n=int(input())
        print("entrez le taux d'interet pour le capital",i+1)
        i=int(input())
        num+=c*n*i
        d+=c*n

    t=num/d
    print("le taux moyen de placament de capitaux est ",t)





window=Tk()
window.title("Intérêts simples,compte d'epargne")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("Business-Finance-logo-design-premium-vector-PNG (1).ico")
window.config(background='#E8C4C4')
menubar=Menu(window)
file_menu=Menu(menubar,tearoff=0)
file_menu.add_command(label='nouveau')
file_menu.add_command(label='ouvrir',command=browseFiles)
file_menu.add_command(label='enregistrer',command=save)
file_menu.add_command(label='enregistrer sous',command=save)
file_menu.add_separator()
file_menu.add_command(label='quitter', command=window.quit)
menubar.add_cascade(label='fichier', menu=file_menu)
aide_menu=Menu(menubar,tearoff=0)
aide_menu.add_command(label='informations',command=help)
menubar.add_cascade(label='aide', menu=aide_menu)
window.config(menu=menubar)




window.grid_columnconfigure(0, weight = 1)
window.grid_columnconfigure(1, weight = 1)
window.grid_rowconfigure(0, weight = 1)

mainframe = Frame(window, bg = "#495579")
mainframe.grid(row = 0, column = 0, sticky = "nesw")
cal = Frame(window, bg = "#263159")
cal.grid(row = 0, column = 1, sticky = "nesw")



b1=Button(mainframe,text='nouveau',bg='#FFFBEB',activeforeground='#5584AC')
b1.place(x=200,y=200)


b2=Button(mainframe,text='calculer un taux moyen de placement de capitaux',bg="#FFFBEB",command=tauxmoyen)
b2.place(x=120,y=300)


b3=Button(mainframe,text='calculer un taux effectif global',bg="#FFFBEB",command=tauxeffectifglobal)
b3.place(x=150,y=400)


calen=Label(cal,text=info,font='consolas 10 bold')
calen.pack()






window.mainloop()

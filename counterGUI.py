from tkinter import *
import counter

class GUI:
    def __init__(self):
        self.card=counter.cardSet()
        self.root=Tk()
        self.root.title('CardCounter')
        self.paths=[]
        self.last=None # me/prev/next
        self.reset()
        self.cmd=StringVar()
        Entry(self.root,textvariable=self.cmd).grid(row=2,columnspan=13)
        Button(self.root,text='reset',command=self.reset).grid(row=2,column=13)
        self.root.bind("<Shift-Return>",self.shiftEnter)
        self.root.bind("<Control-Return>",self.ctrlEnter)
        self.root.bind("<Alt-Return>",self.altEnter)
        self.root.bind("<Control-z>",self.cancel)
        self.root.mainloop()
    def shiftEnter(self,e):
        if self.card.run(self.cmd.get())=='set':
            for i in range(len(self.card.kind)):
                if self.card.kind[i]==self.card.laizi:
                    Label(self.root,text=self.card.kind[i],width=5,bg='gray').grid(row=0,column=i)
        self.pathContent('me')
        self.cmd.set('')
        self.refreshNum()
    def ctrlEnter(self,e):
        self.card.run(self.cmd.get())
        self.pathContent('prev')
        self.cmd.set('')
        self.refreshNum()
    def altEnter(self,e):
        self.card.run(self.cmd.get())
        self.pathContent('next')
        self.cmd.set('')
        self.refreshNum()
    def pathContent(self,player):
        clmn=-1
        if player=='me':clmn=1
        if player=='prev':clmn=0
        if player=='next':clmn=2
        if self.last==player:
            self.paths.append(Frame(self.root,width=750,height=500))
            self.paths[-1].grid(column=3,columnspan=9)
            Label(self.paths[-1],height=0,width=15,bg='gray').grid(row=0,column=0)
            Label(self.paths[-1],height=0,width=15,bg='gray',text='new turn').grid(row=0,column=1)#布局调整
            Label(self.paths[-1],height=0,width=15,bg='gray').grid(row=0,column=2)
        txt=self.card.scaner(self.cmd.get())
        Label(self.paths[-1],text=txt,width=15,bg='white').grid(column=clmn)
        self.last=player
    def reset(self):
        self.card.reset()
        for item in self.paths:
            item.grid_forget()
        self.paths=[]
        self.last=None
        fm=Frame(self.root,width=750)
        self.paths.append(fm)
        Label(self.paths[-1],height=0,width=15,bg='gray').grid(row=0,column=0)
        Label(self.paths[-1],height=0,width=15,bg='gray',text='new game').grid(row=0,column=1)#布局调整
        Label(self.paths[-1],height=0,width=15,bg='gray').grid(row=0,column=2)
        fm.grid(row=3,column=3,columnspan=9)
        self.numlist=[]
        for i in range(len(self.card.kind)):
            Label(self.root,text=self.card.kind[i],width=5).grid(row=0,column=i)
            sv=IntVar()
            self.numlist.append(sv)
            self.numlist[-1].set(self.card.card[self.card.kind[i]])
            Label(self.root,textvariable=self.numlist[-1]).grid(row=1,column=i)
    def cancel(self,e):
        print("cancel")
        self.card.cancel()
        self.refreshNum()
    def refreshNum(self):
        for i in range(len(self.card.kind)):
            self.numlist[i].set(self.card.card[self.card.kind[i]])
    

g=GUI()

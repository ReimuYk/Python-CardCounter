from tkinter import *
import counter

class GUI:
    def __init__(self):
        self.card=counter.cardSet()
        self.root=Tk()
        self.root.title('CardCounter')
        self.reset()
        self.cmd=StringVar()
        Entry(self.root,textvariable=self.cmd).grid(row=2,columnspan=13)
        Button(self.root,text='reset',command=self.reset).grid(row=2,column=13)
        self.root.bind("<Return>",self.enterPress)
        self.root.bind("<Control-z>",self.cancel)
        self.root.mainloop()
    def enterPress(self,e):
        if self.card.run(self.cmd.get())[:5]=='laizi':
            for i in range(len(self.card.kind)):
                if self.card.kind[i]==self.card.laizi:
                    Label(self.root,text=self.card.kind[i],width=5,bg='gray').grid(row=0,column=i)
        self.cmd.set('')
        self.refreshNum()
    def reset(self):
        self.card.reset()
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

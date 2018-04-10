import string

class cardSet:
    def __init__(self):
        self.kind=['jo1','jo0','2','a','k','q','j','10','9','8','7','6','5','4','3']
        self.card={}
        self.commandlist=[]
        self.reset()
    def reset(self):
        for item in self.kind:
            self.card[item]=4
        self.card['jo1']=1
        self.card['jo0']=1
    def cancel(self):
        self.reset()
        self.commandlist=self.commandlist[:-1]
        for item in self.commandlist:
            self.run(item)
    def dec(self,cd):
        self.card[cd]-=1
    def parse(self,line):
        left=line
        res=[]
        while left!='':
            for item in self.kind:
                if left[:len(item)]==item:
                    res.append(item)
                    left=left[len(item):]
                    continue
        return res
    def run(self,command):
        ## x,y stand card, 0 stands 10
        # l.x-y means xx-yy连对
        # s.x-y means x-y顺子
        # x means x单牌
        # xx means xx对子
        # xxx means xxx三个
        # xxxy means xxxy
        # xxxyy means xxxyy
        # b.x means xxxx
        # f.x-y.a b c d e f g means xxx-yyy&abcdefg
        # +x means 前一手牌用癞子当x
        self.commandlist.append(command)
        if command[0]=='l':
            left=command[1:]
            if left[0]=='.':
                left=left[1:]
            left=left.split('-')
            flag=False
            for item in self.kind:
                if item==left[1]:
                    flag=True
                if flag:
                    self.dec(item)
                    self.dec(item)
                if item==left[0]:
                    self.prt()
                    return
        if command[0]=='s':
            left=command[1:]
            if left[0]=='.':
                left=left[1:]
            left=left.split('-')
            flag=False
            for item in self.kind:
                if item==left[1]:
                    flag=True
                if flag:
                    self.dec(item)
                if item==left[0]:
                    return
        if command[0]=='b':
            left=command[1:]
            if left[0]=='.':
                left=left[1:]
            for i in range(4):
                self.dec(left)
            self.prt()
            return
        if command[0]=='f':
            left=command[1:]
            if left[0]=='.':
                left=left[1:]
            left=left.split('.')
            for item in left[1].split():
                self.dec(item)
            flag=False
            left=left[0].split('-')
            for item in self.kind:
                if item==left[1]:
                    flag=True
                if flag:
                    for i in range(3):
                        self.dec(item)
                if item==left[0]:
                    self.prt()
                    return
        if command[0]=='+':
            left=command[1:]
            self.prt()
            return
        left=self.parse(command)
        for item in left:
            self.dec(item)
        self.prt()
    def prt(self):
        line1=[]
        line2=[]
        for item in self.kind:
            line1.append(item)
            line2.append(self.card[item])
        for item in line1:
            print(item,end='\t')
        print()
        for item in line2:
            print(item,end='\t')
        
##
##s = cardSet()
##while True:
##    ss = input('command:')
##    s.run(ss)
        

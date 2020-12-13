import tkinter as tk
import random
import time

class Test():
    def __init__(self,root):
        self.r = root
        self.r.geometry('1000x650')
        self.right_answer = 0
        self.drawWidgets()
    
    def drawWidgets(self):
        self.Label = tk.Label(self.r,text='Καλώς ορίσατε στο\nSTROOP TESTER',font='arial 50 bold',bg = 'black',fg = 'white')
        self.Label.pack(side = 'top')
        self.button = tk.Button(self.r,text='συνέχεια',font='arial 20 bold',command=self.start_test)
        self.button.pack(side = 'bottom')

    def start_test(self):
        self.t = 0
        self.Label.destroy()
        self.button.destroy()
        self.next_test()

    def answer1(self):
        self.answer =  1
        self.check_answer()
    def answer2(self):
        self.answer = 2
        self.check_answer()
    def answer3(self):
        self.answer = 3
        self.check_answer()
    def answer4(self):
        self.answer = 4
        self.check_answer()

    def check_answer(self):
        if self.answer == self.right_answer:
            self.end_timer = time.time()
            self.time_list()
            self.t +=1
            self.next_test()
        else:
            pass

    def next_test(self):
        allcolors = [('grey','γκρι'),('#ffda03','κίτρινο'),('green','πράσινο'),('blue','μπλε'),('purple','μωβ'),('red','κόκκινο'),('darkorange','πορτοκαλί')]
        if self.t==0:
            self.window = tk.Label(self.r)
            self.window.grid(row = 0,pady = 100,padx = 50)
            self.button1 = tk.Button(self.r,command = self.answer1,height = 5, width = 50)
            self.button1.grid(row = 1,column = 0,pady = 50,padx = 50)
            self.button2 = tk.Button(self.r,command = self.answer2,height = 5, width = 50)
            self.button2.grid(row = 1,column = 1,pady = 50,padx = 50)
            self.button3 = tk.Button(self.r,command = self.answer3,height = 5, width = 50)
            self.button3.grid(row = 2,column = 0,pady= 50,padx = 50)
            self.button4 = tk.Button(self.r,command = self.answer4,height = 5, width = 50)
            self.button4.grid(row = 2,column = 1,pady = 50,padx = 50)
        if self.t>=0 and self.t < 21:
            self.start_timer = time.time()
            random.shuffle(allcolors)
            self.rc1 = allcolors[0]
            self.rc2 = allcolors[1]
            self.rc3 = allcolors[2]
            self.rc4 = allcolors[3]
            questioncolor = [(self.rc1,1),(self.rc2,2),(self.rc3,3),(self.rc4,4)]  
            if self.t < 11:
                qcolor = random.choice(questioncolor)
                t = self.t
                self.window.configure(text = qcolor[0][1], fg = qcolor[0][0], font = 'arial 50 bold')
                self.button1.configure(bg = self.rc1[0])
                self.button2.configure(bg = self.rc2[0])
                self.button3.configure(bg = self.rc3[0])
                self.button4.configure(bg = self.rc4[0])
                self.right_answer = qcolor[1]
            elif self.t>=11 and self.t < 21:
                random.shuffle(questioncolor)
                qcolor = questioncolor[0]
                qcolor_color = questioncolor[1]
                t = self.t
                self.window.configure(text = qcolor[0][1], fg = qcolor_color[0][0], font = 'arial 50 bold')
                self.button1.configure(bg = self.rc1[0])
                self.button2.configure(bg = self.rc2[0])
                self.button3.configure(bg = self.rc3[0])
                self.button4.configure(bg = self.rc4[0])
                self.right_answer = qcolor[1]

    def time_list(self):
        no_stroop = []
        yes_stroop = []
        if self.t >= 0 and self.t < 11:
            no_stroop.append(self.end_timer - self.start_timer)
        elif  self.t >= 11 and self.t < 21:
            yes_stroop.append(self.end_timer - self.start_timer)
            
        if self.t == 20 :
            print(no_stroop ,yes_stroop)




root = tk.Tk()
myapp = Test(root)
root.mainloop()
        

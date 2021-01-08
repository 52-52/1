import tkinter as tk
import random
import time
from tkinter import *
from tkinter import ttk

class Test():
    def __init__(self,root):
        self.r = root
        self.r.geometry('1000x650')
       # self.r.resizable(False,False)
        self.right_answer = 0   
        self.drawWidgets()
        self.no_stroop = []
        self.yes_stroop = []
        self.st = []
    
    def drawWidgets(self):
        self.Label = tk.Label(self.r,text='Καλώς ορίσατε στο\nSTROOP TESTER',font='arial 50 bold')
        self.Label.pack(side = 'top')
        self.button = tk.Button(self.r,text='Συνέχεια',font='arial 20 bold',command=self.start_test)
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
            self.prog ["value"] += 5
            self.time_list()
            self.t +=1
            self.next_test()
        else:
            pass
        
    def button_hover1(self,e):
        self.button1["bd"] = "5"

        
    def button_hover2(self,e):
        self.button2["bd"] = "5"

    def button_hover3(self,e):
        self.button3["bd"] = "5"

    def button_hover4(self,e):
        self.button4["bd"] = "5"

    def button_hover_leave1(self,e):
        self.button1["bd"] = "15"

    def button_hover_leave2(self,e):
        self.button2["bd"] = "15"

    def button_hover_leave3(self,e):
        self.button3["bd"] = "15"

    def button_hover_leave4(self,e):
        self.button4["bd"] = "15"

        
    

    def next_test(self):
        allcolors = [('grey','ΓΚΡΙ'),('#ffda03','ΚΙΤΡΙΝΟ'),('green','ΠΡΑΣΙΝΟ'),('blue','ΜΠΛΕ'),('purple','ΜΩΒ'),('red','ΚΟΚΚΙΝΟ'),('darkorange','ΠΟΡΤΟΚΑΛΙ')]
        if self.t == 0:
            self.window = tk.Label(self.r)
            self.window.grid(row = 0,pady = 50,padx = 50)
            
            self.prog = ttk.Progressbar(self.r,orient = "vertical", length = 300, mode = 'determinate')
            self.prog.grid(column = 4)
            
            
            self.button1 = tk.Button(self.r,command = self.answer1  , height = 5, width = 50, bd = 15)
            self.button1.grid(row = 1,column = 0,pady = 50,padx = 50)
            self.button2 = tk.Button(self.r,command = self.answer2 ,height = 5, width = 50, bd = 15)
            self.button2.grid(row = 1,column = 3,pady = 50,padx = 50)
            self.button3 = tk.Button(self.r,command = self.answer3 ,height = 5, width = 50,  bd = 15)
            self.button3.grid(row = 2,column = 0,pady= 50,padx = 50)
            self.button4 = tk.Button(self.r,command = self.answer4 ,height = 5, width = 50, bd = 15)
            self.button4.grid(row = 2,column = 3,pady = 50,padx = 50)

            self.button1.bind("<Enter>", self.button_hover1)
            self.button1.bind("<Leave>", self.button_hover_leave1)
            self.button2.bind("<Enter>", self.button_hover2)
            self.button2.bind("<Leave>", self.button_hover_leave2)
            self.button3.bind("<Enter>", self.button_hover3)
            self.button3.bind("<Leave>", self.button_hover_leave3)
            self.button4.bind("<Enter>", self.button_hover4)
            self.button4.bind("<Leave>", self.button_hover_leave4)

        if self.t>=0 and self.t < 20:
            self.start_timer = time.time()
            random.shuffle(allcolors)
            self.rc1 = allcolors[0]
            self.rc2 = allcolors[1]
            self.rc3 = allcolors[2]
            self.rc4 = allcolors[3]
            questioncolor = [(self.rc1,1),(self.rc2,2),(self.rc3,3),(self.rc4,4)]
        
            if self.t < 10 :
                qcolor = random.choice(questioncolor)
                t = self.t
                self.window.configure(text = qcolor[0][1], fg = qcolor[0][0], font = 'arial 50 bold')
                self.button1.configure(bg = self.rc1[0])
                self.button2.configure(bg = self.rc2[0])
                self.button3.configure(bg = self.rc3[0])
                self.button4.configure(bg = self.rc4[0])
                self.right_answer = qcolor[1]

                        
            elif self.t>=10 and self.t < 20:
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
        a = self.end_timer - self.start_timer
        if self.t >= 0 and self.t < 10:
            self.no_stroop.append(self.end_timer - self.start_timer)
        elif  self.t >= 10 and self.t < 20:
            self.yes_stroop.append(self.end_timer - self.start_timer)      
        if self.t == 19 :
            self.no_stroop_average = sum(self.no_stroop)/10
            self.yes_stroop_average = sum(self.yes_stroop)/10
            stroop_difference = (self.yes_stroop_average - self.no_stroop_average)/self.no_stroop_average
            print(self.no_stroop ,self.yes_stroop)
            print(self.no_stroop_average,self.yes_stroop_average)
            self.st = [('Προσπάθεια','Χωρίς stroop','Με stroop'), 
                       (1,self.no_stroop[0],self.yes_stroop[0]), 
                       (2,self.no_stroop[1],self.yes_stroop[1]),
                       (3,self.no_stroop[2],self.yes_stroop[2]), 
                       (4,self.no_stroop[3],self.yes_stroop[3]),
                       (5,self.no_stroop[4],self.yes_stroop[4]),
                       (6,self.no_stroop[5],self.yes_stroop[5]),
                       (7,self.no_stroop[6],self.yes_stroop[6]),
                       (8,self.no_stroop[7],self.yes_stroop[7]),
                       (9,self.no_stroop[8],self.yes_stroop[8]),
                       (10,self.no_stroop[9],self.yes_stroop[9]),
                       ('Μέσος όρος',self.no_stroop_average,self.yes_stroop_average)]
            self.total_rows = len(self.st) 
            self.total_columns = len(self.st[0])
            self.time_table(root)
    
    def time_table(self,root):
        root = Tk()
        for i in range(self.total_rows): 
            for j in range(self.total_columns): 
                self.e = Entry(root, width=20, fg='blue',font=('Arial',16,'bold'))  
                self.e.grid(row=i, column=j) 
                self.e.insert(END, self.st[i][j])
        root.mainloop()       

root = tk.Tk()
myapp = Test(root)
root.mainloop()

import tkinter as tk

class Test():
    def __init__(self,root):
        self.r = root
        self.t = 0
        self.right_answer = 2
        self.drawWidgets()

    def drawWidgets(self):
        self.Label = tk.Label(self.r,text='καλωσηρθατε στο\nSTROOP TESTER',font='arial 30 bold')
        self.Label.pack(side = 'top')
        self.button = tk.Button(self.r,text='συνεχεια',font='arial 20 bold',command=self.start_test)
        self.button.pack(side = 'bottom')

    def start_test(self):
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
            self.t +=1
            self.next_test()
        else:
            pass

    def next_test(self):
        question_list = [(),('κιτρινο','red','red','purple','blue','orange',1)]
        if self.t==0:
            self.window = tk.Label(self.r, text='πορτοκαλι',fg='green',font='arial 30 bold')
            self.window.pack(side = 'top')
            self.button1 = tk.Button(self.r,text='    ', bg='blue',command = self.answer1)
            self.button1.pack(expand=1)
            self.button2 = tk.Button(self.r,text='    ', bg='green',command = self.answer2)
            self.button2.pack(expand=1)
            self.button3 = tk.Button(self.r,text='     ',bg='purple',command = self.answer3)
            self.button3.pack(expand=1)
            self.button4 = tk.Button(self.r,text='     ',bg='yellow',command = self.answer4)
            self.button4.pack(expand=1)
        elif self.t>0:
            t = self.t
            self.window.configure(text=question_list[t][0], fg=question_list[t][1])
            self.button1.configure(bg = question_list[t][2])
            self.button2.configure(bg = question_list[t][3])
            self.button2.configure(bg = question_list[t][4])
            self.button2.configure(bg = question_list[t][5])
            self.right_answer = question_list[t][6]

root = tk.Tk()
myapp = Test(root)
root.mainloop()
        


        

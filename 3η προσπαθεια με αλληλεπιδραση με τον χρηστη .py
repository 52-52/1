import tkinter as tk
from tkinter import ttk
import random
import time
import csv
from tkinter import *

class Test():
    def __init__(self,root):
        self.r = root
        self.r.geometry('1000x650')
        self.right_answer = 0
        self.drawWidgets()
        self.no_stroop = []
        self.yes_stroop = []
        self.st = [('Προσπάθεια','Χωρίς stroop','Με stroop')]
        self.no_stroop_number = 10
        self.yes_stroop_number = 10
        self.all_tries = 'apires'
        self.current_tries = 1
        self.timer = 'no'


    
    def drawWidgets(self):
        self.Label = tk.Label(self.r,text='\n\n\nΚαλώς ορίσατε στο\nSTROOP TESTER',font='arial 50 bold')
        self.Label.pack(side = 'top')
        self.button = tk.Button(self.r,text='συνέχεια',font='arial 20 bold',command=self.choose_test)
        self.button.pack(side = 'bottom')



    def choose_test(self):

        self.Label.destroy()
        self.button.destroy()
        self.Instructions = tk.Label(self.r,text = 'Σε αυτό το τεστ θα εμφανίζονται στην οθόνη σου κάποιες λέξεις (ονόματα χρωμάτων) καθώς και κάποιες επιλογές χρωμάτων  \nαπό κάτω και εσύ πρέπει να διαλέξεις την επιλογή που αντιστοιχεί στο  χρώμα που είναι γραμμένη η λέξη  .\nΟ προεπιλεγμένος αριθμός ερωτημάτων ειναι: 10 ερωτήσεις χώρις το φαίνομενο stroop και 10 με το φαινόμενο.\n Ο χρήστης μπορει να κάνει όσες προσπάθειες θέλει στο κάθε ερώτημα και δεν έχει τεθεί χρονόμετρο.\nΑν θέλεις να αλλάξεις κάποια απο τις παραμέτρους αυτές, μπορείς να το κάνεις από κάτω. : ',font='arial 10 bold')
        self.Instructions.grid(padx = 0,pady = 2)
        self.label_stroop = tk.Label(self.r,font = 'arial 10',text = 'Πόσες ερωτήσεις θέλεις να έχει το τεστ χωρίς το φαινόμενο stroop; [πάτα Enter για τέλος]:..............................\n\nΠόσες ερωτήσεις θέλεις να έχει το τεστ με το φαινόμενο stroop; [πάτα Enter για τέλος]:..................................\n\nΠόσες προσπάθειες θέλεις να έχει η κάθε ερώτηση; [πάτα Enter για τέλος]:............................................. \n\nΘέλεις οι απαντησεις σου να έχουν όριο χρόνου; :....................................................................................')
        self.label_stroop.grid(row = 1, rowspan = 4, column = 0)
        self.question_no_stroop = tk.Entry(self.r)
        self.question_no_stroop.bind('<Return>',self.get_no_stroop_number)
        self.question_no_stroop.grid(row = 1, column = 1)
        self.question_yes_stroop = tk.Entry(self.r)
        self.question_yes_stroop.bind('<Return>',self.get_yes_stroop_number)
        self.question_yes_stroop.grid(row = 2, column = 1)
        self.tries = tk.Entry(self.r,)
        self.tries.bind('<Return>',self.try_number)
        self.no_tries = tk.Button(self.r,text = 'Άπειρες Προσπάθειες',command = self.apires)
        self.tries.grid(row = 3 , column = 1)
        self.no_tries.grid(row = 3 , column = 3)
        self.yes_timer = tk.Button(self.r, text = 'ΝΑΙ',font = 'arial 10 bold',command = self.yes_timer)
        self.yes_timer.grid(row = 4, column = 1)
        self.no_timer = tk.Button(self.r, text = 'ΟΧΙ',font = 'arial 10 bold',command = self.no_timer)
        self.no_timer.grid(row = 4, column = 3)
        self.timer_choices = tk.Label(self.r, text = '   Γράψε εδώ πόσα δευτερόλεπτα θέλεις να περιμένει το χρονόμετρο: [πάτα Enter για τέλος]:.....................', fg = 'lightgrey',font = 'arial 10')
        self.timer_choices.grid( row = 7, column = 0)
        self.end = tk.Button(self.r,text = 'Πάτα εδώ αν τελείωσες',font = 'arial 30 bold', command = self.start_test)
        self.end.grid(row = 8,columnspan = 2)
    def get_no_stroop_number(self,event):
        self.no_stroop_number = int(self.question_no_stroop.get())
    def get_yes_stroop_number(self,event):
        self.yes_stroop_number = int(self.question_yes_stroop.get())
    def try_number(self,event):
        try:
            self.tries_left = int(self.tries.get())
            self.all_tries  = self.tries_left
        except: pass
    def apires(self):
        self.all_tries = 'apires'
    def yes_timer(self):
        try:
            self.timer_choice_input.destroy()
        except: pass
        self.timer_choices.configure(fg = 'black')
        self.timer_choice_input = tk.Entry(self.r)
        self.timer_choice_input.bind('<Return>',self.timer_input)
        self.timer_choice_input.grid(row = 7, column = 1)
    def no_timer(self):
        self.timer_choices.configure(fg = 'grey')
        try:
            self.timer_choice_input.destroy()
        except: pass
        self.timer = 'no'
    def timer_input(self,event):
        if self.timer_choice_input.get().isnumeric:
            try:
                self.timer = int(self.timer_choice_input.get())
                self.timer_left = self.timer
            except:pass
        
                
    def start_test(self):
        self.t = 0
        self.Instructions.destroy()
        self.label_stroop.destroy()
        self.question_no_stroop.destroy()
        self.question_yes_stroop.destroy()
        self.tries.destroy()
        self.no_tries.destroy()
        self.yes_timer.destroy()
        self.no_timer.destroy()
        self.timer_choices.destroy()
        try:
            self.timer_choice_input.destroy()
        except: pass
        self.end.destroy()
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
            self.prog ["value"] += 100 / (self.no_stroop_number + self.yes_stroop_number)
            self.time_list()
            self.t +=1
            self.current_tries = 1
            if self.all_tries != 'apires':
                self.tries_left = self.all_tries
                self.tries.configure(text = 'προσπάθεια:{}/{}'.format(self.current_tries,self.all_tries))
            self.next_test()
        else:
            if self.all_tries != 'apires' :
                self.tries_left -= 1
                print(self.tries_left)
                if self.tries_left <= 0:
                    if self.t < self.no_stroop_number :
                        self.no_stroop.append('Λάθος')
                    else:
                        self.yes_stroop.append('Λάθος')
                        if self.t == self.no_stroop_number + self.yes_stroop_number - 1:
                            self.end_test()
                    self.t += 1
                    self.prog ["value"] += 100 / (self.no_stroop_number + self.yes_stroop_number)
                    self.next_test()
                else :
                    self.current_tries += 1
                    self.tries.configure(text = 'προσπάθεια:{}/{}'.format(self.current_tries,self.all_tries))
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
        try:self.timer_left = self.timer
        except:pass
        try:
            self.current_tries = 1
            self.tries_left = self.all_tries
            self.tries.configure(text = 'προσπάθεια:{}/{}'.format(self.current_tries,self.all_tries))
        except:pass
        allcolors = [('grey','γκρι'),('#ffda03','κίτρινο'),('green','πράσινο'),('blue','μπλε'),('purple','μωβ'),('red','κόκκινο'),('darkorange','πορτοκαλί')]
        if self.t==0:
            self.prog = ttk.Progressbar(self.r,orient = "vertical", length = 300, mode = 'determinate')
            self.prog.grid(column = 4,rowspan = 3)
            
            self.window = tk.Label(self.r)
            self.window.grid(row = 0,column = 0,pady = 90,padx = 50)
            self.button1 = tk.Button(self.r,command = self.answer1,height = 5, width = 50, bd = 15)
            self.button1.grid(row = 1,column = 0,pady = 50,padx = 50)
            self.button2 = tk.Button(self.r,command = self.answer2,height = 5, width = 50, bd = 15)
            self.button2.grid(row = 1,column = 1,pady = 50,padx = 50,columnspan = 2)
            self.button3 = tk.Button(self.r,command = self.answer3,height = 5, width = 50, bd = 15)
            self.button3.grid(row = 2,column = 0,pady= 50,padx = 50)
            self.button4 = tk.Button(self.r,command = self.answer4,height = 5, width = 50, bd = 15)
            self.button4.grid(row = 2,column = 1,pady = 50,padx = 50, columnspan = 2)
            if self.all_tries != 'apires':
                self.tries = tk.Label(self.r, text = ('προσπάθεια:{}/{}'.format(self.current_tries,self.all_tries)))
                self.tries.grid(row = 0, column = 1, pady = 10, padx = 10)
            self.show_timer = tk.Label(self.r, text = 'χρονόμετρο: {}'.format('--'))
            self.show_timer.grid(row = 0,column = 2, pady = 10, padx = 20)

            self.button1.bind("<Enter>", self.button_hover1)
            self.button1.bind("<Leave>", self.button_hover_leave1)
            self.button2.bind("<Enter>", self.button_hover2)
            self.button2.bind("<Leave>", self.button_hover_leave2)
            self.button3.bind("<Enter>", self.button_hover3)
            self.button3.bind("<Leave>", self.button_hover_leave3)
            self.button4.bind("<Enter>", self.button_hover4)
            self.button4.bind("<Leave>", self.button_hover_leave4)
        if self.t>= 0 and self.t < (self.no_stroop_number + self.yes_stroop_number):
            self.start_timer = time.time()
            random.shuffle(allcolors)
            self.rc1 = allcolors[0]
            self.rc2 = allcolors[1]
            self.rc3 = allcolors[2]
            self.rc4 = allcolors[3]
            questioncolor = [(self.rc1,1),(self.rc2,2),(self.rc3,3),(self.rc4,4)]  
            if self.t < self.no_stroop_number :
                qcolor = random.choice(questioncolor)
                t = self.t
                self.window.configure(text = qcolor[0][1], fg = qcolor[0][0], font = 'arial 50 bold')
                self.button1.configure(bg = self.rc1[0])
                self.button2.configure(bg = self.rc2[0])
                self.button3.configure(bg = self.rc3[0])
                self.button4.configure(bg = self.rc4[0])
                self.right_answer = qcolor[1]
            elif self.t>= self.no_stroop_number and self.t < self.no_stroop_number + self.yes_stroop_number:
                random.shuffle(questioncolor)
                qcolor = questioncolor[0]
                qcolor_color = questioncolor[1]
                t = self.t
                self.window.configure(text = qcolor[0][1], fg = qcolor_color[0][0], font = 'arial 50 bold')
                self.button1.configure(bg = self.rc1[0])
                self.button2.configure(bg = self.rc2[0])
                self.button3.configure(bg = self.rc3[0])
                self.button4.configure(bg = self.rc4[0])
                self.right_answer = qcolor_color[1]
            if self.timer != 'no':
                while self.timer_left:
                    minutes , seconds = divmod(self.timer_left,60)
                    time_left = 'χρονότερο: {:02d}:{:02d}'.format(minutes,seconds)
                    self.show_timer.configure(text = time_left)
                    self.r.update()
                    time.sleep(1)
                    self.timer_left -= 1
                if self.timer_left == 0:
                    self.timer_left = self.timer
                    if self.t < self.no_stroop_number:
                        self.no_stroop.append('Εκτός Χρόνου')
                    else:
                        self.yes_stroop.append('Εκτός Χρόνου')
                        if self.t == self.no_stroop_number + self.yes_stroop_number - 1:
                            self.end_test()
                    self.t += 1
                    self.prog ["value"] += 100 / (self.no_stroop_number + self.yes_stroop_number)
                    self.next_test()

    def time_list(self):
        a = self.end_timer - self.start_timer
        if self.t >= 0 and self.t < self.no_stroop_number:
            self.no_stroop.append(self.end_timer - self.start_timer)
        elif  self.t >= self.no_stroop_number and self.t < self.no_stroop_number + self.yes_stroop_number:
            self.yes_stroop.append(self.end_timer - self.start_timer)      
        if self.t == self.no_stroop_number + self.yes_stroop_number - 1 :
            self.end_test()
    def end_test(self):
        self.prog.destroy()
        self.window.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.show_timer.destroy()
        try:self.tries.destroy()
        except:pass
        if self.no_stroop_number > self.yes_stroop_number:
            self.b = self.no_stroop_number
        else :
            self.b = self.yes_stroop_number
        self.end_label = tk.Label(self.r,text = 'Τελίωσες το Τεστ',font = 'arial 30 bold')
        self.end_label.pack()
        self.give_results = tk.Button(self.r,text = 'Εμφάνιση αποτελεσμάτων',font = 'arial 20 bold',command = self.show_results)
        self.give_results.pack()
        self.save_results = tk.Button(self.r,text = 'Αποθήκευση αποτελεσμάτων',font = 'arial 20 bold',command = self.save_results)
        self.save_results.pack()

    def show_results(self):
        self.no_stroop_numbers = []
        self.yes_stroop_numbers = []
        for i in self.no_stroop:
            if isinstance(i,float):
                self.no_stroop_numbers.append(i)
        for i in self.yes_stroop:
            if isinstance(i,float):
                self.yes_stroop_numbers.append(i)
        try: self.no_stroop_average = sum(self.no_stroop_numbers)/len(self.no_stroop_numbers)
        except: self.no_stroop_average = '--'
        try: self.yes_stroop_average = sum(self.yes_stroop_numbers)/len(self.yes_stroop_numbers)
        except: self.yes_stroop_average= '--'
        try:stroop_difference = (self.yes_stroop_average - self.no_stroop_average)/self.no_stroop_average
        except:stroop_differrence = '--'
        for x in range(0,self.b):
            try:
                self.no_stroop[x]
                self.st.append((x+1,self.no_stroop[x],self.yes_stroop[x]))
            except:
                if self.b == self.no_stroop_number :
                    self.st.append((x+1,self.no_stroop[x],'-'))
                else :
                    print(x)
                    self.st.append((x+1,'-',self.yes_stroop[x]))
        self.st.append(('Μέσος όρος',self.no_stroop_average,self.yes_stroop_average))
        
        self.total_rows = self.b + 2 
        self.total_columns = 3
        self.time_table(root)
    
    def time_table(self,root):
        root = Tk()
        for i in range(self.total_rows): 
            for j in range(self.total_columns): 
                self.e = Entry(root, width=20, fg='blue',font=('Arial',16,'bold'))  
                self.e.grid(row=i, column=j) 
                self.e.insert(END, self.st[i][j])
        
    def save_results(self):
        self.no_stroop_numbers = []
        self.yes_stroop_numbers = []
        for i in self.no_stroop:
            if isinstance(i,float):
                self.no_stroop_numbers.append(i)
        for i in self.yes_stroop:
            if isinstance(i,float):
                self.yes_stroop_numbers.append(i)
        try: self.no_stroop_average = sum(self.no_stroop_numbers)/len(self.no_stroop_numbers)
        except: self.no_stroop_average = '--'
        try: self.yes_stroop_average = sum(self.yes_stroop_numbers)/len(self.yes_stroop_numbers)
        except: self.yes_stroop_average= '--'
        try:stroop_difference = (self.yes_stroop_average - self.no_stroop_average)/self.no_stroop_average
        except:stroop_differrence = '--'
        with open('mycsv.csv','w',newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(['Try','no stroop','yes stroop'])
            for x in range(0,len(self.no_stroop)):
                if self.no_stroop[x] == 'Λάθος':
                    self.no_stroop[x] = "False"
                    
                elif self.no_stroop[x] == 'Εκτός Χρόνου':
                    self.no_stroop[x] = "Time expired"
                    
            for x in range(0,len(self.yes_stroop)):
                if self.yes_stroop[x] == 'Λάθος':
                    self.yes_stroop[x] = "False"
                    
                elif self.yes_stroop[x] == 'Εκτός Χρόνου':
                    self.yes_stroop[x] = "Time expired"                    
                    
            for i in range(0,self.b):
                try:
                    thewriter.writerow([i+1,self.no_stroop[i],self.yes_stroop[i]])
                except:
                    if self.b == self.no_stroop_number :
                        thewriter.writerow((i+1,self.no_stroop[i],'-'))
                    else :
                        thewriter.writerow((i+1,'-',self.yes_stroop[i]))
            thewriter.writerow(['Average',self.no_stroop_average,self.yes_stroop_average])
        root.mainloop()       

root = tk.Tk()
myapp = Test(root)
root.mainloop()

import random

class Set_up_colors():
 def generate_colors(self):
    allcolors = ['yellow','green','blue','purple','red','orange','black']
    random.shuffle(allcolors)
    self.rc1 = allcolors[0]
    self.rc2 = allcolors[1]
    self.rc3 = allcolors[2]
    self.rc4 = allcolors[3]
    return self.rc1, self.rc2, self.rc3, self.rc4
 def generate_questioncolors(self):
     rquestions = [self.rc1,self.rc2,self.rc3,self.rc4]
     self.q = random.choice(rquestions)
     self.colorofq = random.choice(rquestions)
     return self.q, self.colorofq
 def getcolors(self):
     self.c1 = self.generate_colors()
     self.c2 = self.generate_questioncolors()
     return self.c1, self.c2

     


s = Set_up_colors()



print(s.generate_colors())
print(s.generate_colors()[0])
print(s.generate_questioncolors())
print(s.getcolors())
print(s.getcolors())

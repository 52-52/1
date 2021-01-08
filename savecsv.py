def get_results(self):
        with open('mycsv.csv','w',newline='') as f:
            thewriter = csv.writer(f)
            for i in range(0,10):
                thewriter.writerow([i,self.no_stroop[i],self.yes_stroop[i]])

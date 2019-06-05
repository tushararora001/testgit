# File name: ...\\Source_XII\PyXIIch03\Batsman.py
class Batsman:
    Bcode = Innings = Notouts = Runs = Batavg = 0
    Bname = " "    
    def Batsman_InData(self):
        print ("Enter Batsman's data...")
        self.Bcode = int(input("Enter code: "))
        self.Bname = input("Enter name: ")
        self.Innings = float(input("Enter total innings: "))
        self.Notouts = float(input("Enter total notouts: "))
        self.Runs = float(input("Enter total runs: "))
        self.Batsman__DisplayData()
    def __CalcAvg(self):
        self.Batavg = self.Runs / (self.Innings - self.Notouts)
        print("Batsman's average is: %.2f" % self.Batavg)
    def Batsman__DisplayData(self):
        print ("Batsman's information...")
        print("Code: ", self.Bcode)
        print("Name: ", self.Bname)
        print("Innings: ", self.Innings)
        print("Notouts: ", self.Notouts)
        print("Runs: ", self.Runs)
        self.__CalcAvg()
        
        
B = Batsman()
B.Batsman_InData()

        			

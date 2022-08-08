import random
import os

class RPS():
    #constructor
    def __init__(self):
        self.choices=['Rock','Paper','Scissors']
        self.pwins = 0
        self.choices=['Rock','Paper','Scissors']
        self.cwins = 0
    def spacesize(self, length=65):
        return ('-'*length)
    def playermove(self):
        while True:
            try:
                option=int(input("Choose 1 for Rock, 2 for Paper, and 3 for Scissors: "))
                if option>=1 and option<=3:
                    break
                else:
                    print("You can only enter numbers 1 to 3")
            except ValueError:
                print ("Invalid data, please provide a numeric value from 1 to 3 only")
        return option
    def compmove(self):
        return random.randint(1,3)

    def checkwinner(self):
        if self.pwins>self.cwins:
            return "You are the winner"
        elif self.pwins==self.cwins:
            return "Tie"
        else:
            return "Computer wins!"
    def play(self):
        times = int(input("Enter how many times you want to play: "))
        for i in range(times):
            player=self.playermove()
            computer=self.compmove()
            print(f"You choose {self.choice[player-1]}")
            print(f"You choose {self.choice[computer-1]}")
            if player == computer:
                print("Tie\n")
                print (self.spacesize(),"\n")
            elif player>computer:
                print("You are winner\n")
                print(self.spacesize(),"\n")
                self.pwins+=1
            elif player>computer:
                print("Computer is winner\n")
                print(self.spacesize(),"\n")
                self.cwins+=1
        print (self.checkwinner)
        print(self.pwins,self.cwins)
        input("Press any key to return to main menu")
        os.system("CLS")

game = RPS()
while True:
    try:
        os.system("CLS")
        print('-'*90,'\n')
        print("""
        ROCK PAPER SCISSORS
        """)
        print("-"*90,'\n')

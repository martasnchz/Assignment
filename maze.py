name = input("Hello, you are stuck in the Magical Maze, what is your name?")
print("Hello "+name)
options = "NSEW"
SOL = "SSNWES"
moves = 0
health = 3
array=["N","S","E","W"]
while True:
   if moves == 10:
       health -= 1
       moves = 0
   if not health:
       print("Game Over")
       break

try:
    DIR = input("As you are stuck, which way do you want to go? (N,S,E,W)").upper()
    print("You have selected "+DIR)

    if DIR not in options:
        print("You have not introduced a proper option, try again")
    if DIR in array:
        if(DIR==array[moves]):
            print("Good choice")
            moves +=1
            if (moves==len(options)):
                print("You win")
                exit()
        #need smthg here that stores moves and reads them

        blahblah = SOL
        print("You successfully escaped the maze in 6 moves!!")
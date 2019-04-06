#This is only a basic example of some python concepts, not anywhere close to a good/complete project
'''
Example for Las Lomas Hack Club
By: Evan Nishi
Liscense: Do whatever you want with this, it took me like 20 min for this demo.
'''
#quick example of control flow and program logic, may be a bit sloppy, also example for txt file saving
import random
lives = 5
gold = 0
tunnel_events = {1:"You get hit by a dart trap! Oh no! \n you lose 1 life",2:"You find 3 gold!",3: "You find a skeleton!",4:"You find a huge pot of gold!"}
def lose():
    play_again = input("You ran out of lives, you lose...\n do you want to play again?  Your score was: {} ".format(gold))
    if (play_again == "y" or play_again == "yes"):
        print("playing again")
        start_game()
    else:
        quit()
def start_game():
    print("Welcome to temple explorer")
while lives > 0:
    print("-------------------------------------------------------")
    print("Lives:", lives , "Gold:", gold)
    print("You have finally found the ancient temple")
    print("There are four caves, which one will you pick?")
    tunnel_number = input("Choose 1,2,3,4: ")
    if (tunnel_number == '1'):
        print(tunnel_events[1])
        lives = lives - 1
    elif (tunnel_number == '2'):
        print(tunnel_events[2])
        gold = gold + 3
    elif(tunnel_number == '3'):
        print(tunnel_events[3])
        fight = input("Do you want to fight it? y/n?: ")
        win = random.randint(1,2)
        if (fight == 'y' or fight == 'yes'):
            if (win == 1):
                print("You won, and got 3 gold!")
                gold = gold + 3
            elif(win == 2):
                print("You lost!")
                lives = lives - 1
            else:
                print("You ran away")
    elif(tunnel_number == '4'):
        print(tunnel_events[4])
        gold = gold + 5
    else:
        print("invalid input")
    if (lives == 0):
        lose()
    else:
        continue
start_game()
#ha, only 56 lines, child's play

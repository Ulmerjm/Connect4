"""
This will contain to logic to play with game with two human players.

@Author John Ulmer
@Author Richard Muench
"""

class Players:

    """
    Simple method for gathering the name of the players.
    """
    def AskNames():
        playernames = []
        
        playernames.append(input("Player One, what is your name? "))
        playernames.append(input("Player Two, what is your name? "))

        return playernames

    """
    Short rock paper scissors game to determine who should go first?
    It isnt working and it makes me sad
    """
    def Order(playernames):
        print("We will now decide who goes first...")
        print("This will be a normal game of Rock, Paper Scissors, please choose one when asked.")

        playerchoices = []

        playerchoices.append(input(playernames[0] + ", Please choose an option. ").lower().strip())

        while True:
            if playerchoices[0] != "rock" or "paper" or "scissors":
                print("Your input must be rock, paper or scissors.")
                playerchoices.append(input(playernames[0] + ", Please choose an option. ").lower().strip())
                print(playerchoices[0])
                continue
            else:
                break

        playerchoices.append(input(playernames[1] + ", Please choose an option. ").lower().strip())

        while True:
            if playerchoices[1] != "rock" or "paper" or "scissors":
                print("Your input must be rock, paper or scissors.")
                playerchoices.append(input(playernames[1] + ", Please choose an option. ").lower().strip())
                continue
            else:
                break


    Order(AskNames())
    
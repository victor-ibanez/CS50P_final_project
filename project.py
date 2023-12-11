from pyfiglet import Figlet
import random
import os
import sys

def main():
    figlet=Figlet()
    intro_message="Welcome to Secret Santa Game"
    print(figlet.renderText(intro_message))
    print("In case you need to end the game just press Ctrl+C")
    game()

def santa_asks(text):
    i=input(f"🎅: {text}")
    return i
def santa_says(text):
    print(f"🎅:{text}")

def game():
    num=check_num_players()
    players=players_name(num)
    assigned=giveaway(players)
    tell_names(players,assigned)



def check_num_players():
    while True:
        try:
            num=int(santa_asks("Ho Ho How many players? "))
            if num > 1:
                return num
            else:
                santa_says("You need more players, maybe try again")

        except ValueError:
            santa_says("Oops I didnt catch that please try again")
        except KeyboardInterrupt:
            print()
            sys.exit(santa_says("Ho Ho Hope I see you soon"))



def players_name(num):
    try:
        players=[]
        num=range(num)
        for n in num:
            while True:
                player=santa_asks(f"Please input player's #{n+1} name: ")
                if check_player(player, players) == True:
                    players.append(player)
                    break
        return players
    except KeyboardInterrupt:
            print()
            sys.exit(santa_says("Ho Ho Hope I see you soon"))

def check_player(name, players):
    if name in players:
        santa_says("That player has already been entered...")
        return False
    elif name.isalpha()==False:
        santa_says("That name is not valid please type only alphabetical characters")
        return False
    else:
        return True

def giveaway(players):
    assignated=[]
    while True:
        for player in players:
            while True:
                num=int(random.uniform(0,len(players)))
                gifted=players[num]
                if check_gifted(player, gifted, assignated)==True:
                    assignated.append(gifted)
                    break
        if check_giveaway(players, assignated) == True:
                break
    return assignated


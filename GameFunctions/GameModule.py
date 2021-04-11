#Variables
player = 0
bot = 0
draw = 0

#score resume
def score():
    global player, bot, draw

    print("=-=-" * 15, "\n")
    print(" "*25, "SCORE\n")
    print(f"Player: {player} wins")
    print(f"BOT: {bot} wins")
    print(f"DRAW: {draw} games")
    print("=-=-" * 15, "\n")


# return the chosed and the random item
def chosed(a, b):
    if a == 1:
        print("Selected: PAPER")
    if a == 2:
        print("Selected: ROCK")
    if a == 3:
        print("Selected: SCISSORS")
    
    if b == 1:
        print ("Bot = PAPER")
    if b == 2:
        print ("Bot = ROCK")
    if b == 3:
        print("Bot = SCISSORS")


#conditional rule per round
def check (var1, var2):
    global player, bot, draw

    if var1 == 1:
        if var2 == 1:
            draw += 1
            print("DRAW GAME!!")
        elif var2 == 2:
            player += 1
            print("Player WIN!!")
        else:
            bot += 1
            print("Bot WIN!!")
    
    elif var1 == 2:
        if var2 == 2:
            draw += 1
            print("DRAW GAME!!")
        elif var2 == 3:
            player += 1
            print("Player WIN!!")
        else:
            bot += 1
            print("Bot WIN!!")
    
    else:
        if var2 == 3:
            draw += 1
            print("DRAW GAME!!")
        elif var2 == 1:
            player += 1
            print("Player WIN!!")
        else:
            bot += 1
            print("Bot WIN!!")
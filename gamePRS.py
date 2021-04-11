# Game PAPER-ROCK-SCISSORS

from random import randint

#score resume
def score():
    global player, bot, draw

    print("=-=-" * 15, "\n")
    print(" "*25, "SCORE\n")
    print(f"Player: {player} wins")
    print(f"BOT: {bot} wins")
    print(f"DRAW: {draw} games")
    print("=-=-" * 15, "\n")
    return

# return the chosed and the random item
def chosed(a, b):
    global var1, var2
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
    
    return


#conditional rule per round
def check ():
    global player, bot, draw, var1, var2

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
    
    return 


#entry and variables
player = 0
bot = 0
draw = 0
var1 = var2 = 0
r = "S"

#game code
print("+-+-"*15, "\n")
print(" "*15, "Game PAPER-ROCK-SCISSORS\n")
print("+-+-" * 15, "\n")

while r == "S":
    var2 = randint(1,3)
    print("\n[1] - PAPER\n[2] - ROCK\n[3] - SCISSORS \n")
    
    var1 = int(input("Select a number: "))
    while (var1 < 1 or var1 > 3):
        var1 = int(input("Select a number: "))
    
    print(f"\n {chosed(var1, var2)}")
    print(check())
    print(score())

    r = input("Retry? (s/n)").upper()
    if not (r == "S" or r == "N"):
        r = input("Retry? (s/n)").upper()

print("\n--  GAME OVER  --\n")

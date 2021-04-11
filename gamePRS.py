# Game PAPER-ROCK-SCISSORS

from random import randint
from GameFunctions import GameModule

#Variables
var1 = var2 = 0
r = "S"

#   GAME CODE

#Start Header
print("+-+-"*15, "\n")
print(" "*15, "Game PAPER-ROCK-SCISSORS\n")
print("+-+-" * 15, "\n")

#iteration
while r == "S":
    var2 = randint(1,3)
    print("\n[1] - PAPER\n[2] - ROCK\n[3] - SCISSORS \n")
    
    var1 = int(input("Select a number: "))
    while (var1 < 1 or var1 > 3):
        var1 = int(input("Select a number: "))
    
    print(f"\n {GameModule.chosed(var1, var2)}")
    print(GameModule.check(var1, var2))
    print(GameModule.score())

    r = input("Retry? (s/n)").upper()
    if not (r == "S" or r == "N"):
        r = input("Retry? (s/n)").upper()

print("\n--  GAME OVER  --\n")

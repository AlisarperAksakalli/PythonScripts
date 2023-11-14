import time
import random

start = input("To Start Type Any Word")

victims = 15

limit = 1





print("You Came Here As Detective To Find Out The Murderer")

print("Around like 1, 15 victims if you can guess one you win!")

while True:
    print("To vote a victim, you must type number between", limit, "and", victims)
    choosed = int(input("Who Victim You Choose? (murderer can become different number each time you choose(disguise)"))
    
    if victims <= 1:
            print("You Died Instantly Because 1 person")
            break
    
    murderer = random.randint(limit, victims)
    
    killchance = random.randint(1, 8)
    
    victimdeathchance = random.randint(1, 3)
    
    victims = victims - 1
    
    print("You Choosed an victim...")
    time.sleep(3)
    print("The lights goes off...")
    time.sleep(3)
    
    if choosed == murderer:
        print("Congrats! You Found The Murderer!")
        print("Gameover...")
        break
    else:
        if killchance == 1:
            print("You were Killed by a Murderer!")
            print("Gameover...")
            break
        else:
            if victimdeathchance == 1:
                victims = victims - 1
                print("An Victim Found Dead")
            else:
                print("Nobody Died This Night!")
    
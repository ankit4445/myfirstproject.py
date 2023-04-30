import random
l=["rock","scissor","paper"]
while True:
    ucount=0
    ccount=0
    uc=int(input('''
Game Start...
1 Yes
2 No | Exit    
    '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1. Rock
2. scissor
3 paper                 
            '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            cChoice=random.choice(l)
            print(uchoice)
            print(cChoice)
            if cChoice==uchoice:
                print("computer value",cChoice)
                print("user choice",uchoice)
                print("Game draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and cChoice=="scissor") or (uchoice=="paper" and cChoice=="rock") or (uchoice
            =="scissor" and cChoice=="paper"):
                print("computer value",cChoice)
                print("user value",uchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("computer value", cChoice)
                print("user value", uchoice)
                print("computer  win")
                ccount = ccount + 1
    if ucount==ccount:
        print("final game draw...")
        print("user score",ucount)
        print("computer score",ccount)
    elif ucount>ccount:
        print("finally u won the game..")
        print("user score", ucount)
        print("computer score", ccount)
    else:
        print("computer won the game..")
        print("user score", ucount)
        print("computer score", ccount)



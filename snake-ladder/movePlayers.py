# 1) THIS FUNCTION WILL ROLL THE DICE AND WILL INCREASE THE POSITION DEPENDING ON THE VALUE OF DICE
# 2) AND ALSO WILL CHECK FOR OVERFLOW
# 3) DEPENDIGN ON THE NEW POSITION IT WILL CHECK IF THERE IS ANY SNAKE AT THAT POSITION, IF THERE IS 
    # ONE SNAKE IT WILL BRING THAT PLAYERS POSITION DOWN
# 4)SAME GOES FOR LADDERS IF PLAYERS END UP AT LADDER BOTTON IT WILL CLIMB
import random
import snakesPositions
import laddersPositions

class MovePlayer:

    def move(player, value):
        roll_dice = random.randint(1, 6)
        num = value + roll_dice
        if num > 100:
            print(f"BAD LUCK, YOU CANT MOVE, YOU NEED {100 - value} TO WIN")
            return value

        if num == 100:
            return num

        # IF PLAYER IS NOT REACHED HOME
        print(player, "Rolled a ", roll_dice, " and moved from", value, " to ", num)

        # TO CHECK IF PLAYER STOPPED ON SNAKE HEAD
        if num in snakesPositions.snakes:
            print(player, " got bitten by a snake and is now on", snakesPositions.snakes[num])
            num = snakesPositions.snakes[num]
            # to check if even after bitten by snake is there any other snakes or ladder at
            # that position
            if num in snakesPositions.snakes:
                print(player, " got bitten by a snake again! and is now on", snakesPositions.snakes[num])
                num = snakesPositions.snakes[num]
            if num in laddersPositions.ladders:
                print(player, " Your Lucky after bitten by snake you got a ladder your now on ", laddersPositions.ladders[num])
                num = laddersPositions.ladders[num]

        # IF PLAYER IS ON LADDER BOTTOM IT WILL CLIMB THE LADDER
        if num in laddersPositions.ladders:
            print(player, "Climbed the ladder and is now on ", laddersPositions.ladders[num])
            num = laddersPositions.ladders[num]
            # extra functionality
            if num in snakesPositions.snakes:
                print(player, " bad luck bro! just climbed and again bitten by snakes and your now on ", snakesPositions.snakes[num])
                num = snakesPositions.snakes[num]
            if num in laddersPositions.ladders:
                print(player, " Your lucky You climbed again! and your now on ", laddersPositions.ladders[num])
                num = laddersPositions.ladders[num]

        return num
    


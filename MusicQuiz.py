'''Game Basics:  ---> Music Quiz
Game has 3 or more levels and each level contains 4 or more blanks to fill in
(---> Extra Level: User can choose Genre: Rock & Pop, HipHop, Jazz, Rick Astley Special ...)

Beginning the Game
Immediately after running the program, user is prompted to select a difficulty level
 from easy / medium / hard
Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.

Game Play
When player guesses correctly, new prompt shows with correct answer in the previous blank
and a new prompt for the next blank
When player guesses incorrectly, they are prompted to try again'''


def game_level():
    #user chooses his level
    level = input('Choose your level: 1 for easy, 2 for medium, 3 for hard:')
    if level == 1:
        print('You have chosen the easy level, Good luck!')
    elif level == 2:
        print('You have chosen the medium level, Try your best!')
    elif level == 3:
        print('You have chosen the hard level, You need more than luck!')
    else:
        print ('You did not chose a number between 1 and 3. Try again!')
        game_level()

game_level()

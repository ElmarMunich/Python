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
When player guesses incorrectly, they are prompted to try again

No functions are longer than 18 lines of code (does not include blank lines, comments, or function definitions)


Wikipedia contributors. (2018, March 13). Rick Astley. In Wikipedia, The Free Encyclopedia.
Retrieved 14:47, March 27, 2018, from https://en.wikipedia.org/w/index.php?title=Rick_Astley&oldid=830205124

Wikipedia contributors. (2018, March 29). Rihanna. In Wikipedia, The Free Encyclopedia.
Retrieved 17:44, March 29, 2018, from https://en.wikipedia.org/w/index.php?title=Rihanna&oldid=833024608

Wikipedia contributors. (2018, March 27). Madonna (entertainer). In Wikipedia, The Free Encyclopedia.
Retrieved 18:00, March 29, 2018, from https://en.wikipedia.org/w/index.php?title=Madonna_(entertainer)&oldid=832678186
'''

Rick = ['Richard Paul Astley',
'Rick Astleys 1987 song ..... Gonna Give You Up was a No. 1 hit single in 25 countries.',
'never',
'Rick Astleys 1987 song Never Gonna Give You Up was a No. 1 hit single in 25 countries.',
'The song won the 1988 Brit Award for Best British ......',
'single',
'The song won the 1988 Brit Award for Best British Single',
'Astley made a comeback in 2007, becoming an ........ phenomenon',
'internet',
'Astley made a comeback in 2007, becoming an Internet phenomenon',
'His music video for "Never Gonna Give You Up" became integral to the meme known as .......',
'rickrolling',
'His music video for "Never Gonna Give You Up" became integral to the meme known as rickrolling',
]

Rihanna = ['Robyn Rihanna Fenty','Rihanna is a Barbadian-born singer, .......... and actress',
'songwriter',
'Rihanna is a Barbadian-born singer, songwriter and actress',
'In 2005, Rihanna rose to fame with the release of her ..... studio album Music of the Sun and its follow-up A Girl like Me (2006)',
'debut',
'In 2005, Rihanna rose to fame with the release of her debut studio album Music of the Sun and its follow-up A Girl like Me (2006)',
'Many of her songs rank among the world`s best-selling singles of all time, including the single .........',
'umbrella',
'Many of her songs rank among the world`s best-selling singles of all time, including the single Umbrella.',
'Among numerous awards and accolades, Rihanna has won nine Grammy Awards, twelve American MusicAwards and twelve .. .. .. .. Music Awards.',
'billboard',
'Among numerous awards and accolades, Rihanna has won nine Grammy Awards, twelve American Music Awards and twelve Billboard Music Awards.',
]

Madonna = ['Madonna Louise Ciccone',
'Madonna is an American singer, songwriter, actress, and ..............',
'businesswoman',
'Madonna is an American singer, songwriter, actress, and businesswoman.',
'After performing as a ......., guitarist and vocalist in the music groups Breakfast Club and Emmy, Madonna signed with Sire Records in 1982. ',
'drummer',
'fter performing as a drummer, guitarist and vocalist in the music groups Breakfast Club and Emmy, Madonna signed with Sire Records in 1982.',
'Her other ventures include fashion design, writing childrens books, opening of health clubs, and filmmaking. She also contributed in various charities and founded the .............. organization in 2006.',
'raising malawi',
'Her other ventures include fashion design, writing childrens books, opening of health clubs, and filmmaking. She also contributed in various charities and founded the Raising Malawi organization in 2006.',
'Upon being confirmed in the Catholic Church in 1966, she adopted .......... as a confirmation name.',
'veronica',
'Upon being confirmed in the Catholic Church in 1966, she adopted Veronica as a confirmation name.',
]

not_correct = 'Your answer is not correct. Try again'




level = 0
def game_level():
    #user chooses his level
    print ('Welcome to the world of music. In this game you can shine with your music knowledge!!!')
    level = input('Choose your level: 1 for easy, 2 for medium, 3 for hard:')
    if level == 1:
        print('You have chosen the easy level, Good luck!')
        fill_in_the_blank(Rick)
    elif level == 2:
        print('You have chosen the medium level, Try your best!')
        fill_in_the_blank(Rihanna)
    elif level == 3:
        print('You have chosen the hard level, You need more than luck!')
        fill_in_the_blank(Madonna)
    else:
        print ('You did not choose a number between 1 and 3. Try again!')
        game_level()


def fill_in_the_blank(artist):
    set=1
    pos=1
    #Prompts a sentence to the user with a blank to fill in.
    while set <= 4:
        print(artist)[pos]
        answer = raw_input('Fill the blank >>> use only lower cases <<< : ')
        if answer == (artist)[pos+1]:
            print(artist)[pos+2]
            pos = pos + 3
            set = set + 1
        else:
            print(not_correct)

    print('Congratulations !!! You know a lot about the artist:')
    print(artist[0])





game_level()

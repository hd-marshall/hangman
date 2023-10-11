import random

# PICKS A RANDOM WORD FROM THE ARRAY OF WORDS
def pickWord():
    words = [
    "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom",
    "azurefoxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby",
    "galaxy", "galvanize", "gazebo", "giaour", "gizmoengths", "lucky",
    "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave",
    "mnemonic", "mystify", "naphtha"
    ]
    randIndex = random.randint(0, len(words) - 1)
    guessWord = words[randIndex]
    print('It is a ' + str(len(guessWord)) + ' letter word.')
    return guessWord

# DISPLAYS THE PLAYERS CURRENT STATUS IN THE GAME
def livesCounter(lives):
    print('You have ' + str(lives) + ' left.')
    hangmanStages = [
    '''
    +---+
    |   \|
    O    |
    /|\  |
    / \  |
         |
    =========
    ''',
    '''
    +---+
    |    |
    O    |
    /|\  |
    /    |
         |
    =========
    ''',
    '''
    +----+
    |     |
    O     |
    /|\   |
          |
          |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
        |   
        |
        |
        |
        |
    =========
    ''',
    '''
        |   
        |
        |
        |
        |
    =========
    ''',
    '''

    


     =========
    ''',
    ]
    print(hangmanStages[lives])

# CHECK FOR VALID INPUT FROM USER
def validateLetter(pickedLetter):
    check = False
    while True:
        letter = input('Enter a letter? ').lower()
        # check the letter has not already been selected
        if letter not in pickedLetter:
            check = True
        # return letter if its of valid size and character
        if len(letter) == 1 and letter.isalpha() and check == True:
            print("\n")
            return letter

# CHECK THE LETTER IS IN THE WORD
def checkLetter(guess, arr, letter):
    loseLife = True
    counter = 0
    # iterate through the pickedWord taking both the letter at the index and the value of the index
    for i, l in enumerate(guess):
        # if the letter guessed is in the word change loseLife to false and add the letter at the same index to the empty array that is being displayed to the player
        if letter == l:
            arr[i] = l
            loseLife = False
            counter += 1
    if counter != 0:
        print("** There was " + str(counter) + " ocurrances of letter: " + letter + " **")
    return loseLife

# PRINT ALL PICKED USER PICKED LETTERS WHILST PLAYING
def inputsPicked(letterArr, input):
    letterArr.append(input)
    if len(letterArr) != 0:
        print("Letters that have been picked: ")
        print(letterArr)

# CHANGE THE VALUE OF LIFES LEFT
def loseLife(loseLife):
    lifeValue = 0
    if loseLife == True:
        lifeValue = -1
    return lifeValue

# CHECK THE PLAYER HAS WON BY ITERATING THROUGH THE ARRAY AND DISPLAYINH
def checkWin(chosenWordArr):
    if '_' not in chosenWordArr:
        return True

# RESTART GAME FUNCTION
def validateRestart():
    while True:
        restart = input('Would you like to play again? (yes / no) ')
        if restart == 'yes' or restart == 'no':
            return restart

def main():
    runGame = 'yes'

    # begin loop for the game
    while runGame == 'yes':
        # intialise the word
        chosenWord = pickWord()
        # create empty array that is being displayed
        chosenWordArr = ['_'] * len(chosenWord)
        # intialise the beginning lives
        lives = 7
        pickedLetters = []

        while lives > 0:
            print(chosenWordArr, "\n")
            letter = validateLetter(pickedLetters)
            # this function can return 0 or -1 depending on the checkLetter
            lives = lives + loseLife(checkLetter(chosenWord, chosenWordArr, letter))
            if checkWin(chosenWordArr) == True:
                print('You won congrats!!')
                print(chosenWordArr)
                break
            if lives == 0:
                print('You lost!! the word was ' + chosenWord)
                break
            inputsPicked(pickedLetters, letter)

        runGame = validateRestart()

main()
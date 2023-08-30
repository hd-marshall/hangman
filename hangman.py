import random

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

def validateLetter(pickedLetter):
    check = False
    while True:
        letter = input('Enter a letter? ').lower()
        if letter not in pickedLetter:
            check = True
        if len(letter) == 1 and letter.isalpha() and check == True:
            print("\n")
            return letter

def checkLetter(guess, arr, letter):
    loseLife = True
    counter = 0
    for i, l in enumerate(guess):
        if letter == l:
            arr[i] = l
            loseLife = False
            counter += 1
    if counter != 0:
        print("** There was " + str(counter) + " ocurrances of letter: " + letter + " **")
    return loseLife

def inputsPicked(letterArr, input):
    letterArr.append(input)
    if len(letterArr) != 0:
        print("Letters that have been picked: ")
        print(letterArr)

def loseLife(loseLife):
    lifeValue = 0
    if loseLife == True:
        lifeValue = -1
    return lifeValue
    
def checkWin(chosenWordArr):
    if '_' not in chosenWordArr:
        return True

def validateRestart():
    while True:
        restart = input('Would you like to play again? (yes / no) ')
        if restart == 'yes' or restart == 'no':
            return restart

def main():
    runGame = 'yes'

    while runGame == 'yes':
        chosenWord = pickWord()
        chosenWordArr = ['_'] * len(chosenWord)
        lives = 7
        pickedLetters = []

        while lives > 0:
            print(chosenWordArr, "\n")
            letter = validateLetter(pickedLetters)
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

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''']

import random

lives = 6
word_list = ["ardvark" , "baboon", "camel"]
chosen_word = random.choice(word_list)
# testing
print(f"pssst, the solution is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game :
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"current position : {position} \n current letter : {letter} \n guessed letter : {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word :
      lives -= 1
      print(stages[lives])
      if lives == 0 :
        end_of_game = True
        print("you loose !!")
        


    print(display)

    if "_" not in display :
        end_of_game = True
        print("you win")

# challenge 4
    







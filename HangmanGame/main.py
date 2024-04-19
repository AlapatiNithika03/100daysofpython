#import modules
import random
from hangman_art import logo, stages
from hangman_words import word_list
print(logo)
chosen_word = random.choice(word_list)
lives = 3
#testing code
#print(f'{chosen_word}.')
#create blanks
display=[]
for _ in chosen_word:
  display += "_"
end_of_game = False
while not end_of_game:
  guess = input("Guess a letter : ").lower()

#check guessed letter
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter==guess:
        display[position] = letter
  #if guess is not in the word
  if guess not in chosen_word:
    lives -= 1
    if lives==0:
      end_of_game=True
      print("You lose")
  #join all the elements in the list and turn it inot a string
  print(f"{''.join(display)}")
  #check if the user got all letters
  if "_" not in display:
    end_of_game = True
    print("You win")
  print(stages[lives])  

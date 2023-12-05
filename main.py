
import random
import string

words = ["chicken", "rice", "nuggets", "strawberry"]
algorithm_choice = random.choice(words)

#Break down the word into letters. FYI, I declared this var as a list, because of that the while loop iterated until strikes = 6, took me two hours to figure it out and set it up as a set. 
word_letters = set(algorithm_choice)

#Storing the alphabet to validate letters used by user.
alphabet = set(string.ascii_lowercase)
letters_used = set()

input("""
    Hello there! this is the classic hangman game.
    Be welcome to have fun, on the other hand, let me introduce you on the basic rules.\n
    Rule #1: Sticky man has 0 strikes at the beginning, but if you get caught with 6 strikes, say goodbye and play again.
    Rule #2: Have fun!

    PRESS ANY KEY TO CONTINUE: """)

strikes = 0

while strikes < 6 and len(word_letters) > 0:
    word_list = []

    #Validate if letter has been used before.
    for letter in algorithm_choice:
        if letter in letters_used:
            word_list.append(letter)
            #print(word_list, letter, letters_used)
        else:
            word_list.append('-')
            #print(word_list, letter, letters_used)

    print("""
          Current word: """, ' '.join(word_list), f"""
          Strike number #{strikes}""")
    

    user_letter = input("""
            Dear user, guess a letter: """).lower().strip()
    
    #Validate if the letter has not been used before.
    if user_letter in alphabet - letters_used:
        letters_used.add(user_letter)
        if user_letter in word_letters:
            #Remove letter guessed to avoid repetition.
            word_letters.remove(user_letter)
            print("")
        else:
            print("""
                  Wrong dude.""")
            strikes += 1
    elif user_letter in letters_used:
        print("""
              You have already used that letter .-.""")
    else:
        print("""
              Type a valid character.""")
        
    

if strikes > 6:
    print(f"""
          Game over. The word was {algorithm_choice}""")
else:
    print("""
          Congrats, you guessed it!""")
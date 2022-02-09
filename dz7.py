
# Пишем игру. Программа выбирает из диапазона чисел (пусть для начала будет 1-100)
# случайное число и предлагает пользователю его угадать. Пользователь вводит число. 
# Если пользователь не угадал - предлагает пользователю угадать еще раз, пока он не угадает. 
# Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить.


def prompt_user(prompt_message : str) -> bool :
    print(prompt_message, end=' [Y|N]')
    
import random
user_wants_to_proceed = True
while user_wants_to_proceed:
    userGuessed = False
    while not userGuessed:
        NumberToGuess = random.randint(1, 100)
        userGuess = int(input("Guess a number in the range [1..100]"))
        userGuessed = NumberToGuess == userGuess
        if userGuessed:
            print("Guessed!")
        else:
            print("Not guessed yet, try again")
    # while not userGuessed
    user_wants_to_proceed = prompt_user("Do you want to proceed?")
# while user_wants_to_proceed

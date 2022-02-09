from lib import prompt_user

user_wants_to_proceed = True
while user_wants_to_proceed:
    print("Enter a sting here>", end="")
    user_string = input()
    print(user_string)
    user_wants_to_proceed = prompt_user("Do you want to proceed?")

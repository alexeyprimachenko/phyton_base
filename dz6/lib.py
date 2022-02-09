def prompt_user(prompt_message : str) -> bool :
    print(prompt_message, end=' [Y|N]')
    user_answer = input()
    print()
    return (len(user_answer) > 0) and (user_answer[0] in ['y', 'Y'])
# def get_user_confirmation()

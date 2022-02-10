# Модифицируем ДЗ 2. Напишите с помощью функций!. Помните о Single Responsibility! Попросить ввести свой возраст (можно использовать константу или input()). Пользователь ввел значение возраста [year number] а на место [year string] нужно поставить правильный падеж существительного "год", который зависит от значения [year number].
# если пользователь ввел непонятные данные (ничего не ввел, ввел не число, неактуальный возраст и тд.) - вывести “не понимаю”
# если пользователю меньше 7 - вывести “Тебе [year number] [year string], где твои мама и папа?”
# если пользователю меньше 18 - вывести “Тебе [year number] [year string], а мы не продаем сигареты несовершеннолетним”
# если пользователю больше 65 - вывести “Вам уже [year number] [year string], вы в зоне риска”!
# в любом другом случае - вывести “Оденьте маску, вам же [year number] [year string]!”
# Например:

# Тебе 1 год, где твои мама и папа?

# Оденьте маску, вам же 23 года!

# Вам уже 68 лет, вы в зоне риска!


# Returns a positive number that specifies the user age. A zero value means, the user has not provided his age.
def ask_user_age(user_prompt : str) -> int :
    try:
        age = max(0, int(input(user_prompt)))
    except:
        age = 0
    return age
# def ask_user_age()

# Returns the word "years" in a proper form in Russian (UTF-8 encoding) depending on the actual number of years
# Example: 1 -> year; 2 -> years, etc.
def get_years(years : int) -> str :
    YEARS_ENDINGS = ["лет", "год", "года", "года", "года", "лет", "лет", "лет", "лет", "лет"]
    if (10 <= years) and (years <= 20):
        return "лет"
    else:
        return YEARS_ENDINGS[years % 10]
# def get_years()

age = ask_user_age("Сколько Вам лет?")
if age <= 0:
    print("Не понимаю Ваш ответ.")
    exit(1)

if age < 7:
    print("Тебе {} {}, где твои мама и папа?".format(age, get_years(age)))
    exit(0)

if age < 18:
    print("Тебе {} {}, а мы не продаем сигареты несовершеннолетним!".format(age, get_years(age)))
    exit(0)

if age <= 65:
    print("Оденьте маску, вам же {} {}!".format(age, get_years(age)))
    exit(0)

print("Вам уже {} {}, Вы в зоне риска!".format(age, get_years(age)))
exit(0)

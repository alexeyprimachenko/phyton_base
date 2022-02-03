#1 Есть строка произвольного содержания. 
# Написать код, который найдет в строке самое короткое слово, в котором присутствуют подряд две гласные буквы.


SYS_MAX_INT = 0x7FFFFFFF
OUTSIDE_A_WORD = 0
INSIDE_A_WORD  = 1
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', \
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
           'U', 'V', 'W', 'X', 'Y', 'Z',                     \
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', \
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', \
           'u', 'v', 'w', 'x', 'y', 'z']
VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']

if __name__ == '__main__':
  phrase = input('Enter here: ')

  phrase += " " 
  state = OUTSIDE_A_WORD
  word_contains_two_subsequest_vowels = False
  last_letter_is_vowel = False
  word_length = 0
  min_word_length = SYS_MAX_INT
  the_shortest_word = ''
  last_word_starts_at = 0
  for i in range(0, len(phrase)):
    c = phrase[i]
    if state == OUTSIDE_A_WORD:
      if c in LETTERS:
        state = INSIDE_A_WORD
        word_length = 1
        last_word_starts_at = i
        last_letter_is_vowel = c in VOWELS
        word_contains_two_subsequest_vowels = False
      continue

    if state == INSIDE_A_WORD:
      if c in LETTERS:
        word_length += 1
        current_letter_is_vowel = c in VOWELS
        if last_letter_is_vowel and current_letter_is_vowel:
          word_contains_two_subsequest_vowels = True
        last_letter_is_vowel = current_letter_is_vowel
      else:
        state = OUTSIDE_A_WORD
        if word_contains_two_subsequest_vowels:
          if word_length < min_word_length:
            min_word_length = word_length
            the_shortest_word = phrase[last_word_starts_at:i]
      continue
  
  if min_word_length != SYS_MAX_INT:
    print("The shortest word that contains at least two subsequent vowels is:", the_shortest_word)
  else:
    print("Not a single word in your phrase contains at least two subsequent vowels")






# #2
# Есть два числа - минимальная цена и максимальная цена. 
# Дан словарь продавцов и цен на какой 
# то товар у разных продавцов: 
# { "citrus": 47.999, "istudio" 42.999, "moyo": 49.999, "royal-service": 37.245, "buy.ua": 38.324, "g-store": 37.166, "ipartner": 38.988, "sota": 37.720, "rozetka": 38.003}. 
# Написать код, который найдет и выведет на экран список продавцов, чьи цены попадают в диапазон между нижней и верхней ценой. Например:
# lower_limit = 35.9
# upper_limit = 37.3


RESELLERS = {
  "citrus"        : 47.999,
  "istudio"       : 42.999,
  "moyo"          : 49.999,
  "royal-service" : 37.245,
  "buy.ua"        : 38.324,
  "g-store"       : 37.166,
  "ipartner"      : 38.988,
  "sota"          : 37.720,
  "rozetka"       : 38.003
}
LOWER_LIMIT = 35.9
UPPER_LIMIT = 37.3

if __name__ == '__main__':
  print("Below are resellers that offer their goods at a price within", LOWER_LIMIT, "-", UPPER_LIMIT)
  for reseller in RESELLERS:
    if (LOWER_LIMIT <= RESELLERS[reseller]) and (RESELLERS[reseller] <= UPPER_LIMIT):
      print(reseller)



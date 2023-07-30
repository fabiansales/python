# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Enter a Word: ")
user_word = user_word.upper()
vocales = "AEIOU"
word_without_vocal = ""
for letter in user_word:
    if letter in vocales:
        continue
    else:
        print(letter)
        word_without_vocal += letter

print(f"The word without vowels is: {word_without_vocal}")






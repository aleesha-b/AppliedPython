word = input("Please enter a word to be altered: ")
alterAmount = input("Enter the number of letters for your word to be altered by: ")

for letter in word:
    if letter != " ":
        alteredLetter = ord(letter) + int(alterAmount)
        print(chr(alteredLetter))
    else:
        print(" ")
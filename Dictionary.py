from PyDictionary import PyDictionary

dictionary = PyDictionary

while True:

    word = input("What is the definition of: ")
    if word == "":
        break

    print(dictionary.meaning(word))
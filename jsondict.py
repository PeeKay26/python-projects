# Interactive Dictionary
import json
fin = open("dictionary.json","r")
cont = json.load(fin) #dict

# Word starting with specific letter
def display():
    letter = input("Enter the letter with which the word begins: ")
    for i in cont: #searches key
        if i[0] == letter: #searches for words with first letter in key
            print (i)

# Word search
def search(): 
    word = input("What word are you looking for? ")
    found = False
    for i in cont: #searches key
        if i == word:
            found = True
    if found == False:
        print (f"'{word}' does not exist in the dictionary")
    else:
        print (f"'{word}' is in the dictionary")

# Word and meaning search
def meansearch():
    word = input("What word's meaning are you looking for? ")
    found = False
    for i in cont:
        if i == word:
            print (f"{word}: {cont[word]}")
            found = True
        
    if found == False:
        print (f"'{word}' does not exist in the dictionary")

# Looking for a word in definitions
def searchsw():
    word = input("Enter the word in the definition: ")
    found = False
    for k, val in cont.items(): #items() unpacks dictionary into key, value
        if word in val:
            print ("{}".format(k))
            found = True
        
    if found == False:
        print (f"'{word}' is not in the dictionary")

while True:
    print("""
    1. Display all words starting with a specific letter
    2. Search for a word
    3. Search for a word and display meaning
    4. Search for a word in definitions
    5. Exit""")
    choice = int(input("Enter the number of the action you want to carry out: "))
    if choice == 1:
        display()
    elif choice == 2:
        search()
    elif choice == 3:
        meansearch()
    elif choice == 4:
        searchsw()
    elif choice == 5:
        break
    else:
        print ("Enter an appropriate number")
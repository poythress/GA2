# Dalen Carr–dcarr18@student.gsu.edu
# Matias Espinoza–mespinoza2@student.gsu.edu
# Elizabeth Poythress-epoythress3@student.gsu.edu

import string

string1 = input("Enter a string: ")
string2 = string1
print()

print("Enter p if you'd like to delete all punctuation from the string. \n"
      "Enter c if you'd like to know the number of words in the string. \n"
      "Enter w, then type a word if you'd like to know whether that word is in the string. \n"
      "Enter r if you'd like to replace a word in the string, then enter the word you'd like to replace \n"
      "followed by the word you'd like to replace it with.\n"
      "Enter q if you'd like to quit.\n")

command = input(">")

while command != 'q':
    if command == 'p':
        string1 = string1.translate(str.maketrans('','', string.punctuation))
        print(string1)
    elif command == 'c':
        print(len(string1.split()))
    command = input(">")
    if command == 'w':
        string3 =input("Enter word:")
        if string3 in string2:
            print(string3, "is in", string2)
        elif string3 not in string2:
            print(string3, "is not in", string2)
    if command == 'r':
        rep = input("Enter the word you'd like to replace:")
        new = input("Enter your new word:")
        txt = string2
        if rep in string2:
            newnew= txt.replace(rep,new)
            print(newnew)
        else:
            print("Word not located in string.")
if command == 'q':
    print("Are you sure you want to quit the software? type Yes for confirmation.")
    choice = input(">")
    if choice == "yes" or "Yes":
        print("End of software.")


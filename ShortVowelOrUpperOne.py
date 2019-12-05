print( " Zahra Memar", '\n',"HW2",'\n',"September 17",'\n')

lower_casevowel=("u","a","e","i","o")
upper_casevowel=("U","A","E","I","O")

def AskForLetter():
    while True:
            letter=str(input("Please input a letter."))
            if letter=='quit':
                print(" You quit the program.")
                break
            elif len(letter)==1:
                if IsVowel(letter):
                    IsVowel("your input is a vowel letter")
            else:
                print("Error! please input A letter.")

def IsVowel(letter):
    if letter in lower_casevowel :
        print("Your letter ", letter, " is a vowel.")
        if IsLowerCaseVowel(letter):
            print("")
    elif letter in upper_casevowel:
        print("Your letter ", letter, " is a vowel.")
        if IsUpperCaseVowel(letter):
            print("")
    else:
        print("Please input a vowel letter")
    
def IsLowerCaseVowel(letter):
    if letter in lower_casevowel:
        print("And it is a lower case vowel.")

def IsUpperCaseVowel(letter):
    if letter in upper_casevowel:
        print("And it is an upper case vowel.")

def PrintIsVowel(letter):
    print("")
AskForLetter()

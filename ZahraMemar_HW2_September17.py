print( " Zahra Memar", '\n',"HW2",'\n',"September 17",'\n')

u='u'
a='a'
e='e'
i='i'
o='o'
U='U'
A='A'
E='E'
I='I'
O='O'
vowel=(u,a,e,i,o,U,A,E,I,O)
lower_casevowel=(u,a,e,i,o)
upper_casevowel=(U,A,E,I,O)

def AskForLetter():
    while True:
        try:
            letter=str(input("Please input a letter."))
            if letter=='quit':
                print(" You quit the program.")
                break
            elif len(letter)==1:
                if IsVowel(letter):
                    PrintIsVowel("your input is a letter")
                else:
                    PrintIsVowel("is not a vowel")
            else:
                print("Error! please input A letter.")
        except ValueError:
            print("Error! please input your letter as a string")
        else:
            print("**")

def IsVowel(letter):
    if letter in vowel:
        print("Your letter ", letter, " is a vowel.")
        if IsLowerCaseVowel(letter) or IsUpperCaseVowel(letter):
            print("")
        else:
            print("Error!")
        return True
    else:
        print("Error! your letter ", letter, " is not a vowel.Please input a vowel")
        return False
    
def IsLowerCaseVowel(letter):
    if letter in lower_casevowel:
        print("And it is a lower case vowel.")
        return True
    else:
        return False

def IsUpperCaseVowel(letter):
    if letter in upper_casevowel:
        print("And it is an upper case vowel.")
        return True
    else:
        return False

def PrintIsVowel(letter):
    print("")
AskForLetter()

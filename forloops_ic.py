def main():
    # problem0()
    # problem1()
    # problem3()
    # problem4()
    problem5()

'''
Print Loop
'''


def problem0():
    print("LOOP")

'''
Create a program that takes user input and prints the user input.
'''

def problem1():
    print(input("i'll repeat anything you say."))

'''
Create a program that takes user input in a while loop. 
If they enter ‘q’ or 0 (your choice), quit. 
Inside the loop print LOOP
'''


def problem3():
    user_input = input("gimme a word, sentence, anything!")

    for loop in user_input:
        print(loop)
        if loop == "q":
            print("loop!")
            break

'''
Create a program that takes user input in a while loop. 
If they enter 1, print ONE. 
If they enter 2, print TWO. 
If they enter 3 print 3. 
If they enter ‘q’ or 0 (your choice), quit. 
Else, print ERROR.
'''

def problem4():
    userInput = input("gimme a number between 1 and 3")
    while userInput != "q":
        if userInput == "1":
            print("ONE")
        elif userInput == "2":
            print("TWO")
        elif userInput == "3":
            print("3")
        else:
            print("THAT'S NOT RIGHT!")
        userInput = input("gimme a different one!")
'''
Create a program that takes user input. 
If they enter 1, call a function that prints IN FUNCTION 1. 
If they press 2, call a function that prints IN FUNCTION 2. 
If they press 3, call a function that prints IN FUNCTION 3. 
If they enter ‘q’ or 0 (your choice), quit. 
Else, print ERROR.
'''

def problem5():
    def print1():
        print("IN FUNCTION 1.")
    def print2():
        print("IN FUNCTION 2.")
    def print3():
        print("IN FUNCTION 3.")


    while(True):
        userInput = input("gimme a number between 1-3")
        if userInput == "1":
            print1()
        elif userInput == "2":
            print2()
        elif userInput == "3":
            print3()
        elif userInput == "q":
            break
        else:
            print("ERROR")


if __name__=='__main__':
    main()

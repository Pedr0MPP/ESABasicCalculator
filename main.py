import math



def basic_calculator():
    exp=input("Enter your expression: ")
    while True:
        try:
            print("Result to [",exp,"] = ", eval(exp))
            print("\n")
            print("---------------------------------------")
            print("Press R to restart Calculator or Press any key return to Menu!")
            read=input()
            if read == 'r' or read == 'R':
                exp=input("Enter your expression")
            else:
                print("Back to Menu\n")
                return menu()
        except Exception:
            print("Invalid Expression!!!")
            print("Press R to restart Calculator or Press any key to return to Menu! ")
            if read == 'r' or read == 'R':
                exp = input("Enter your expression: ")
            else:
                print("Back to Menu\n")
                return menu()


def powerCalculator(number, power):
    result = math.pow(number, power)
    return result

def rootCalculator(number, root):
    result=math.pow(number, 1/root)
    return result

def menu():
    print("Choose calculator:")
    print("1. Basic Calculator + - / * ")
    print("2. Power Calculator")
    print("3. Root Calculator")
    print("4. Quit!!")
    while(True):
        choice = int(input("Option -> "))
        if choice == 1:
            basic_calculator()
        elif choice == 2:
            print("Calculating power...")
            number = int(input("Number"))
            power = int(input("Power"))
            print(f"{power} of {number} is {powerCalculator(number, power)}")
        elif choice == 3:
            print("Calculating Root...")
            number = int(input("Number"))
            root = int(input("Root"))
            print(f"{root} of {number} is {rootCalculator(number,root)}")
        elif choice == 4:
            print("Quiting...")
            exit()
    else:
        print("Invalid choice")

print("***** ESA Caculator *****")
menu()

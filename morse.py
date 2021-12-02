
def translate(char):
    if char.lower() == 'q':
        morse = "--•-"
        return morse
    elif char.lower() == 'w':
        morse = "•--"
        return morse
    elif char.lower() == 'e':
        morse = "•"
        return morse
    elif char.lower() == 'r':
        morse = "•-•"
        return morse
    elif char.lower() == 't':
        morse = "-"
        return morse
    elif char.lower() == 'y':
        morse = "-•--"
        return morse
    elif char.lower() == 'u':
        morse = "••-"
        return morse
    elif char.lower() == 'i':
        morse = "••"
        return morse
    elif char.lower() == 'o':
        morse = "---"
        return morse
    elif char.lower() == 'p':
        morse = "•--•"
        return morse
    elif char.lower() == 'a':
        morse = "•-"
        return morse
    elif char.lower() == 's':
        morse = "•••"
        return morse
    elif char.lower() == 'd':
        morse = "-••"
        return morse
    elif char.lower() == 'f':
        morse = "••-•"
        return morse
    elif char.lower() == 'g':
        morse = "--•"
        return morse
    elif char.lower() == 'h':
        morse = "••••"
        return morse
    elif char.lower() == 'j':
        morse = "•---"
        return morse
    elif char.lower() == 'k':
        morse = "-•-"
        return morse
    elif char.lower() == 'l':
        morse = "•-••"
        return morse
    elif char.lower() == 'z':
        morse = "--••"
        return morse
    elif char.lower() == 'x':
        morse = "-••-"
        return morse
    elif char.lower() == 'c':
        morse = "-•-•"
        return morse
    elif char.lower() == 'v':
        morse = "•••-"
        return morse
    elif char.lower() == 'b':
        morse = "-•••"
        return morse
    elif char.lower() == 'n':
        morse = "-•"
        return morse
    elif char.lower() == 'm':
        morse = "--"
        return morse
    elif char == '1':
        morse = "•----"
        return morse
    elif char == '2':
        morse = "••---"
        return morse
    elif char == '3':
        morse = "•••--"
        return morse
    elif char == '4':
        morse = "••••-"
        return morse
    elif char == '5':
        morse = "•••••"
        return morse
    elif char == '6':
        morse = "-••••"
        return morse
    elif char == '7':
        morse = "--•••"
        return morse
    elif char == '8':
        morse = "---••"
        return morse
    elif char == '9':
        morse = "----•"
        return morse
    elif char == '0':
        morse = '-----'
        return morse
    elif char == ' ':
        morse = "   "
        return morse
    else:
        morse = ""
        return morse

def encode():
    while True:
        chars = getChars("Enter text to be encoded: ")
        code = []
        for j in chars:
            next = translate(j)
            code.append(next)
        new = ""
        for x in code:
            new += x
            new += ' '
        print(new)
        return


def getChars(text):
    list = []
    while True:
        try:
            phrase = str(input(text))
            for i in phrase:
                list.append(i)
            break
        except:
            print("Invalid characters, try again.")
    return list



def menu(options):
    choice = ""
    print(options)
    choice = input("Enter your choice: ")
    return choice


def main():
    print("Program Name")
    cont = "y"
    while cont.lower() == "y" or cont.lower() == "yes":
        selection = menu("1. Encode Morse\nE. Exit")
        if selection == "1":
            encode()
        elif selection == "e" or selection == "E":
            cont = "n"
        else:
            print("Wrong choice, try again.")


main()
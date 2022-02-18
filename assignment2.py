Size = int(input("What Size Game GoPy?"))
if Size < 3:
    print(" Please enter a valid number.")
    exit()
else:
    pass

liste = [i for i in range(Size * Size)]

def Board():
    spacing = str(Size**2)
    a = len(spacing)
    size1 = Size
    x = 0
    for i in range(int(Size)):
        for j in range(x, size1):
            print("{}".format(str(liste[j]).rjust(a)), end='  ')
        print()
        size1 = size1 + Size
        x = x + Size
Board()

def Player1():
    choice = int(input("Player1 turn --> "))
    if liste[choice] == 'X':
        print(" You have made this choice before.")
        Board()
        Player2()
    elif liste[choice] == 'O':
        print("The other player select this cell before.")
        Board()
        Player2()
    else:
        liste[choice] = 'X'
        Board()
        b = Winner()
        while b is False:
            Player2()
        exit()

def Player2():
    choice2 = int(input("Player2 turn --> "))
    if liste[choice2] == 'O':
        print("You have made this choice before")
        Board()
        Player1()
    elif liste[choice2] == 'X':
        print("The other player select this cell before")
        Board()
        Player1()
    else:
        liste[choice2] = 'O'
        Board()
        a = Winner()
        while a is False:
            Player1()
        exit()

def Winner():
    for i in range(Size):
        if len(set(liste[i * Size:(i + 1) * Size])) == 1:
            print("Winner: {}".format(liste[i*Size]))
            return True    #from left to right

    for i in range(Size):
        if len(set(liste[i: Size ** 2 - Size + i + 1:Size])) == 1:
            print("Winner: {}".format(liste[i]))   #from top to bottom
            return True

    if len(set(liste[0:len(liste):Size + 1])) == 1:
        print("Winner: {}".format(liste[0]))  #left-leaning cross
        return True

    if len(set(liste[Size - 1:len(liste) + 1 - Size:Size - 1])) == 1:
        print("Winner: {}".format(liste[Size-1]))  #right-leaning cross
        return True
    elif (int(Size**2) == liste.count("X") + liste.count("O")):
        print("No winner")   #if they draw
        exit()
    else:
        return False

Player1()


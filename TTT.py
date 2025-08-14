ans = "Y"
while ans == "Y":
    # created variables for design
    h = "|"
    g = "---------"

    lft = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # for not overputting
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # position list
    print("STARTING THE GAME")
    print("T | I | C")
    print(g)
    print("T | A | C")
    print(g)
    print("T | O | E")
    print("Welcome Players")
    # printing for position
    print(l[0], h, l[1], h, l[2])
    print(g)
    print(l[3], h, l[4], h, l[5])
    print(g)
    print(l[6], h, l[7], h, l[8])
    print("You have to play according to these positions")

    l = [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ]

    # main printing pattern
    print(l[0], h, l[1], h, l[2])
    print(g)
    print(l[3], h, l[4], h, l[5])
    print(g)
    print(l[6], h, l[7], h, l[8])
    print("Player 1 will use X and Player 2 will use O")

    i = 0
    n = " "
    s = ["X", "O"]

    while n in l:
        if (
            l[0] == l[1] == l[2] in s
            or l[3] == l[4] == l[5] in s
            or l[6] == l[7] == l[8] in s
        ):  # for rows
            print("You win")
            break
        elif l[2] == l[4] == l[6] in s or l[0] == l[4] == l[8] in s:  # for diagonals
            print("You win")
            break
        elif (
            l[0] == l[3] == l[6] in s
            or l[1] == l[4] == l[7] in s
            or l[2] == l[5] == l[8] in s
        ):  # for columns
            print("You win")
            break
        else:
            # alternating values evenodd method

            if i % 2 == 0:
                c1 = s[0]
            else:
                c1 = s[1]

            print("Player", c1, "turn")

            # user input for position
            pos = int(input("enter on which position you want to put your symbol"))

            # check inputy is in range or not
            if pos in lft:
                l[pos - 1] = c1
                lft.remove(pos)
                i = i + 1
            elif pos >= 9:
                print("please enter number from 1 to 9")
            elif pos not in lft:
                print("occupied")
            else:
                print("invalid input")

            # printed the new output
            print(l[0], h, l[1], h, l[2])
            print(g)
            print(l[3], h, l[4], h, l[5])
            print(g)
            print(l[6], h, l[7], h, l[8])
    if n not in l:
        print("Match Draw")
    print("Want to play again ? ")
    ans = input("Type Y for Yes or N for No")
print("GAME CLOSED")

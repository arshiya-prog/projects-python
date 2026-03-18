def calculate_love_score(name1, name2):
    name = name1 + name2
    name = name.lower()
    name = name.replace(" ", "")
    nm = list(name)

    T, R, U, E = 0, 0, 0, 0
    L, O, V = 0, 0, 0

    for char in nm:
        if char == "t":
            T += 1
        elif char == "r":
            R += 1
        elif char == "u":
            U += 1
        elif char == "e":
            E += 1
        elif char == "l":
            L += 1
        elif char == "o":
            O += 1
        elif char == "v":
            V += 1

    total_true = str(T+R+U+E)
    total_love = str(L+O+V+E)
    score = total_true + total_love

    print(f"T occurs {T} times")
    print(f"R occurs {R} times")
    print(f"U occurs {U} times")
    print(f"E occurs {E} times")
    print(f"Total = {total_true}\n")

    print(f"L occurs {L} times")
    print(f"O occurs {O} times")
    print(f"V occurs {V} times")
    print(f"E occurs {E} times")
    print(f"Total = {total_love}\n")

    return score

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

score = calculate_love_score(name1, name2)

print(f"Your love score is: {score}\n")

def main():

    case = 0
    counter = 0
    indicies = []

    with open("file.txt", "r") as f:
      while True:
            c = f.read(1)
            if not c: break
            counter = counter + 1
            print c
            print(counter)

            if case == 0:
                case = q0(c)
                continue
            elif case == 1:
                case = q1(c)
                continue
            elif case == 2:
                case = q2(c)
                continue
            elif case == 3:
                case = q3(c)
                continue
            elif case == 4:
                case = q4(c, counter-1, indicies)
                continue

    print(indicies)

def q0(c):
    if c == 'a':
        case = 1
    else:
        case = 0
    return case

def q1(c):
    if c == 'a':
        case = 1
    elif c == 'b':
        case = 2
    else:
        case = 0
    return case

def q2(c):
    if c == 'a':
        case = 3
    else:
        case = 0
    return case

def q3(c):
    if c == 'a':
        case = 1
    elif c == 'b':
        case = 4
    else:
        case = 0
    return case

def q4(c, counter, indicies):
    indicies.append(counter)
    if c == 'a':
        case = 3
    else:
        case = 0
    return case

main()

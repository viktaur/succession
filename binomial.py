import math

while True:
    print("")
    n0 = eval(input('(n0) Number of times that an experiment has resulted favorable: '))
    n = eval(input('(n) Number of times that an experiment has been made: '))

    p = (n0 + 1) / (n + 2)

    print('The probability that the next experiment results favorable is: ' + str(p) + ' or ' + str("{:.2%}".format(p)))  
    while True:
        i = input("Want to try again? [y/n]: ")
        if i.lower() == 'y':
            break
        elif i.lower() == 'n':
            break
        else:
            i = input("ERROR: Please introduce a valid argument: ")
            continue
    
    if i.lower() == 'y':
        continue
    elif i.lower() == 'n':
        break
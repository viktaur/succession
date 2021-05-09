import math

while True:
    print("Welcome! Please select one of the following:")
    print("")
    print("[1] Binomial distributions")
    print("[2] Sunrise problem")
    print("[3] Reviews optimizer")
    print("")

    while True:
        i = input("")
        if i == '1':
            import binomial
            break
        elif i == '2':
            import sunrise
            break
        if i == '3':
            import reviews
            break
        else:
            print('Please try again')
            
    m = input("Would you like to return to the main menu? [y/n]:" )
    if m.lower() == 'y':
        continue
    if m.lower() == 'n':
        break
            
while True:
    contestant_switches = input('Should the contestant switch? ')
    if contestant_switches.istitle():
        contestant_switches = contestant_switches.lower()
    if contestant_switches in {'yes', 'y'}: #yes 和 y是有的
        print('I keep in mind you want to switch.')
        break
    if contestant_switches in {'no', 'n','oN','nooooo!','No!'}:
        print("I keep in mind you don't want to switch.")
        break
    print('Your input is incorrect, try again.')

for 

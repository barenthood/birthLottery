import random, sys, time

worldPop = 7530000000
billionPop = 2153

oneOutOf = int(worldPop / billionPop)

def birthLottery():
            result = random.randint(0, oneOutOf)
            print('Calculating your results...')
            time.sleep(2)
            print('......')
            time.sleep(1)
            input('Results ready, press any key to view. ')
            if result == 3:
                print('Congratulations! You are officially part of the 1%.')
            else:
                print('Sorry! You are one of the myriad unlucky.')
            print('Try Again, y/n?')
            again = input('> ')
            if again == 'y':
                birthLottery()
            else:
                sys.exit()


def runLottery():
    while True:
        print('Run lottery simulation, y/n?')
        choice = input('> ')
        if choice == 'y':
            birthLottery()
        elif choice == 'n':
            print('Thank you goodbye')
            sys.exit()
        else:
            print('I didn\'t understand that, lets try again.')
            return

runLottery()
from random import randint
import time, sys, os

def lose():
    print('You ran out of guesses, I win')
    print('The number was', num)
    time.sleep(2)
    gameLoop()

def win():
    print('Well done, you got it in', goes)
    time.sleep(2)
    gameLoop()

def gameLoop():
    global goes
    global used
    global num
    goes = 0
    used = []
    os.system('clear')
    print('\nWelcome to Pkr\'s Guessing Game')
    try:
        limit = int(input('\nPick an upper limit to our guessing game?'))
        tries = int(input('How many guesses can you get it in?'))
        time.sleep(1)
        if tries < abs(limit /4):
            print('Someone feels lucky!')
        elif tries > abs((limit / 4) * 3):
            print('Huh, playing it safe!')
        else:
            print('Good luck!')
    except ValueError:
        print('This is a number guessing game remember!')
        time.sleep(2)
        gameLoop()
    except KeyboardInterrupt:
        print('\nExiting script')
        sys.exit()
    if tries > limit or limit < 2 or tries == 0:
        print('Let\'s try that again shall we.')
        time.sleep(2)
        gameLoop()
    else:
        num = (randint(1,limit))
        time.sleep(1)
        while True:
            if goes == tries:
                time.sleep(1)
                lose()
            else:
                try:
                    guess = int(input('Take a guess? '))
                    if guess in list(used):
                        time.sleep(1)
                        print('You\'ve already tried that!')
                        goes += 1
                    else:
                        n_num = abs(num - guess)
                        if guess == num:
                            goes += 1
                            time.sleep(1)
                            win()
                        elif guess <= num and n_num <= 5 and limit > 10:
                            goes += 1
                            used.append(guess)
                            print('Too low but your not far off!')
                        elif guess >= num and n_num <= 5 and limit > 10:
                            goes += 1
                            used.append(guess)
                            print('Too high but your not far off!')
                        elif guess < num:
                            goes += 1
                            used.append(guess)
                            print('Too low')
                        elif guess > num:
                            goes += 1
                            used.append(guess)
                            print('Too high')
                except ValueError:
                    print('This is a number guessing game remember!')
                    goes += 1
                    pass
                except KeyboardInterrupt:
                    print('\nExiting script')
                    sys.exit()
gameLoop()

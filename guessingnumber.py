while True:
    n = int(input('Guess the number: '))
    if n == 54:
        print('congratulations')
        break
    elif n > 54:
        print('too high')
        continue
    else:
        print('too low')
        continue
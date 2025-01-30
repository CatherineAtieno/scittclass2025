secret_number=(1, 10)
guess_count= 0
guess_limit = 3
while guess_count < guess_limit:
    guess= int(input('Guess: '))
    if guess == secret_number:
        print('congratulations you have won')
        break
    else:
        print('sorry, try again')
        


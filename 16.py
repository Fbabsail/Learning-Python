guess_count = 0
guess_limit = 3
seceret_number=7
while guess_count < guess_limit:
    guess=int(input('Guess: '))
    guess_count += 1
    if guess == seceret_number:
        print('You won!! ')
        break
else:
    print('You failed nigga')

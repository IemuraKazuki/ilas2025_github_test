import random

guess = int(input('guess='))
print('Your guess is', guess)
answer = random.randint(1, 100)
while guess != answer:
    if guess < answer:
        print('Too low')
    else:
        print('Too high')
    guess = int(input('guess='))
    print('Your next guess is', guess)
print('Good guess!')
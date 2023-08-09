import random


def code_generate():
    digits = list(range(10))
    random.shuffle(digits)
    num_to_guess = digits[:code_length]

    return num_to_guess


def code_compare(user_guess, com_code):
    if [int(n) for n in user_guess] == com_code:
        return 'Great'
    for num in range(code_length):
        if int(user_guess[num]) == com_code[num]:
            return 'Match'
        elif int(user_guess[num]) in com_code:
            return 'Close'


code_length = 3
attempts = 0
print('################################')
print('### ----- CODEBREAKER ------ ###')
print('### -- Nope--Close--Match -- ###')
print('################################')

print(f'Welcome to Code Breaker! Let\'s see if you can guess my {code_length} digit number!')
code_to_guess = code_generate()

print(f'Code has been generated, please guess a {code_length} digit number')
print('-' * 25)
print('Possible answers are:')
print('-' * 25)
print('Close: You\'ve guessed a correct number but in the wrong position\n\
Match: You\'ve guessed a correct number in the correct position\n\
Nope: You haven\'t guess any of the numbers correctly')
print('-' * 25)

while True:
    guess = input("What is your guess? ")
    attempts += 1
    if len(guess) != code_length:
        print(f'Please enter only {code_length} numbers!')
        continue

    answer = code_compare(guess, code_to_guess)

    if answer == 'Great':
        print(f'Great You did it! You break the code with in {attempts} attempts! The code was {guess}')
        break

    if not answer:
        print('Nope')
    else:
        print(answer)

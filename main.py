print('You can check if a number is prime or not using this tool.')
num = input('Please type the number that you want to check: ')
if float(num) % 1 == 0:
    print('Checking your number...')

    if int(num) < 2:
        statement = f'{num} is not a prime number.'
    elif int(num) == 2:
        statement = f'{num} is a prime number'
    else:
        is_prime = True
        for i in range(2, int(num)):
            if int(num) % i == 0:
                is_prime = False
                break
        if is_prime:
            statement = f'{num} is a prime number'
        else:
            statement = f'{num} is not a prime number'

else:
    statement = f'{num} is not an int, therefore {num} is not a prime number.'

print(statement)
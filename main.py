print('You can check if a number is prime or not using this tool.')
num = int(input('Please type the number that you want to check: '))

if num < 2:
    statement = f'{num} is not a prime number.'
elif num == 2:
    statement = f'{num} is a prime number'
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        statement = f'{num} is a prime number'
    else:
        statement = f'{num} is not a prime number'

print(statement)

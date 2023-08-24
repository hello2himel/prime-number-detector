print('You can check if a number is prime or not using this tool.')
num = int(input('Please type the number that you want to check: '))

numlist = range(2 , num)
statement = ''

for i in numlist:
    calculation = num % i

    if num < 2:
        statement = f'{num} is not a prime number.'
    elif num == 2:
        statement = f'{num} is a prime number'
    elif calculation == 0:
        statement = f'{num} is not a prime number'
        break
    else:
        statement = f'{num} is a prime number'

print(statement)

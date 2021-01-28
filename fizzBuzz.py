def fizzbuzz(n):
    list = []
    for number in range(1, n+1):
        if number % 3 == 0 and number % 5 == 0:
            number = 'FizzBuzz'
            list.append(number)
        elif number % 3  == 0:
            number = 'Fizz'
            list.append(number)
        elif number % 5 == 0:
            number = 'Buzz'
            list.append(number)
        else:
            list.append(number)
    return list

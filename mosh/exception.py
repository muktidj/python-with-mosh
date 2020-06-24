try:
    age = int(input('> '))
    risk = 2000 / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid Value')
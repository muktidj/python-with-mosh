# Looping Number
for angka in range(1, 11):
    print(angka)
print('done')

# Looping Strimg
for myName in 'Mukti':
    print(myName)
print("*" * 20)


# Looping in List
lists = ['The', 'Rain', 'In', 'Italy']
for list in lists:
    print(list)
print("*" * 20)

# Looping then Break
numbers = [1, 2, "", 4]
for number in numbers:
    if number == "":
        break
    print(number)
print('Loop is over')

print("*" * 20)
# Looping then Continue
alphabet = ['A', 'B', '', 'D']
for alphabets in alphabet:
    if alphabets == '':
        print('Lanjut')
        continue
    print(alphabets)
print('Loop is Over')

print("*" * 20)
# Nested Loop
# Outer Loop
for outer in ['First', 'Second', 'Thrid']:
    print(outer)
    # Inner Loop
    for inner in range(3):
        inner += 1
        print(inner)
print('its over')

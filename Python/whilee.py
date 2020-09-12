import random

counter = 65
while counter < 5:
    print(counter)
    print(str(counter) + "=" + chr(counter))
    counter += 1
print('All Done')

# Break And Continue
print('odd random')
hitung = 0
while hitung < 50:
    angka = random.randint(1, 100)
    if int(angka / 5) == (angka / 5):
        # if it's an even number, don't print itu.
        break
        # continue
    # otherwisw, if it's odd, print it and increment the counter
    print(angka)
    hitung += 1
print('Done')

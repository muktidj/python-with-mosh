sun = 'down'
if sun == 'down':
    print("Good Night")
print("i'am here!")

print("*" * 70)

sun = 'up'
if sun == 'down':
    print('Night')
print('Morning')

print("*" * 70)

total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total : ${total:.2f}")

age = 21
if age < 15:
    beverage = "Milk"
elif age > 18 and age < 80:
    beverage = "beer"
else:
    beverage = 'Juice'


print("Have a " + beverage)

people = {
 'htanaka': 'Haru Tanaka',
 'ppatel': 'Priya Patel',
 'bagarcia': 'Benjamin Alberto Garcia',
 'zmin': 'Zhang Min',
 'afarooqi': 'Ayesha Farooqi',
 'hajackson': 'Hanna Jackson',
 'papatel': 'Pratyush Aarav Patel',
 'hrjackson': 'Henry Jackson'
}
# person = 'zmin'
# print(people[person])
print(people['papatel'])
print(len(people))
# Seeing whether a key exists in dictionary
print('zmin' in people)
# Getting data with get
# print(people.get(person))
# changing the value-key
print(people.get('hrjackson'))
people['hrjackson'] = 'Henry Jackson Smith'
print(people.get('hrjackson'))
# Adding or changing dictionary data
people.update({'smaulanti': 'Suci Maulanti'})
print('smaulanti' in people)

# Removing data in dictionary
del people['zmin']

# looping in the dictionary
for person in people.keys():
    print(person + " = " + people[person])

for person in people.values():
    print(person)

for key, value in people.items():
    print(key, " = ", value)

print("=" * 70)

product = {
    'name': 'car',
    'unit_price': 112.99,
    'taxable': 'true',
    'in_stock': 5,
    'colors': ['red', 'black', 'white']
}

print('Name: ', product['name'])
print('Price: ', f"${product['unit_price']:.2f}")
print('taxable: ', product['taxable'])
print('stock: ', product['in_stock'])
print('Colors: ')
for color in product['colors']:
    print(" " * 10 + color)

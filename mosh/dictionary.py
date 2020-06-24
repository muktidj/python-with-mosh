customers = {
    "name" : "Ayu Retno",
    "Age"  : 22,
    "is_verifed" : True
}
customers["name"] = "Ayu Retno Mukti"
print(customers['name'])

print(10 * "=")

phone = input("Phone: ")
digits_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "Four"
}
output = ""
for ch in phone:
    output+= digits_mapping.get(ch, "!") + " "
print(output)
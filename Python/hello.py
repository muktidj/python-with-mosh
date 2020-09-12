first_name = "Mukti"
middle_name = "DWI"
last_name = "Jatmoko"
fullname = first_name + " " + middle_name + " " + last_name
print(fullname)

print("=" * 50)

word = "lorem ipsum is"

print("A" in word)
print("A" not in word)
print(word[2:5])
print(ord("B"))  # ASCII

print("=" * 50)

unitPrice = 70000
quantity = 30
# print(f" Subtotal: Rp {unitPrice * quantity:,}")

print("=" * 50)


def friction(sales_tax):
    exercise = f"{sales_tax:.1%}"
    result = "$" + exercise
    final_result = f"""
    Result: {result:>2}
    """
    print(final_result)


# friction(0.065)

user1 = "Alberto"
user2 = "Babs"
user3 = "Carlos"
output = f"{user1} \n{user2} \n{user3}"
# print(output)

print("=" * 50)

angka = 8
print(bin(angka))
print(oct(angka))
print(hex(angka))

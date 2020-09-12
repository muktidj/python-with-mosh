names = ['Adams', 'Ma', 'mail', 'diMeola', 'Zandusky']
names.sort(key=lambda s: s.lower())
print(names)

currency = lambda n: f"${n:,.2f}"
percent = lambda p: f"${p:.1%}"

# Test Currency
print(currency(99))
print(currency(1234134142134322))

# Test Percent
print(percent(0.075))
print(percent(0.5))

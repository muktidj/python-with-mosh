def hello(fname, lname, datestring=''):
    msg = "Hello " + fname + " " + lname
    if len(datestring) > 0:
        msg += " You Mentioned " + datestring
    print(msg)


hello('Mukti', 'DJ', '17-08-2019')
first_name = 'Paolo'
last_name = 'Maldini'
current_date = '17 Agustus 2020'
hello('Mukti', 'DJ')
hello(fname=first_name, lname=last_name, datestring=current_date)

print("=" * 40)


# passing multiple values in a list
def alphabetize(original_list=[]):
    # Inside the function make a working copy of the list passed in.
    sorted_list = original_list.copy()
    # Sort the working copy.
    sorted_list.sort()
    # Make a new empty string for output
    final_list = ''
    # Loop through sorted list and append name and comma and space.
    for name in sorted_list:
        final_list += name + ', '
    # Knock of last comma space if final list is long enough
    final_list = final_list[:-2]
    # Print the alphabetized list.
    print(final_list)


names = ['Schrepfer', 'Maier', 'Santiago', 'Adams']
alphabetize(names)


# Passing in an arbitrary number of arguments
def sorter(*args):
    newlist = list(args)
    newlist.sort()
    print(newlist)


sorter(1, 0.212, -112, 221111)

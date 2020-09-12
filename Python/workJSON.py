import json

# This is the Excel data (no keys)
fileName = 'exercise_.json'
# Open the file (standard file open stuff)
with open(fileName, 'r', encoding='utf-8', newline='') as file:
    # Load the whole json file into an object named people
    people = json.load(file)
    for loop in people:
        print(loop['Full Name'], loop['Birth Year'], loop['Date Joined'], loop['Is Active'], loop['Balance'])

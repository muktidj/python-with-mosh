import csv

with open('new-names-2.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print(csv_reader)

    # with open('new_names_3.csv', 'w') as new_file:
    #     fieldnames = ['first_name', 'last_name']

    #     csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

    #     csv_writer.writeheader()

    #     for line in csv_reader:
    #         del line['email']
    #         csv_writer.writerows(line)


# import csv

# with open('new-names-2.csv', 'r') as csv_file:
#     # csv_reader = csv.reader(csv_file)
#     # Dictionary
#     csv_reader = csv.DictReader(csv_file)
#     # Heading not include print
#     # next(csv_reader)

#     # for i in csv_reader:
#     #     print(i['last_name'])

#     with open('new-names-3.csv', 'w', newline='') as new_file:
#         fieldnames = ["first_name", "last_name", "email"]

#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

#         csv_writer.writeheader()

#         for line in csv_reader:
#             del line['email']
#             csv_writer.writerows(line)

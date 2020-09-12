with open('Vocab-book.txt') as var:
    # fileContext = var.read()
    # fileContext = var.readline()
    # fileContext = var.readlines()
    # Looping
    for fileContext in var.readlines():
        # Double Space
        # print(fileContext)
        # one space
        print(fileContext, end='')

print('the file is closed', var.closed)

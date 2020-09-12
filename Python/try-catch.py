try:
    # theFile = open('cell-basis.csv')
    theFile = open('cell-basis.xlsx')
    print(theFile.name)
except Exception:
    print('Sorry, I dont see a file name cell-basis.xlsx here')

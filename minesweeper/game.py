from field import *

def menu():
    r = int(input("number of rows: "))
    c = int(input("number of columns: "))
    m = int(input("number of mines: "))
    return field.createField(r,c,m)

minesweeper = menu()
print(minesweeper)

    




from random import randint

def createField(rows, columns, mines):
    fields = [["."]*columns]*rows
    for i in range(mines):
        fields[randint(0, rows-1)][randint(0, columns-1)] = "*"

    for i in range(rows):
        for j in range(columns):
            print(fields[i][j])

    return fields

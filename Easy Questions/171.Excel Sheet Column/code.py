def titleNumber(columnTitle):
    col_number=0
    for char in columnTitle:
        col_number=col_number*26+ord(char)-65+1
    return col_number





columnTitle="ZY"
print(titleNumber(columnTitle))

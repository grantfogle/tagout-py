import camelot
import tkinter
print('cats')
allTables = camelot.read_pdf("../../../../2021ElkDrawRecap-1.pdf", pages="all")

print(allTables[2])
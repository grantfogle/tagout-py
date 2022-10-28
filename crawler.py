import camelot
import tkinter
print('cats')
df = camelot.read_pdf("../../../../2021ElkDrawRecap-1.pdf", pages="all")

print(df[2])
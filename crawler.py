import tabula

df = tabula.read_pdf("../../../../2021ElkDrawRecap-1.pdf", pages="all")

print(df)
import pandas as pd

filename = "stat_104102.xlsx"
sheet_name = "Sheet0"
book = pd.read_excel(filename, sheet_name=sheet_name, header=1)

book = book.sort_values(by='2015', ascending=False)
print(book)
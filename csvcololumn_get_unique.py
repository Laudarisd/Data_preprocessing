import pandas as pd
import csv


df = pd.read_csv("./test.csv")
unique_class = df['class_name'].unique()
s = pd.Series(unique_class)
# with open('unique_clss.csv', "w") as myfile:
#     wr = csv.writer(myfile)
#     wr.writerow(unique_class)

s.to_csv('unique.csv')

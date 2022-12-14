import csv
import pandas as pd

df = pd.read_csv('sb-nutrition-drinks.csv')

for line in df:
    print(line)
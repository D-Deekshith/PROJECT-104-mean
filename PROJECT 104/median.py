from statistics import median
import pandas as pd
df=pd.read_csv("data.csv")
data=df['Weight(Pounds)'].to_list()

lengthHeight = len(data)

data.sort()

median1 = data[lengthHeight//2]
median2 = data[lengthHeight//2 - 1]
median = (median1 + median2)/2

print(median)
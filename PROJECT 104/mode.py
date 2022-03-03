from collections import Counter
import pandas as pd
df=pd.read_csv("data.csv")
data=df['Weight(Pounds)'].to_list()
lengthWeight = len(data)
val = Counter(data)
findMode = dict(val)
mode = [i for i, v in findMode.items() if v == max(list(val.values()))]
if len(mode) == data:
    findMode = "The group of number do not have any mode"
else:
    findMode = "The mode of a number is / are: " + ', '.join(map(str, mode))
print(findMode)
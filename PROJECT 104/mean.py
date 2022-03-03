import pandas as pd
df=pd.read_csv("data.csv")
data=df['Weight(Pounds)'].to_list()
sum = 0
for weight in data:
    sum = sum+weight

lengthWeight = len(data)

mean = sum/lengthWeight

print(mean)
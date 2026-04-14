import pandas

df=pandas.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
x=df.groupby('country')
for name, group in x:
    print(name)
    # print(group.head())

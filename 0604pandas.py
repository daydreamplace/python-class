import pandas as pd

df = pd.read_csv('/Users/eden/Downloads/ex-data/data2.csv')
# df = pd.read_json('/Users/eden/Downloads/ex-data/data.json')
# print(df.to_string())
# pd.options.display.max_rows = 200
# print(df)

# print(df.head(10))  # 처음 10개 행 출력
# print(df.tail(10))  # 마지막 10개 행 출력
# print(df.sample(10))  # 무작위로 10개 행 출력


# x = df["Calories"].mean()
# df.fillna({"Calories": x}, inplace = True)

# df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# df.loc[7, 'Duration'] = 45

#----------
df = pd.read_csv('/Users/eden/Downloads/ex-data/data2.csv')

# for x in df.index:
#     if df.loc[x, 'Duration'] > 120:
#         df.loc[x, 'Duration'] = 30

df.drop_duplicates(inplace = True)

print(df.to_string())


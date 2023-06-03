import pandas as pd

df = pd.read_csv('l.csv')

# print(df.head())

# print(df.columns)

# print(df.size)

# statuses = []
# country = ""
# for index, row in df.iterrows():
#     if country != row['Country']:
#         country = row['Country']
#         statuses.append(row['Status'])
#         if row['Status'] == 'Developed': print("developed country ", country)

# print(len([s for s in statuses if s=="Developing"]), len([s for s in statuses if s=="Developing"])/len(statuses), "%", "developing")
# print(len([s for s in statuses if s=="Developed"]), len([s for s in statuses if s=="Developed"])/len(statuses), "%", "developoed")

# counter = 0
# for index, row in df.iterrows():
#     if row['Income composition of resources'] < 0.1:
#         print(row['Country'])
#         counter += 1

# print(counter)

# for index, row in df.iterrows():
#     if row['Country'] in ['India', 'China', 'Angola']:
#         print(row['Country'], row[' BMI '])

# ---------------------------

# country = ""
# for index, row in df.iterrows():
#     if country != row['Country']:
#         country = row['Country']
#     for c in df.columns:
#         if row[c] != 0 and type(row[c]) in [int, float]:
#             while ((df.iloc[index-1]['Country'] == row['Country'] and df.iloc[index-1][c] >= 8*df.iloc[index][c]) or
#                    (index != 2937 and df.iloc[index+1]['Country'] == row['Country'] and df.iloc[index+1][c] >= 8*df.iloc[index][c])):
#                 # df.iloc[index][c] *= 10
#                 df.loc[index, c] = df.iloc[index][c]*10
#                 #print(df.iloc[index][c])
#     print(index)

# df.to_csv("l_fixed.csv", index=False)

country = ""
for index, row in df.iterrows():
    if country != row['Country']:
        country = row['Country']
    for c in df.columns:
        if type(row[c]) in [int, float]:
            while ((df.iloc[index-1]['Country'] == row['Country'] and df.iloc[index-1][c] >= 8*df.iloc[index][c]) or
                   (index != 2937 and df.iloc[index+1]['Country'] == row['Country'] and df.iloc[index+1][c] >= 8*df.iloc[index][c])):
                # df.iloc[index][c] *= 10
                if row[c] == 0:
                    df.loc[index, c] = None
                    break
                df.loc[index, c] = df.iloc[index][c]*10
                #print(df.iloc[index][c])
    print(index)

df.to_csv("l_fixed2.csv", index=False)
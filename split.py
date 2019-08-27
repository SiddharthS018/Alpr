import pandas as pd

im = pd.read_csv('data.csv')
i=0
for data in im['Acorn']:
    print(data)
    if i==5: break


# test=pd.DataFrame(set(im['Acorn']))
# print(test)
# # pd.to_csv(pd.DataFrame(set(im['ACRON-A'])))
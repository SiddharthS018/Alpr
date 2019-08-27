import pandas as pd

dataset = pd.read_csv('E:\\TcS\\HumaIn\\SmartAnalysis\\data.csv')
#print(dataset)
#print(dataset.head())
#houses = set(dataset['Acorn'])
#print(houses)

# acorna=[]
# for index,row in dataset.iterrows():
#     if row[4]=='ACORN-N':
#       acorna.append(list(row))
# pd.DataFrame(acorna).to_csv("acorn_n.csv",header=None,index=None)

tot = pd.read_csv('E:\\TcS\\HumaIn\\SmartAnalysis\\acorn_a.csv')
#print(tot.sum(axis = 1, skipna = True))
# a=0
for index,row in tot.iterrows():
    
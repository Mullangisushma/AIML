

""" Find-S Algorithm """

import csv
num_attributes=6
a=[]
print("The training dataset is")
csvfile=open('1.csv','r')
reader=csv.reader(csvfile)
for row in reader:
    a.append(row)
    print(row)
print("The initial values of the hypothesis is")
hypothesis=[0]*num_attributes
print(hypothesis)
for j in range(0,num_attributes):
    hypothesis[j]=a[0][j]
for i in range(0,len(a)):
    if(a[i][num_attributes]=='Yes'):
        for j in range(0,num_attributes):
            if(a[i][j]!=hypothesis[j]):
                hypothesis[j]='?'
            else:
                hypothesis[j]=a[i][j]
    print("for training instance ",i,"the hypothesis is",hypothesis)
print("The maximally specific hypothesis is",hypothesis)

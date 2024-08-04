import csv
a=[]
csvfile=open('1.csv','r')
reader=csv.reader(csvfile)
for row in reader:
    a.append(row)
    print(row)
num_att=len(a[0])-1
print("Initial hypothesis is ")
S=['0']*num_att
G=['?']*num_att
print("The most specific ",S)
print("The most general ",G)
for j in range(0,num_att):
    S[j]=a[0][j]
print("The candidate algorithm\n")
temp=[]
for i in range(0,len(a)):
    if(a[i][num_att]=='Yes'):
        for j in range(0,num_att):
            if(a[i][j]!=S[j]):
                S[j]='?'
        for j in range(0,num_att):
            for k in range(1,len(temp)):
                if temp[k][j]!='?' and temp[k][j]!=S[j]:
                    del temp[k]
    print("For instance {} the hypothesis is S{}".format(i+1,S))
    if len(temp)==0:
        print("For instance {} the hypotheis is G{}".format(i+1,G))
    else:
        print("For instance {} the hypotheis is G{}".format(i+1,temp))
    if(a[i][num_att]=='No'):
        for j in range(0,num_att):
            if S[j]!=a[i][j] and S[j]!='?':
                G[j]=S[j]
                temp.append(G)
                G=['?']*num_att
        print("For Instances {} the hypothesis is S{}".format(i+1,S))
        print("For Instances {} the hypothesis is G{}".format(i+1,temp))
        
        
        
        
        
        
        
        
        
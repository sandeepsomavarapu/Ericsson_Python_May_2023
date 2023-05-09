import csv
f=open("employees.csv",'r')
r=csv.reader(f) #returns csv reader object
data=list(r)
 #print(data)
for line in data:
    for word in line:
        print(word,"\t",end='')
    print("\n") 
print("") 
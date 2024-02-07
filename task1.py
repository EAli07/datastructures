names = []
flag=0
max = int(input("enter the max number of elements: "))
for j in range(0, max):
    record = input("enter a name for the record: ")
    names.append(record)
    
print(names)
element = input("which record do you want to check?: ")

for i in names:
    if(i==element):
        print("element found at", names[0][i])
        flag=1
        break
if (flag==0):
    print("element not found")

#ws1,t1,q2
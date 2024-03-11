n=int(input("enter number"))
a=1
b=1
count=2
print(a,end=" ")
print(b,end=" ")
while(count<n):
    temp=a+b
    print(temp,end=" ")
    count+=1
    a=b
    b=temp

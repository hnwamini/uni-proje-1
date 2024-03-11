x=int(input("mojodi khod ra elam konid"))
y=int(input("darsad sood ra vared konid"))
count=0
while count<12:
    x=x+(x*(y/100))
    count+=1
    print(x)
num=int(input('enter how many number u want to display'))
x=0
y=1
c=2
print('fibonacci sequence is:')
print(x)
print(y)
while(c<num):
    z=x+y
    print(z)
    x=y
    y=z
    c+=1

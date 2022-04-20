a=int(input())
b=a//2
c=0
for i in range (b):
    if (i*i==a):
         c=c+1
if(c!=0):
    print("True")
else:
    print("False")
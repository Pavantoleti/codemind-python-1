a=int(input())
for i in range(a):
    for j in range(a-(i+1)):
        print(" ",end="")
    for j in range(i*2+1):
        print(i+1,end="")
    print(""),
a=int(input())
arr=list(map(int,input().split()))
for i in range(0,a,2):
    l=arr[i]
    p=arr[i+1]
    for i in range(l):
        print(p,end=" ")
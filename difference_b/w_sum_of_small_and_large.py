a=input()
arr=list(a.split())
l=s=0
d=g=0
for i in arr:
    l=0
    s=10000
    for j in i:
        if ord(j)>l:
            l=ord(j)
        if ord(j)<s:
            s=ord(j)
    d+=l
    g+=s
print(d-g)
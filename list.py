L=[1,2,3,4,5]
L1=[]
n=int(input("Enter a Number:"))
for i in range(0,len(L)):
    if (L[i]==n):
        m=n**2
        L1.append(m)
    else:
        L1.append(L[i])

print("Before List:",L)
print("After list:",L1)

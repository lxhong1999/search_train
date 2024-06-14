def LS(ar,n):
    for i in range(len(ar)):
        if n == ar[i]:
            return i

a = [1,3,5,7,9]
print(LS(a,9))
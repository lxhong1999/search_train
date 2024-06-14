def BS(ar, n):
    left = 0
    right = len(ar) - 1
    while (left <= right):
        mid = left+(right-left)//2
        if n == ar[mid]:
            return mid
        elif n>ar[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1

a = [1,3,5,7,9]
print(BS(a,9))
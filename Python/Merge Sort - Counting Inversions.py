#https://www.hackerrank.com/challenges/ctci-merge-sort/problem

def merge(arr, x, y):
    i, j, k = 0, 0, 0
    s = 0
    left_len, right_len = len(x), len(y)
    while i < left_len and j < right_len:
        if x[i] > y[j]:
            arr[k] = y[j]
            j, k = j + 1, k + 1
            s += len(x) - i
        else:
            arr[k] = x[i]
            i, k = i + 1, k + 1

    while i < left_len:
        arr[k] = x[i]
        i, k = i + 1, k + 1

    while j < right_len:
        arr[k] = y[j]
        j, k = j + 1, k + 1

    return s

def countInversions(arr):
    if len(arr) <= 1:
        return 0
    m = len(arr) // 2
    lh = arr[:m]
    rh = arr[m:]

    s = countInversions(lh) + countInversions(rh) + merge(arr, lh, rh)
    return s


t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

print(countInversions(arr))

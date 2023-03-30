def mLastElement(arr, m) -> int:
    n = len(arr)
    if m > n:
        return None
    get_m = n - m
    ret = arr[get_m]
    return ret


m = int(input())
arr = list(map(int, input().split(" ")))
if mLastElement(arr, m) == None:
    print("NIL")
else:
    print(mLastElement(arr, m))
import time

st = time.time()

lt = [11,12,13,14,15,16,1,2,3,4,5,6,7,8,9,10]
lt_2 = []
def left_less(arr, lo, hi, query):
    while lo <= hi:
        mid = (lo + hi)//2
        if arr[mid] == query:
            return mid
        else:
            lo = mid + 1     
def right_big(arr, lo, hi, query):
    while lo <= hi:
        mid = (lo + hi)//2
        if arr[mid] == query:
            return mid
        elif arr[mid] > query:
            hi = mid - 1
        elif arr[mid] < query:
            lo = mid + 1
def left_big(arr, lo, hi, query):
    while lo <= hi:
        mid = (lo + hi)//2
        if arr[mid] == query:
            return mid
        elif arr[mid] > query:
            hi = mid - 1
        elif arr[mid] < query:
            lo = mid + 1
def src_bin(arr, query):
    if len(arr) == 0:
        return -1
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi)//2
        if arr[mid] == query:
            return mid
        elif query < arr[mid] and query < arr[lo]:
            hi = mid - 1
            res = left_less(arr, lo, hi, query)
            return res 
        elif query > arr[mid] and query <= arr[hi]:
            lo = mid + 1
            res = right_big(arr, lo, hi, query)
            return res
        elif query > arr[mid] and query > arr[hi]:
            hi = mid - 1
            res = left_big(arr, lo, hi, query)
            return res
    return -1
        
print(src_bin(lt_2, 10))

et = time.time()

print(et - st)
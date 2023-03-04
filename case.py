lt = [1,1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,6,7]

def first_el(arr,query,mid):
    mid_el = arr[mid]
    
    if mid_el == query:
        if mid - 1 >= 0 and arr[mid - 1] == query:
            return "left"
        else:
            return "found"
    elif mid_el < query:
        return "right"
    elif mid_el > query:
        return "left"

def bin_s(arr, query):
    lo = 0
    hi = len(lt) - 1
    
    while lo <= hi:
        mid = (lo + hi)//2
        
        res_first = first_el(arr, query, mid)
                
        if res_first == "found":
            return mid
        elif res_first == "right":
            lo = mid + 1
        elif res_first == "left":
            hi = mid - 1
            
            
def last_el(arr, query, mid):
    mid_el = arr[mid]
    
    if mid_el == query:
        if mid != len(arr) - 1 and arr[mid + 1] == query:
            return "right"
        else:
            return "found"
    elif mid_el < query:
        return "right"
    elif mid_el > query:
        return "left"

def bin_l(arr, query):
    lo = 0
    hi = len(lt) - 1
    
    while lo <= hi:
        mid = (lo + hi)//2
        
        res_last = last_el(arr, query, mid)
                
        if res_last == "found":
            return mid
        elif res_last == "right":
            lo = mid + 1
        elif res_last == "left":
            hi = mid - 1

print(len(lt) - 1)

first = bin_s(lt,4)
last = bin_l(lt,4)

print(f"first index =  {first}, last index = {last}")
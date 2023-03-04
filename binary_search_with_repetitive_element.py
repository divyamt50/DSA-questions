lt = [10,9,9,9,8,8,7,6,5,5,5,4,4,3,2,2,2,1]

def test_location(arr,query,mid):
    mid_number = arr[mid]
    
    if mid_number == query:
        if mid - 1 > 0 and arr[mid - 1] == query:
            return "left"
        else:
            return "found"
    
    elif mid_number < query:
        return "left"
    elif mid_number > query:
        return "right"

def find_index(arr,query):
    if len(arr) == 0:
        return -1 
    low = 0
    hi = len(arr) - 1
    
    
    while low <= hi:
        mid = (low + hi) // 2
        
        result = test_location(arr,query,mid)
        
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            low = mid + 1
    
    return -1

print(find_index(lt,10))
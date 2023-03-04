lt = [12,11,10,9,8,7,6,5,4,3,2,1]

def find_index(in_list, query):
    if len(in_list) == 0:
        return -1
    low = 0
    hi = len(in_list) - 1
    
    #print(low, hi , mid) 
    
    while low <= hi:
        mid = (low + hi) // 2
        mid_number = in_list[mid]

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            low = mid + 1
        
    return -1
        
print(find_index(lt,4))
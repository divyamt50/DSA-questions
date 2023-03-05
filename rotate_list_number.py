lt = [1,2,3,4]
r_count = 0

def rotation(arr, obj):
    global r_count
    while r_count < obj:
        r_count += 1
        arr.insert(0,lt[len(lt) - 1])
        arr.pop(len(lt) - 1)
    
    return arr
    
print(rotation(lt,3))
print(r_count)
# start = 0
# end = len(lt) - 1
# rotation_count = 0
# lt_sec = []

# def rotate():
#     lt_sec.append(lt[(len(lt) - 1)])
#     #lt.remove(lt[len(lt) - 1])
#     for i in range(len(lt) - 1):
#         lt_sec.append(lt[i])
#     global rotation_count
#     rotation_count += 1
        
# rotate()
# print(lt_sec)
# print(rotation_count)
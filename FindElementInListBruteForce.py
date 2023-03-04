lt = [12,11,10,9,8,7,6,5,4,3,2,1]

def findElement(input_list, user_query):
    if len(input_list) == 0:
        return -1
    for index in range(len(input_list)):
        if input_list[index] == user_query:
            return index
    return -1

print(findElement(lt, 1))
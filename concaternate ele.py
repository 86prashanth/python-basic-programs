def concatenate_list_data(list):
    result=''
    for element in list:
        result+= str(element)
    return result
print(concatenate_list_data([2,4,5,6]))
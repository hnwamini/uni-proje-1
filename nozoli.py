def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid=len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

#لیست مورد نظر 
my_list = [12, 5, 7, 10, 3, 8, 15]

sorted_list = merge_sort(my_list)
print("list-nozoli", sorted_list)
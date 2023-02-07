



def remove_value(ordered_array: [int]) -> [int]:
    front_pointer = 1
    back_pointer = 0
    while front_pointer < len(ordered_array) - 1:
        if ordered_array[back_pointer] == ordered_array[front_pointer]:
            ordered_array.pop(back_pointer)
        else:
            front_pointer += 1
            back_pointer += 1
    if len(ordered_array) > 1:
        if ordered_array[len(ordered_array) - 1] == ordered_array[len(ordered_array) - 2]:
            ordered_array.pop(len(ordered_array) - 1)
    return ordered_array

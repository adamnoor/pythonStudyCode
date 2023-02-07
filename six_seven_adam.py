def find_nth_look_say(location: int) -> str:
    user_index = location - 1
    if user_index == 0:
        return "1"
    current_number = "11"
    current_index = 0
    while current_index < user_index - 1:
        current_number = create_counted(current_number)
        current_index += 1
    return current_number


def create_counted(num: str) -> str:
    number = num
    length = len(num)
    index_front = 0
    index_back = 1
    new_value = ""
    count = 1

    while length > index_back:
        if number[index_front] == number[index_back]:
            count += 1
            index_back += 1
            if index_back >= length:
                new_value = new_value + str(count) + number[index_front]

        else:
            new_value = new_value + str(count) + number[index_front]
            index_front = index_back
            index_back = index_front + 1
            count = 1

    if number[length - 1] != number[length - 2]:
        new_value = new_value + "1" + number[index_front]

    return new_value

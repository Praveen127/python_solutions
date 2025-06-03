def check_order(first_string, second_string):
    chars_index_tuple_list = []
    char_freqency_dict = {}
    for char in list(second_string):
        if char not in char_freqency_dict.keys():
            char_freqency_dict[char] = 1
        else:
            char_freqency_dict[char] += 1
    print(char_freqency_dict)
    char_org_count = char_freqency_dict.copy()
    char_skip_count = char_freqency_dict.copy()
    for key in char_skip_count:
        char_skip_count[key] = 0
    for char in list(second_string):
        if char not in list(first_string):
            return False
    for char in list(second_string):
        for i in range(len(first_string)):
            # print(char, first_string[i])
            if char == first_string[i]:
                if (char in char_freqency_dict.keys()):
                    if (char_skip_count[char] == 0):
                        chars_index_tuple_list.append((char, i))
                        char_freqency_dict[char] -= 1
                        char_skip_count[char] = char_org_count[char] - char_freqency_dict[char]
                        break
                    else:
                        char_skip_count[char] -= 1
                else:
                    chars_index_tuple_list.append((char, i))
                    break
    print(chars_index_tuple_list)
    index_list = [value for key, value in chars_index_tuple_list]
    print(index_list)
    previous = -1
    current = 0
    for i in list(index_list):
        # print(i,previous)
        if i < previous:
            return False
        previous = i

    return True


if __name__ == "__main__":
    str1 = "sddhncksdlliivvsdyyssaa"
    str2 = "sddcsiivya"
    print(check_order(str1, str2))

def check_order(first, second):
    chars_list = []
    char_dict = {}
    for char in list(second):
        if char not in char_dict.keys():
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    print(char_dict)
    char_org_count = char_dict.copy()
    char_skip_count = char_dict.copy()
    for key in char_skip_count:
        char_skip_count[key] = 0
    for char in list(second):
        for i in range(len(first)):
            #print(char, first[i])
            if char == first[i]:
                if(char in char_dict.keys()):
                    if(char_skip_count[char] == 0):
                        chars_list.append((char,i))
                        char_dict[char] -= 1
                        char_skip_count[char] = char_org_count[char] - char_dict[char]
                        break
                    else:
                        char_skip_count[char] -= 1
                else:
                    chars_list.append((char, i))
                    break
    print(chars_list)
    index_list = [value for key, value in chars_list]
    print(index_list)
    previous = -1
    current = 0
    for i in list(index_list):
        #print(i,previous)
        if i < previous:
            return False
        previous = i

    return True

str1 = "sddhncksdlliivvsdyyssaa"
str2 = "sddcsiivya"
print(check_order(str1,str2))













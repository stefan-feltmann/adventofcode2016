__author__ = 'stefan'

def decompress(compressed):
    decompress_num = False
    finding_copy_info = False
    copying_length = False
    temp = ""
    copy_length = 0
    copy_num = 0
    temp_num = ""
    output_array = []
    for i in compressed:
        if not decompress_num:
            copy_num = 1
            if i == '(':
                output_array.append((1, temp))
                temp = ""
                decompress_num = True
                copying_length = True
                finding_copy_info = True
            else:
                temp += i
        elif finding_copy_info:
            if copying_length:
                if i != 'x':
                    temp_num += i
                else:
                    copy_length = int(temp_num) - 1
                    temp_num = ''
                    copying_length = False
            else:
                if i != ')':
                    temp_num += i
                else:
                    copy_num = int(temp_num)

                    temp_num = ''
                    finding_copy_info = False
        else:
            temp += i
            if copy_length == 0:
                output_array.append((copy_num, temp))
                decompress_num = False
                copying_length = False
                finding_copy_info = False
                copy_num = 0
                temp = ''
            copy_length -= 1
    output_string = ''
    output_array.append((copy_num, temp))
    for i in output_array:
        for j in range(0, i[0]):
            output_string += i[1]
    # print output_array
    print output_string
    print len(output_string)

def decompressV2(compressed, int_num=0):
    decompress_num = False
    finding_copy_info = False
    copying_length = False
    temp = ""
    copy_length = 0
    copy_num = 0
    temp_num = ""
    output_array = []
    for i in compressed:
        if not decompress_num:
            copy_num = 1
            if i == '(':
                output_array.append((1, temp))
                temp = ""
                decompress_num = True
                copying_length = True
                finding_copy_info = True
            else:
                temp += i
        elif finding_copy_info:
            if copying_length:
                if i != 'x':
                    temp_num += i
                else:
                    copy_length = int(temp_num) - 1
                    temp_num = ''
                    copying_length = False
            else:
                if i != ')':
                    temp_num += i
                else:
                    copy_num = int(temp_num)

                    temp_num = ''
                    finding_copy_info = False
        else:
            temp += i
            if copy_length == 0:
                output_array.append((copy_num, temp))
                decompress_num = False
                copying_length = False
                finding_copy_info = False
                copy_num = 0
                temp = ''
            copy_length -= 1
    output_string = ''
    output_array.append((copy_num, temp))
    string_lent = 0
    for i in output_array:
        local_temp = ""
        for j in range(0, i[0]):
            local_temp += i[1]
        if '(' in local_temp:
            string_lent += decompressV2(compressed=local_temp, int_num = len(local_temp))
        else:
            # print local_temp
            string_lent += len(local_temp)
    # print output_array
    print string_lent
    return string_lent

    # string_lent = len(output_string)
    # if(string_lent == int_num):
    #     print output_string
    #     return string_lent
    # else:
    #     return decompressV2(compressed=output_string, int_num=string_lent)






if __name__ == "__main__":
    f = open('day9.txt', 'r')
    input = f.read()
    # decompress("ADVENT")
    # decompress("A(1x5)BC")
    # decompress("(3x3)XYZ")
    # decompress("A(2x2)BCD(2x2)EFG")
    # decompress("(6x1)(1x3)A")
    # decompress("X(8x2)(3x3)ABCY")
    print decompressV2(input)
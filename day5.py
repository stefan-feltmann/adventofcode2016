__author__ = 'stefan'

import hashlib
import string

def get_password(input):
    output = ""
    index = 0
    while len(output) < 8:
        m = hashlib.md5()
        m.update(input + str(index))
        hex = m.hexdigest()
        if hex[:5] == "00000":
            output += hex[5]
        index += 1
    print output

def get_password_part2(input):
    char_count = 0
    index = 0
    password = [None, None, None, None, None, None, None, None]
    while char_count < 8:
        m = hashlib.md5()
        m.update(input + str(index))
        hex = m.hexdigest()
        if hex[:5] == "00000":
            if hex[5].isdigit() and int(hex[5]) < len(password) and password[int(hex[5])] == None:
                password[int(hex[5])] = hex[6]
                char_count += 1
        index += 1
    print "".join(password)

if __name__ == "__main__":
    f = open('day5.txt', 'r')
    input = f.read()
    get_password_part2(input)

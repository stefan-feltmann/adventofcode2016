__author__ = 'stefan'
import re

def split_ip(ip):
    # Got this code from here
    # https://github.com/Hwesta/advent-of-code/blob/master/aoc2016/day7.py
    split = re.split(r'\[|\]', ip)
    outside = split[::2]
    inside = split[1::2]

    return outside, inside

def is_reversable(string, num):
    string_reversable = False
    for i in range(num, len(string)+1):
        test_string = string[(i-num):i]
        if str(test_string) == str(test_string)[::-1] and test_string != len(test_string) * test_string[0]:
            string_reversable = True
    return string_reversable

def get_bab_list(string):
    bab_list = []
    for i in range(3, len(string)+1):
        test_string = string[(i-3):i]
        if str(test_string) == str(test_string)[::-1] and test_string != len(test_string) * test_string[0]:
            bab = test_string[1] + test_string[0] + test_string[1]
            bab_list.append(bab)
    return bab_list


def is_ssl(address):
    outside, inside = split_ip(address)
    ssl_good = False
    for i in outside:
        if is_reversable(i, 3):
            bab_list = get_bab_list(i)
            for j in inside:
                for k in bab_list:
                    if k in j:
                        ssl_good = True
    return ssl_good



def is_tls(address):
    outside, inside = split_ip(address)
    outside_good = False
    for i in outside:
        if is_reversable(i, 4):
            outside_good = True
    inside_good = True
    for i in inside:
        if is_reversable(i, 4):
            inside_good = False
    ipv7 = outside_good and inside_good
    return ipv7


if __name__ == "__main__":
    f = open('day7.txt', 'r')
    input = f.read().split('\n')
    count = 0
    for i in input:
        if is_tls(i):
            count += 1
    print count
    count = 0
    for i in input:
        if is_ssl(i):
            count += 1
    print count

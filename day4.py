__author__ = 'stefan'
import string

def parse(input):
    input_token = input.split('-')
    room_name = "".join(input_token[:-1])
    id_token = input_token[-1].split('[')
    id = id_token[0]
    answer = id_token[1][:-1]
    return room_name, id, answer

def parse_encrypted(input):
    input_token = input.split('-')
    room_name = " ".join(input_token[:-1])
    id_token = input_token[-1].split('[')
    id = id_token[0]
    answer = id_token[1][:-1]
    return room_name, id, answer

def hash(table):
    letter = ''
    output = ''
    for number in range(5):
        for i in table.keys():
            if letter == '' or table[i] > table[letter] or (table[i] == table[letter] and string.lowercase.index(i) < string.lowercase.index(letter)):
                letter = i
        output += letter
        table.pop(letter)
        letter = ''
    return output

def calculate(input):
    room_name, id, answer = parse(input)
    table = {}
    output = 0
    for i in room_name:
        try:
            table[i] += 1
        except:
            table[i] = 1
    hashed = hash(table)
    if answer == hashed:
        output = int(id)
    return output

def get_total(input):
    count = 0
    input_token = input.split("\n")
    for i in input_token:
        count += calculate(i)
    print count

def decipher(input):
    room_name, id, answer = parse_encrypted(input)
    output = ""
    for character in room_name:
        if not " " is character:
            for i in range(int(id)):
                index = ord(character) + 1
                if index > ord('z'):
                    index -= 26
                character = chr(index)
        output += character
    print output, id


if __name__ == "__main__":
    f = open('day4.txt', 'r')
    input = f.read()
    get_total(input)
    input_token = input.split("\n")
    for i in input_token:
        decipher(i)

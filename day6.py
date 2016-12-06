__author__ = 'stefan'

def decode(encoded, find_max):
    encoded_tokens = encoded.split('\n')
    string_len = len(encoded_tokens[0])
    letters = []
    for i in range(string_len):
        letters.append({})

    for i in encoded_tokens:
        for j in range(len(i)):
            char = i[j]
            try:
                letters[j][char] += 1
            except:
                letters[j][char] = 1

    answer = ""
    for i in letters:
        if find_max:
            answer += max(i, key=i.get)
        else:
            answer += min(i, key=i.get)
    print answer


if __name__ == "__main__":
    f = open('day6.txt', 'r')
    input = f.read()
    decode(input, True)
    decode(input, False)

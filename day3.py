__author__ = 'stefan'



def get_is_triangle(number_tokens):
    total1 = int(number_tokens[0]) + int(number_tokens[1])
    full1 = int(number_tokens[2])
    answer1 = total1 > full1
    total2 = int(number_tokens[1]) + int(number_tokens[2])
    full2 = int(number_tokens[0])
    answer2 = total2 > full2
    total3 = int(number_tokens[0]) + int(number_tokens[2])
    full3 = int(number_tokens[1])
    answer3 = total3 > full3
    is_triangle = answer1 and answer2 and answer3
    return is_triangle


def find_is_triangle(number):
    number_tokens_raw = number.strip().split("  ")
    number_tokens = []
    for i in number_tokens_raw:
        if i.strip().isdigit():
            number_tokens.append(i)
    is_triangle = get_is_triangle(number_tokens)
    return is_triangle

def is_triangle_column(triangles):
    column1 = []
    column2 = []
    column3 = []
    triangle_token = triangles.split("\n")
    for number in triangle_token:
        number_tokens_raw = number.strip().split("  ")
        number_tokens = []
        for i in number_tokens_raw:
            if i.strip().isdigit():
                number_tokens.append(i)
        index = 1
        for i in number_tokens:
            if index == 1:
                column1.append(i)
                index += 1
            elif index == 2:
                column2.append(i)
                index += 1
            else:
                column3.append(i)
                index = 1

    number_tokens = []
    count = 0
    for i in column1:
        number_tokens.append(i)
        if len(number_tokens) == 3:
            if get_is_triangle(number_tokens):
                count += 1
            number_tokens = []

    for i in column2:
        number_tokens.append(i)
        if len(number_tokens) == 3:
            if get_is_triangle(number_tokens):
                count += 1
            number_tokens = []

    for i in column3:
        number_tokens.append(i)
        if len(number_tokens) == 3:
            if get_is_triangle(number_tokens):
                count += 1
            number_tokens = []

    print count



if __name__ == "__main__":
    f = open('day3.txt', 'r')
    triangles = f.read()
    triangle_token = triangles.split("\n")
    count = 0
    for i in triangle_token:
        if find_is_triangle(i):
            count += 1
    print count
    is_triangle_column(triangles)

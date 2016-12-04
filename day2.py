__author__ = 'stefan'

class DayTwo(object):
    key_pad = [ [ 0 for i in range(3) ] for j in range(3) ]
    x_cord = 1
    y_cord = 1
    output = ""

    def __init__(self):
        count = 1
        for i in range(3):
            for j in range(3):
                self.key_pad[i][j] = count
                # print count
                count += 1

    def move_up(self):
        if not self.y_cord <= 0:
            self.y_cord -= 1
        # else:
        #     print "not"

    def move_down(self):
        if not self.y_cord >= (len(self.key_pad[0]) - 1):
            self.y_cord += 1
        # else:
        #     print "not"

    def move_left(self):
        if not self.x_cord <= 0:
            self.x_cord -= 1
        # else:
        #     print "not"

    def move_right(self):
        if not self.x_cord >= (len(self.key_pad) - 1):
            self.x_cord += 1
        # else:
        #     print "not"

    def find_key(self):
        key = str(self.key_pad[self.y_cord][self.x_cord])
        print "key: " + key
        self.output += key


    def find_move(self, letter):
        # print self.x_cord, self.y_cord
        # print letter
        if 'U' in letter:
            self.move_up()
        elif 'D' in letter:
            self.move_down()
        elif 'L' in letter:
            self.move_left()
        else:
            self.move_right()
        # print self.x_cord, self.y_cord
        #
        # print self.key_pad[self.x_cord][self.y_cord]

    def read(self, pattern):
        pattern_tokens = pattern.split('\n')
        for sub_pattern in pattern_tokens:
            for letter in sub_pattern:
                self.find_move(letter)
            self.find_key()
            # print '-------------------------------------------------------------------------'
        print self.output

class DayTwoPart2(object):
    key_pad = None
    x_cord = 0
    y_cord = 2
    output = ""
    empty = "#"

    def __init__(self):
        row1 = [self.empty, self.empty, 1, self.empty, self.empty]
        row2 = [self.empty,2,3,4, self.empty]
        row3 = [5,6,7,8,9]
        row4 = [self.empty,'A','B','C', self.empty]
        row5 = [self.empty, self.empty, 'D', self.empty, self.empty]
        self.key_pad = [row1, row2, row3, row4, row5]

    def move_up(self):
        if not self.y_cord <= 0:
            if not str(self.key_pad[self.y_cord-1][self.x_cord]) in self.empty:
                self.y_cord -= 1

    def move_down(self):
        if not self.y_cord >= (len(self.key_pad) - 1):
            if not str(self.key_pad[self.y_cord+1][self.x_cord]) in self.empty:
                self.y_cord += 1

    def move_left(self):
        if not self.x_cord <= 0:
            if not str(self.key_pad[self.y_cord][self.x_cord-1]) in self.empty:
                self.x_cord -= 1

    def move_right(self):
        if not self.x_cord >= (len(self.key_pad[self.y_cord]) - 1):
            if not str(self.key_pad[self.y_cord][self.x_cord+1]) in self.empty:
                self.x_cord += 1

    def find_move(self, letter):
        if 'U' in letter:
            self.move_up()
        elif 'D' in letter:
            self.move_down()
        elif 'L' in letter:
            self.move_left()
        else:
            self.move_right()

    def read(self, pattern):
        pattern_tokens = pattern.split('\n')
        for sub_pattern in pattern_tokens:
            for letter in sub_pattern:
                self.find_move(letter)
            self.find_key()
        print self.output

    def find_key(self):
        key = str(self.key_pad[self.y_cord][self.x_cord])
        print "key: " + key
        self.output += key


if __name__ == "__main__":
    day2 = DayTwo()
    f = open('day2.txt', 'r')
    directions = f.read()
    day2.read(directions)
    day2part2 = DayTwoPart2()
    day2part2.read(directions)
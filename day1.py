__author__ = 'stefan'

class DayOne(object):
    NORTH_VAL = 1
    SOUTH_VAL = -1
    EAST_VAL = 1
    WEST_VAL = -1

    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

    current_facing_name = NORTH
    current_facing_val = NORTH_VAL

    north_south = 0
    eastWest = 0

    visited_places = []
    place_found = False

    def change_north(self, direction):
        if 'L' in direction :
            self.current_facing_name = self.WEST
            self.current_facing_val = self.WEST_VAL
        else:
            self.current_facing_name = self.EAST
            self.current_facing_val = self.EAST_VAL

    def change_south(self, direction):
        if 'L' in direction :
            self.current_facing_name = self.EAST
            self.current_facing_val = self.EAST_VAL
        else:
            self.current_facing_name = self.WEST
            self.current_facing_val = self.WEST_VAL

    def change_east(self, direction):
        if 'L' in direction:
            self.current_facing_name = self.NORTH
            self.current_facing_val = self.NORTH_VAL
        else:
            self.current_facing_name = self.SOUTH
            self.current_facing_val = self.SOUTH_VAL

    def change_west(self, direction):
        if 'L' in direction:
            self.current_facing_name = self.SOUTH
            self.current_facing_val = self.SOUTH_VAL
        else:
            self.current_facing_name = self.NORTH
            self.current_facing_val = self.NORTH_VAL

    def calculate_move(self, direction):
        distance_string = direction.replace('L','').replace('R','')
        distance = int(distance_string)
        if self.current_facing_name == self.NORTH or self.current_facing_name == self.SOUTH:
            for i in range(0, distance):
                self.north_south += self.current_facing_val
                if not self.place_found:
                    self.add_visited_places()
        else:
            for i in range(0, distance):
                self.eastWest += self.current_facing_val
                if not self.place_found:
                    self.add_visited_places()

    def process(self, directions):
        movement_tokens = directions.split(',')
        for i in movement_tokens:
            if self.current_facing_name == self.NORTH:
                self.change_north(i)
            elif self.current_facing_name == self.SOUTH:
                self.change_south(i)
            elif self.current_facing_name == self.EAST:
                self.change_east(i)
            else:
                self.change_west(i)
            self.calculate_move(i)

        self.total()

    def add_visited_places(self):
        location = str(self.north_south) + ' ' + str(self.eastWest)
        if location in self.visited_places:
            self.total()
            self.place_found = True
        else:
            self.visited_places.append(location)

    def total(self):
        total = abs(self.north_south) + abs(self.eastWest)
        print total

if __name__ == "__main__":
    day1 = DayOne()
    f = open('day1.txt', 'r')
    directions = f.read()
    day1.process(directions)




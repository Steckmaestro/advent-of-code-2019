import timeit


def load_file(filename):
    with open(filename, 'r') as file:
        return [row.strip('\n').split(',') for row in file.readlines()]


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def return_as_list(self):
        return [self.x, self.y]

    def return_as_tuple(self):
        return (self.x, self.y)

    # U - Up R - Right L - Left - D Down
    @classmethod
    def move_to_new_position(cls, positions, current_pos, movement):
        dir = movement[0]
        steps = int(movement[1:])

        for i in range(1, steps+1):
            if dir == 'U':
                x = int(current_pos[0])
                y = int(current_pos[1]) + i
            elif dir == 'D':
                x = int(current_pos[0])
                y = int(current_pos[1]) - i
            elif dir == 'R':
                x = int(current_pos[0]) + i
                y = int(current_pos[1])

            elif dir == 'L':
                x = int(current_pos[0]) - i
                y = int(current_pos[1])

            new_pos = (x, y)
            positions.append(new_pos)

        return positions


class Cable:
    def __init__(self, wiring):
        self.wiring = wiring
        self.visited_positions = self.calculate_positions(wiring)

    def __str__(self):
        return "Class() Positions: {}. Positions length: {}. Wiring: {}.".format(self.visited_positions, len(self.visited_positions), self.wiring)

    def calculate_positions(self, wiring):
        last_position = (0, 0)
        positions = []

        for direction in wiring:
            visited_positions = Position.move_to_new_position(
                positions, last_position, direction)

            last_position = visited_positions[-1]

        return positions


def main():
    file = load_file('input_3')
    cables = []
    for i in range(0, len(file)):
        wiring = file[i]
        cable = Cable(wiring).visited_positions
        cables.append(cable)

    intersections = set(cables[0]) & set(cables[1])

    return {'part1': min(abs(x)+abs(y) for (x, y) in intersections), 'part2': (2 + min(sum(cable.index(intersect) for cable in cables) for intersect in intersections))}


if __name__ == '__main__':
    main()

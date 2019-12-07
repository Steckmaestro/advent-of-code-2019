import math


def f(mass): return math.floor(mass / 3) - 2


total_fuel = 0


with open('input_1', 'r') as file:
    rows = [row.rstrip('\n') for row in file.readlines()]

    for row in rows:
        total_fuel += f(int(row))

    print(total_fuel)

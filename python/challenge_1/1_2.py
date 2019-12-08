import math


def f(mass): return math.floor(mass / 3) - 2


total_fuel = 0
additional_fuel = 0


with open('input_1', 'r') as file:
    rows = [row.rstrip('\n') for row in file.readlines()]
    missing_fuel = 0

    for row in rows:
        total_fuel += f(int(row))
        missing_fuel += f(int(row))
        while(f(int(missing_fuel))>=0):
            missing_fuel = f(int(missing_fuel))
            additional_fuel += missing_fuel
    
    print("Total fuel for mass (1:1): ", total_fuel)
    print("Added fuel because of added fuelmass: ", additional_fuel)

#!/usr/bin/env python3

def get_fuel_req(mass):
    # take its mass, divide by three, round down, and subtract 2
    fuel = int(mass/3) - 2
    if fuel <= 0:
        return 0
    return fuel + get_fuel_req(fuel)

total_fuel = 0
with open("input1.txt") as f:
    for line in f:
        mass = int(line)
        total_fuel += get_fuel_req(mass)

print(total_fuel)
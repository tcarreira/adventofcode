#!/usr/bin/env python3

import os
from solver_1 import convert_ticket_to_id

curdir = os.path.dirname(os.path.realpath(__file__))

def main():
    my_ticket_id=0
    seen_tickets = [False] * 2**10

    with open(curdir + "/input.txt") as f:
        document = {}

        for line in f.readlines():
            id = convert_ticket_to_id(line.strip())
            seen_tickets[id] = True
    
    front_rows = True
    i = 0
    while True:
        if seen_tickets[i] and front_rows:
            front_rows = False
            continue

        if not seen_tickets[i] and not front_rows:
            my_ticket_id = i
            break
        
        i += 1
        

    print(f"my seat ID: {my_ticket_id}")

if __name__ == "__main__":
    main()
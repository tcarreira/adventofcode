#!/usr/bin/env python3

input="1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0"

class HaltException(Exception):
    pass
class InvalidOpcodeException(Exception):
    pass

def read_opcode(four_sized_array, full_array):
    # print("reading ", four_sized_array)
    if four_sized_array[0] == 99:
        raise HaltException()
    elif four_sized_array[0] == 1:
        full_array[four_sized_array[3]] = full_array[four_sized_array[1]] + full_array[four_sized_array[2]]
        return full_array
    elif four_sized_array[0] == 2:
        full_array[four_sized_array[3]] = full_array[four_sized_array[1]] * full_array[four_sized_array[2]]
        return full_array
    else:
        raise InvalidOpcodeException()


def computer(full_array):
    try:
        for i in range(0, len(full_array), 4):
            full_array = read_opcode(full_array[i:i+4], full_array)
    except HaltException:
        # print(",".join([str(x) for x in full_array]))
        return full_array[0]
    except InvalidOpcodeException:
        print("Invalid Opcode")


def main1():
    full_array = [int(x) for x in input.split(",")]
    return(computer(full_array))

def main2():
    for noun in range(100):
        for verb in range(100):
            full_array = [int(x) for x in input.split(",")] # reset state
            full_array[1] = noun
            full_array[2] = verb

            if 19690720 == computer(full_array):
                return noun*100 + verb


print("part 1: ", main1())
print("part 2: ",main2())

#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = "A0016C880162017C3686B18A3D4780"

global expression  # I'm lazy


def append_literal(literal_value: int):
    global expression
    expression += f"{literal_value}"


def append_start_expression(type_id):
    global expression
    if type_id == 2:
        expression += "min(["
    elif type_id == 3:
        expression += "max(["
    else:
        expression += "("


def append_operator(type_id):
    global expression
    if type_id == 0:
        expression += "+"
    elif type_id == 1:
        expression += "*"
    elif type_id in (2, 3):
        expression += ","
    elif type_id == 5:
        expression += ">"
    elif type_id == 6:
        expression += "<"
    elif type_id == 7:
        expression += "=="


def append_end_expression(type_id):
    global expression
    if type_id == 7:
        expression = expression[:-1]

    if type_id in [2, 3]:
        expression = expression[:-1] + "])"
    else:
        expression = expression[:-1] + ")"


def part1(p_input):
    global expression  # part 2
    expression = ""  # part 2

    full_message = "".join([f"{int(c,16):04b}" for c in p_input])

    def read_packet(message):
        global expression
        version = int(message[0:3], 2)
        type_id = int(message[3:6], 2)
        v_sum = version

        if type_id == 4:
            current_group, literal_value = 0, ""
            while True:
                char_pos = 6 + current_group * 5
                chunk = message[char_pos : char_pos + 5]
                literal_value += chunk[1:]
                current_group += 1
                if chunk[0] == "0":
                    break

            append_literal(int(literal_value, 2))  # part 2
            return v_sum, 6 + current_group * 5

        append_start_expression(type_id)  # part 2
        length_type_id = int(message[6:7], 2)
        if length_type_id == 0:

            total_length = int(message[7 : 7 + 15], 2)
            chunk_end = 7 + 15 + total_length
            next_chunk = 7 + 15
            while next_chunk < chunk_end:
                tmp_value, tmp_next_chunk = read_packet(message[next_chunk:chunk_end])
                v_sum += tmp_value
                next_chunk += tmp_next_chunk
                append_operator(type_id)  # part2

            append_end_expression(type_id)  # part 2
            return v_sum, chunk_end
        else:
            number_sub_packets = int(message[7 : 7 + 11], 2)
            next_bytes = 7 + 11
            for _ in range(number_sub_packets):
                tmp_value, tmp_next_bytes = read_packet(message[next_bytes:])
                v_sum += tmp_value
                next_bytes += tmp_next_bytes
                append_operator(type_id)  # part2

            append_end_expression(type_id)  # part 2
            return v_sum, next_bytes

    return read_packet(full_message)[0]


def part2(p_input):
    solution = p_input
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    message = raw_input.strip()

    print("Solution to Part 1:")
    print(part1(message))

    print("Solution to Part 2:")
    print(eval(expression))


if __name__ == "__main__":
    main()

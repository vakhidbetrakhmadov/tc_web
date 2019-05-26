import sys
from enum import Enum

def parse(in_filename):
    class State(Enum):
        SEARCHING = 1
        READING = 2

    in_file = open(in_filename, "r")
    output = []
    state = State.SEARCHING
    buffer = ""
    for next_line in in_file:
        if state == State.SEARCHING:
            if "generatedCuda:" in next_line:
                state = State.READING
        elif state == State.READING:
            if "Execution time:" in next_line:
                buffer += next_line
                output.append(buffer)
                buffer = ""
                state = State.SEARCHING
            elif "generatedCuda:" in next_line:
                buffer = ""
                state = State.SEARCHING
            else:
                buffer += next_line

    in_file.close()

    return output

def parse_to_file(in_filename, out_filename):
    class State(Enum):
        SEARCHING = 1
        READING = 2

    in_file = open(in_filename, "r")
    output = []
    state = State.SEARCHING
    buffer = ""
    for next_line in in_file:
        if state == State.SEARCHING:
            if "generatedCuda:" in next_line:
                state = State.READING
        elif state == State.READING:
            if "Execution time:" in next_line:
                buffer += next_line
                output.append(buffer)
                buffer = ""
                state = State.SEARCHING
            elif "generatedCuda:" in next_line:
                buffer = ""
                state = State.SEARCHING
            else:
                buffer += next_line

    in_file.close()

    out_file = open(out_filename, "w+")
    for next_output in output:
        out_file.write(next_output)
    out_file.close()
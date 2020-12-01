# --- Day 2: 1202 Program Alarm ---
# https://adventofcode.com/2019/day/2

import sys

PROGRAM = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,10,19,23,2,9,23,27,1,6,27,31,1,10,31,35,1,35,10,39,1,9,39,43,1,6,43,47,1,10,47,51,1,6,51,55,2,13,55,59,1,6,59,63,1,10,63,67,2,67,9,71,1,71,5,75,1,13,75,79,2,79,13,83,1,83,9,87,2,10,87,91,2,91,6,95,2,13,95,99,1,10,99,103,2,9,103,107,1,107,5,111,2,9,111,115,1,5,115,119,1,9,119,123,2,123,6,127,1,5,127,131,1,10,131,135,1,135,6,139,1,139,5,143,1,143,9,147,1,5,147,151,1,151,13,155,1,5,155,159,1,2,159,163,1,163,6,0,99,2,0,14,0]

def run_gravity_assist(noun, verb):
    memory = PROGRAM.copy() # Reset/Read/Load program into memory
    memory[1] = noun
    memory[2] = verb
    pointer = 0
    opcode = memory[pointer]
    while opcode != 99:
        if opcode == 1:
            memory[memory[pointer + 3]] = memory[memory[pointer + 1]] + memory[memory[pointer + 2]]
        elif opcode == 2:
            memory[memory[pointer + 3]] = memory[memory[pointer + 1]] * memory[memory[pointer + 2]]
        else:
            print("Unknown opcode. Something went wrong.")
            break
        pointer += 4
        opcode = memory[pointer]
    return memory[0]

for noun in range(0, 100):
    for verb in range(0, 100):
        result = run_gravity_assist(noun, verb)
        print("Result", result)
        if result == 19690720:
            print("Gravity assist parameters:", noun, verb)
            print("100 * noun + verb =", 100 * noun + verb)
            sys.exit() # Break nested for-loop?
        else:
            print("not found")

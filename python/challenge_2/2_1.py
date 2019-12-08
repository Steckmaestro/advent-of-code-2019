with open('input_2', 'r') as file:
    instructions = file.readlines()[0].strip('\n').split(',')

print("Unmodifed instructions: ", instructions)

print("Restore state at crash...")
instructions[1] = 12
instructions[2] = 2

exit = False

for i, val in (enumerate(instructions)):
    if exit:
        break
    if i % 4 == 0:
        print("Instruction found at pos: ", i)
        instruction = int(instructions[i])

        if instruction == 99:
            exit = True
            break

        operand_1_pos = int(instructions[i+1])
        operand_2_pos = int(instructions[i+2])
        operand_1 = int(instructions[operand_1_pos])
        operand_2 = int(instructions[operand_2_pos])
        save_to_location = int(instructions[i+3])

        print("$ Current position: {}. Instruction: {}. Operand 1 pos: {} val: {}. Operand 2 pos: {} val: {}. Save to location: {}.".format(
            i, instruction, operand_1_pos, operand_1, operand_2_pos, operand_2, save_to_location))

        # Opcodes:
        # 1 add together
        # 2 multiplies
        # 99 exit program
        if instruction == 1:
            print("Found adding operation. Adding {} and {} at position {}".format(
                operand_1, operand_2, save_to_location))
            instructions[save_to_location] = operand_1 + operand_2
        elif instruction == 2:
            print("Found multiplication operation. Multiplying {} and {} at position {}".format(
                operand_1, operand_2, save_to_location))
            instructions[save_to_location] = operand_1 * operand_2
        else:
            print("Found incorrect instruction {} at position {}".format(
                instruction, i))
            exit = not exit
            break

print("Finished: ", instructions)

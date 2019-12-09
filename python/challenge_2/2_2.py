exit = False

answer = None


def generate_instructions(noun, verb):
    with open('input_2', 'r') as file:
        #print("Generating file")
        instructions = file.readlines()[0].strip('\n').split(',')
        # Restore state before crash
        instructions[1] = noun
        instructions[2] = verb

    return instructions


def run_operand(instruction, operand_1, operand_2):
    if instruction == 1:
        return operand_1 + operand_2
    elif instruction == 2:
        return operand_1 * operand_2


while (not exit):
    for noun in range(0, 50):
        for verb in range(0, 50):
            print(
                "Noun is {} verb is {} generating instructions with seed..".format(noun, verb))
            instructions = generate_instructions(noun, verb)

            for i in range(0, len(instructions)-1):
                if exit:
                    break
                if i % 4 == 0:
                    instruction = int(instructions[i])

                    if instruction == 99:
                        break

                    operand_1_pos = int(instructions[i+1])
                    operand_2_pos = int(instructions[i+2])
                    operand_1 = int(instructions[operand_1_pos])
                    operand_2 = int(instructions[operand_2_pos])
                    save_to_location = int(instructions[i+3])

                    result = run_operand(instruction, operand_1, operand_2)
                    #print("Result: ", result)
                    if result == 19690720:
                        print("Found 19690720. Operand 1: {}. Operand 2: {}. Noun: {}. Verb: {}.".format(
                            operand_1, operand_2, noun, verb))

                        answer = {'operand_1': operand_1,
                                  'operand_2': operand_2, 'noun': noun, 'verb': verb}

                        exit = True
                        break

                    instructions[save_to_location] = result


print(answer)

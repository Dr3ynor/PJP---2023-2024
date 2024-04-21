#!/usr/bin/env python3
class VirtualMachine:
    def __init__(self, filename):
        self.memory = {}
        self.stack = []
        self.pc = 0
        self.labels = {}
        self.instructions = self.load_instructions(filename)
        print(f"INSTRUCTIONS: {self.instructions}")

    def load_instructions(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        instructions = []
        for i, line in enumerate(lines):
            parts = line.strip().split()

            parts[0] = parts[0].upper()
            instructions.append(parts)

        return instructions

    def run(self):
        #print(self.instructions)
        for instruction in self.instructions:
            #print(f"Labels: {self.labels}")
            #print(f"Stack: {self.stack}\n")
            #print(f"Memory: {self.memory}")
            if instruction[0] == "PUSH":
                if instruction[1] == "I":
                    self.stack.append(int(instruction[2]))
                elif instruction[1] == "F":
                    self.stack.append(float(instruction[2]))
                elif instruction[1] == "S":
                    value = ' '.join(instruction[2:])
                    self.stack.append(value)

                elif instruction[1] == "B":
                    #print(f"BOOL INSTRUCTION: {instruction}")

                    
                    self.stack.append(instruction[2])
                    #print(f"STACK AFTER APPENDING: {self.stack}")
                else:
                    print(f"Error: Unknown type {instruction[1]} in PUSH instruction")
                    return
            elif instruction[0] == "SAVE":
                if len(instruction) < 2:
                    print("Error: Missing variable name in SAVE instruction")
                    return
                variable_name = instruction[1]
                self.memory[variable_name] = self.stack.pop()
            elif instruction[0] == "LOAD":
                if instruction[1] not in self.memory:
                    print(f"Error: Variable {instruction[1]} not found")
                    return
                self.stack.append(self.memory[instruction[1]])
            elif instruction[0] in ["ADD", "SUB", "MUL", "DIV", "MOD"]:
                if len(self.stack) < 2:
                    print("Error: Not enough values on the stack")
                    return
                right = self.stack.pop()
                left = self.stack.pop()
                if instruction[0] == "ADD":
                    self.stack.append(left + right)
                elif instruction[0] == "SUB":
                    self.stack.append(left - right)
                elif instruction[0] == "MUL":
                    self.stack.append(left * right)
                elif instruction[0] == "DIV":
                    self.stack.append(int(left / right))
                elif instruction[0] == "MOD":
                    self.stack.append(left % right)

            elif instruction[0] == "PRINT":
                n = int(instruction[1]) if len(instruction) > 1 else 1
                if len(self.stack) < n:
                    print(f"Error: Not enough values on the stack")
                    return
                values = [self.stack.pop() for _ in range(n)]
                print(values[::-1])

                #for value in reversed(values):
                        #print(value)


            elif instruction[0] == "POP":
                if not self.stack:
                    print("Error: Stack is empty")
                    return
                self.stack.pop()

            elif instruction[0] == "UMINUS":
                if not self.stack:
                    print("Error: Stack is empty")
                    return
                self.stack[-1] = -self.stack[-1]

            elif instruction[0] == "ITOF":
                if not self.stack:
                    print("Error: Stack is empty")
                    return
                if not isinstance(self.stack[-1], int):
                    print("Error: Top element on the stack is not an integer")
                    return
                self.stack[-1] = float(self.stack[-1])

            elif instruction[0] == "CONCAT":
                if len(self.stack) < 2:
                    print("Error: Less than two elements on the stack")
                    return
                right = self.stack.pop()
                left = self.stack.pop()
                if not isinstance(left, str) or not isinstance(right, str):
                    print("Error: CONCAT expects two strings on the stack")
                    return

                result = (left + right).replace('"', '')
                self.stack.append(result)

            elif instruction[0] == "READ":
                if len(instruction) < 2:
                    print("Error: Missing type in READ instruction")
                    return
                if instruction[1] == "I":
                    value = int(input("Please enter an integer: "))
                elif instruction[1] == "F":
                    value = float(input("Please enter a float: "))
                elif instruction[1] == "S":
                    value = input("Please enter a string: ")
                elif instruction[1] == "B":
                    value = input("Please enter a boolean (True/False): ") #== "True"

                    if value.upper() == "TRUE":
                        value = True
                    elif value.upper() == "FALSE":
                        value = False
                    else:
                        print("Error: Invalid boolean value")
                        return

                else:
                    print(f"Error: Unknown type {instruction[1]} in READ instruction")
                    return
                self.stack.append(value)


            elif instruction[0] == "LT":
                if len(self.stack) < 2:
                    print("Error: Not enough values on the stack")
                    return
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(left < right)
            
            elif instruction[0] == "GT":
                if len(self.stack) < 2:
                    print("Error: Not enough values on the stack")
                    return
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(left > right)
            elif instruction[0] == "EQ":
                if len(self.stack) < 2:
                    print("Error: Not enough values on the stack")
                    return
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(left == right)


            elif instruction[0] == "AND":
                if len(self.stack) < 2:
                    print("Error: Not enough values on the stack")
                    return
                right = self.stack.pop()
                left = self.stack.pop()


                if right == "true":
                    right = True
                elif right == "false":
                    right = False

                if left == "true":
                    left = True
                elif left == "false":
                    left = False

                # print(f"Left: {left} | Right: {right}")
                self.stack.append(left and right)
                
            elif instruction[0] == "OR":
                if len(self.stack) < 2:
                    print("Error: Not enough values on the stack")
                    return
                right = self.stack.pop()
                left = self.stack.pop()

                if right == "true":
                    right = True
                elif right == "false":
                    right = False

                if left == "true":
                    left = True
                elif left == "false":
                    left = False

                self.stack.append(left or right)

            elif instruction[0] == "NOT":
                if not self.stack:
                    print("Error: Stack is empty")
                    return
                self.stack[-1] = not self.stack[-1]
            
            elif instruction[0] == 'FJMP':
                if not self.stack:
                    print("Error: Stack is empty")
                    return
                if not self.stack[-1]:
                    try:
                        self.pc = self.labels[instruction[1]]
                    except KeyError:
                        print(f"Error: Label {instruction[1]} not found | FJMP")
                        return
                else:
                    self.pc += 1

            elif instruction[0] == 'JMP':
                try:
                    self.pc = self.labels[instruction[1]]
                except KeyError:
                    print(f"Error: Label {instruction[1]} not found | JMP")
                    return

            else:
                print(f"Error: Unknown instruction {instruction[0]}")
                return


#filename = "inputs/lab_input"
#filename = "inputs/testing"

"""
for i in range(1,4):
    filename = f"inputs/PLC_t{i}.out"

    vm = VirtualMachine(filename)
    vm.run()

    # print(vm.memory)
    print("\n\n\n ---------------------- \n\n\n")
"""


filename = "inputs/PLC_t1.out"

vm = VirtualMachine(filename)
vm.run()

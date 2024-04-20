#!/usr/bin/env python3

class VirtualMachine:
    def __init__(self, filename):
        self.memory = {}
        self.stack = []
        self.instructions = self.load_instructions(filename)

    def load_instructions(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        instructions = []
        for line in lines:
            instruction = line.strip().split()
            instruction[0] = instruction[0].upper()
            instructions.append(instruction)
        return instructions

    def run(self):
        for instruction in self.instructions:
            #print(f"Stack: {self.stack}\n")
            #print(f"Memory: {self.memory}")
            if instruction[0] == "PUSH":
                if instruction[1] == "I":
                    self.stack.append(int(instruction[2]))
                elif instruction[1] == "F":
                    self.stack.append(float(instruction[2]))
                elif instruction[1] == "S":
                    value = ' '.join(instruction[2:])
                    #print(f"Value: {value}")
                    #print(f"Instruction: {instruction}")
                    self.stack.append(value)
                    #self.stack.append(instruction[2])
                elif instruction[1] == "B":
                    self.stack.append(bool(instruction[2]))
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
                for value in reversed(values):
                    print(value)


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

                self.stack.append(left + right)

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
                    value = input("Please enter a boolean (True/False): ") == "True"
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
                print("Stack: ", self.stack)
                right = self.stack.pop()
                left = self.stack.pop()

                #print(f"Left: {left} | Right: {right}")
                self.stack.append(left and right)



                
            elif instruction[0] == "OR":
                if len(self.stack) < 2:
                    print("Error: Not enough values on the stack")
                    return
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(left or right)
            elif instruction[0] == "NOT":
                if not self.stack:
                    print("Error: Stack is empty")
                    return
                self.stack[-1] = not self.stack[-1]
            





            else:
                print(f"Error: Unknown instruction {instruction[0]}")
                return


#filename = "inputs/lab_input"
#filename = "inputs/testing"

filename = "inputs/PLC_t3.out"
vm = VirtualMachine(filename)
vm.run()

class InstructionGenerator:
    def __init__(self):
        self.output = []

    def parse(self, input):
        instructions = input.split('\n')
        for instruction in instructions:
            self.interpret(instruction)

    # TODO: Add more elifs!
    def interpret(self, instruction):
        if instruction.startswith('write'):
            self.generate_write(instruction)
        elif instruction.startswith('string') or instruction.startswith('float') or instruction.startswith('int') or instruction.startswith('bool'):
            self.generate_declaration(instruction)
        elif instruction.startswith('read'):
            self.generate_read(instruction)
        elif '=' in instruction:
            self.generate_assignment(instruction)
        

    # TODO: Implement check for how many instructions used(?)
    def generate_write(self, instruction):
        value = instruction[6:].split(":")[0].strip('"')
        self.output.append('push S "{}"'.format(value))
        self.output.append('print 1')
        
        #self.output.append('push S "{}"'.format(instruction[6:-1]))
        # self.output.append('print 1') #?????

    def generate_declaration(self, instruction):
        split_instruction = instruction.split()
        var_type = split_instruction[0]
        var_name = split_instruction[1] if len(split_instruction) > 1 else None
        if var_type == 'string':
            self.output.append('push S ""')
        elif var_type == 'float':
            self.output.append('push F 0.0')
        elif var_type == 'int':
            self.output.append('push I 0')
        elif var_type == 'bool':
            self.output.append('push B true')
        if var_name:
            self.output.append('save {}'.format(var_name))

    def generate_read(self, instruction):
        var_names = instruction[5:].split(',')
        for var_name in var_names:
            self.output.append('read I') #
            self.output.append('save {}'.format(var_name))

    def generate_assignment(self, instruction):   
        split_instruction = instruction.split('=')
        value = split_instruction[-1].strip()
        var_names = [var_name.strip() for var_name in split_instruction[:-1]]
        for var_name in var_names:
            self.output.append('push {} {}'.format(self.get_type(value), value))
            self.output.append('save {}'.format(var_name))

    def add_sub(self, instruction):
        pass

    def mul_div(self, instruction):
        pass

    def mod(self, instruction):
        pass

    def unary_minus(self, instruction):
        pass

    def and_or(self, instruction):
        pass

    def gt(self, instruction):
        pass

    def lt(self, instruction):
        pass

    def eq(self, instruction):
        pass

    def neg(self, instruction):
        #unary not
        pass

    def push_T_x(self, instruction):
        pass

    def pop(self, instruction):
        pass

    def load_id(self, instruction):
        pass

    def save_id(self, instruction):
        pass

    def label(self, instruction):
        pass

    def jump(self, instruction):
        pass

    def fjmp(self, instruction):
        pass

    def print_(self, instruction):
        pass

    def concat(self, instruction):
        pass

    def itof(self, instruction):
        pass

    def load(self, instruction):
        pass

    def get_output(self):
        return '\n'.join(self.output)
    
    def get_type(self, value):
        if value.isdigit():
            return 'I'
        elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
            return 'F'
        elif value.lower() in ['true', 'false']:
            return 'B'
        else:
            return 'S'
    
    def pre_process_data(self, data):
        lines = data.split('\n')
        cleaned_lines = []
        for line in lines:
            cleaned_line = line.rstrip(';')
            cleaned_lines.append(cleaned_line)
        return '\n'.join(cleaned_lines)

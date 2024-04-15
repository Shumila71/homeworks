OP_NAMES = {0: 'entry', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}

def not_implemented(vm):
    raise RuntimeError('Not implemented!')

LIB = {
    '+': not_implemented,
    '-': not_implemented,
    '*': not_implemented,
    '/': not_implemented,
    '%': not_implemented,
    '&': not_implemented,
    '|': not_implemented,
    '^': not_implemented,
    '<': not_implemented,
    '>': not_implemented,
    '=': not_implemented,
    '<<': not_implemented,
    '>>': not_implemented,
    'if': not_implemented,
    'for': not_implemented,
    '.': not_implemented,
    'emit': not_implemented,
    '?': not_implemented,
    'array': not_implemented,
    '@': not_implemented,
    '!': not_implemented
}

def disasm(bytecode):
    pc = 0
    while pc < len(bytecode):
        opcode = bytecode[pc] & 0b111
        argument = bytecode[pc] >> 3
        if opcode in OP_NAMES:
            if opcode == 0:
                print(f"  {OP_NAMES[opcode]} {argument}")
            elif opcode == 1:
                op_code = argument
                op_name = LIB.get(op_code)
                if op_name is not None:
                    print(f"  {OP_NAMES[opcode]} '{op_name}'")
                else:
                    print(f"  {OP_NAMES[opcode]} {op_code}")
            else:
                print(f"  {OP_NAMES[opcode]}")
        else:
            print(f"  Unknown opcode: {opcode}")

        pc += 1

# Пример использования:
disasm([0, 16, 16, 1, 121, 5])

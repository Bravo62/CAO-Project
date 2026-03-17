import pandas as pd

# Instruction categories
INSTRUCTION_TYPES = {
    "LOAD": "Memory",
    "STORE": "Memory",
    "ADD": "Arithmetic",
    "SUB": "Arithmetic",
    "MUL": "Complex",
    "DIV": "Complex",
    "BRANCH": "Control",
    "JUMP": "Control"
}


def parse_trace(file):
    """
    Reads instruction trace file and categorizes instructions
    """
    instructions = []

    with open(file, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue

        opcode = parts[0]
        operands = parts[1:]

        category = INSTRUCTION_TYPES.get(opcode, "Unknown")

        instructions.append({
            "opcode": opcode,
            "operands": operands,
            "category": category
        })

    df = pd.DataFrame(instructions)
    return df
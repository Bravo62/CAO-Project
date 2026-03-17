def detect_hazards(df):
    """
    Detects data hazards, memory penalties and branch penalties.
    """

    data_hazard_penalty = 0
    branch_penalty = 0
    memory_penalty = 0

    previous_dest = None

    for i, row in df.iterrows():

        opcode = row["opcode"]
        operands = row["operands"]

        # DATA HAZARD DETECTION
        if previous_dest and previous_dest in operands:
            data_hazard_penalty += 1

        # MEMORY LATENCY
        if row["category"] == "Memory":
            memory_penalty += 2

        # BRANCH PENALTY
        if row["category"] == "Control":
            branch_penalty += 2

        # destination register heuristic
        if len(operands) > 0:
            previous_dest = operands[0]

    return {
        "data_hazard": data_hazard_penalty,
        "branch_penalty": branch_penalty,
        "memory_penalty": memory_penalty
    }
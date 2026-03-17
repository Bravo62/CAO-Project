# Basic cycle costs per instruction type

CYCLE_COST = {
    "Arithmetic": 1,
    "Complex": 3,
    "Memory": 5,
    "Control": 2
}


def compute_ideal_cycles(df):
    """
    Calculates ideal cycles assuming no hazards.
    """
    cycles = 0

    for _, row in df.iterrows():
        cycles += CYCLE_COST.get(row["category"], 1)

    return cycles
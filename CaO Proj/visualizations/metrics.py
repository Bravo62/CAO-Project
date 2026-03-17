def compute_efficiency(ideal_cycles, penalties):
    """
    Calculates CPU efficiency.
    """

    total_penalty = sum(penalties.values())

    actual_cycles = ideal_cycles + total_penalty

    efficiency = (ideal_cycles / actual_cycles) * 100

    return actual_cycles, efficiency
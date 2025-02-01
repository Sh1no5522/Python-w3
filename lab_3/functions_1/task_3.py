def solve(num_heads, num_legs):
    if num_legs % 2 != 0 or num_heads > num_legs // 2:
        return "No solution."

    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if 2 * chickens + 4 * rabbits == num_legs:
            return f"Chickens: {chickens}, Rabbits: {rabbits}"

    return "No solution."
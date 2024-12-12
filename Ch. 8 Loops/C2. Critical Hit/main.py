def calculate_flurry_crit(num_attacks, base_damage):
    total = 0
    for i in range(num_attacks):
        if i == num_attacks - 1:
            total += base_damage * 4
            print(f"i is: {i} num_attacks is: {num_attacks}")
        else:
            total += base_damage * 2
    return total
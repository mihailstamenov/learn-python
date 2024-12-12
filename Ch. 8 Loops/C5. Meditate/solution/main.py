def meditate(mana, max_mana, energy, energy_potions):
    while mana < max_mana and (energy > 0 or energy_potions > 0):
        if energy == 0:
            energy_potions -= 1
            energy += 50
        mana += 3
        energy -= 1
    if mana > max_mana:
        mana = max_mana
    return mana, energy, energy_potions

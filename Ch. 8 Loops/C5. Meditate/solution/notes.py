def meditate(mana, max_mana, energy, energy_potions):
  pass
    # while mana < max_mana and (energy > 0 or energy_potions > 0):
    #     if energy == 0:
    #         energy += 50
    #         energy_potions -= 1
    #     mana += 3
    #     energy -= 1
    # if mana > max_mana:
    #     mana = max_mana
    # return mana, energy, energy_potions

# run cases
mana, max_mana, energy, energy_potions = 0, 10, 3, 0 # -> 9, 0, 0 🚀
#mana, max_mana, energy, energy_potions = 0, 12, 0, 1 # -> 12, 46, 0 🚀
#mana, max_mana, energy, energy_potions = 1, 100, 33, 2 # -> 100, 0, 2 🚀

# submit cases
#mana, max_mana, energy, energy_potions = 0, 0, 0, 0 # -> 0, 0, 0 🚀
#mana, max_mana, energy, energy_potions = 1000, 1000, 200, 5 # -> 1000, 200, 5 🚀
#mana, max_mana, energy, energy_potions = 0, 10, 0, 2 # -> 10, 46, 1 🚀
#mana, max_mana, energy, energy_potions = 5, 2000, 200, 3 # -> 1055, 0, 0 🚀

while mana < max_mana and (energy > 0 or energy_potions > 0):
    if energy == 0:
        energy += 50
        energy_potions -= 1
        #print(f"energy (+50): {energy}, energy potions (-1): {energy_potions}")
        #print("========================================")
    #print(f"current mana: {mana} (max {max_mana}), current energy: {energy}, energy potions: {energy_potions}")
    #print("meditating...")
    mana += 3
    energy -= 1
    if mana > max_mana:
        mana = max_mana
        #print(f"mana (+3): {mana} (max {max_mana} exceeded!), energy (-1): {energy}")
        #print("========================================")
#print(f"final -> mana: {mana}, energy: {energy}, energy potions: {energy_potions}")





def can_withstand_blow(hero_armor, enemy_damage):
    result = hero_armor >= enemy_damage
    return result


print(can_withstand_blow(3, 2))
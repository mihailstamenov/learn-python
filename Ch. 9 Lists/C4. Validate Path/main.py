def validate_path(expected_path, character_path):
    hero = character_path[0]
    path = character_path[1::]
    match = 0

    for i in range(len(expected_path)):
        if path[i] == expected_path[i]:
            match += 1
    match_percentage = match / len(expected_path) * 100
    return hero, match_percentage

# expected_path = ["A", "B", "C", "D"]
# character_path = ["Hero123", "A", "C", "B", "D"]
# name, percent = validate_path(expected_path, character_path)
# print(name, percent)
# prints: Hero123, 50.0

# print(f"{character_path[0]}, {match_percentage}")
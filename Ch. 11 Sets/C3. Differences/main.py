def find_missing_ids(first_ids, second_ids):
    first = set(first_ids)
    missing = []
    for id in first:
        if id not in second_ids:
            missing.append(id)
    return missing

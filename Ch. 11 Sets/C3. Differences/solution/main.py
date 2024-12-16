def find_missing_ids(first_ids, second_ids):
    s1 = set(first_ids)
    s2 = set(second_ids)
    return list(s1 - s2)
def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    # Don't touch above this line
    unpurchased_items = []
    receipt = {}
    total = 0
    for key in pinned_list:
        if key not in items_purchased:
            unpurchased_items.append(key)
    for key in items_purchased:
        receipt[key] = item_prices[key]
        total += item_prices[key]
    return unpurchased_items, receipt, total

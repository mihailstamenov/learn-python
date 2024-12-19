def area_sum(rectangles):
    sum = 0
    for rect in rectangles:
        sum = sum + (rect["height"] * rect["width"])
    return sum
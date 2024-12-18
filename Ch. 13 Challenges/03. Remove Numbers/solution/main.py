def remove_nonints(nums):
    ints = []
    for item in nums:
        if type(item) == int:
            ints.append(item)
    return ints

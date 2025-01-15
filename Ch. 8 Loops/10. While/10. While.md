# While
Python has another type of loop, the `while` loop. It's a loop that continues `while` a condition remains `True`. The syntax is simple:

```python
while 1:
    print("1 evaluates to True")

# prints:
# 1 evaluates to True
# 1 evaluates to True
# (...continuing)
```
The example above is hardcoded to continue forever, creating an infinite loop. Typically, a `while` loop condition is a comparison or variable, and it determines when the loop ends:

```python
num = 0
while num < 3:
    num += 1
    print(num)

# prints:
# 1
# 2
# 3
# (the loop stops when num >= 3)
```

## Assignment
In `Fantasy Quest`, player characters regenerate health when standing still while away from enemies. This means they will gain health but can't run from enemies that are coming towards them while regenerating.

Complete the `regenerate` function using a `while` loop. It takes `current_health`, `max_health` and `enemy_distance` integers.

- While regenerating health, a character gains `1` health each iteration until it reaches the `max_health` amount.
- The `enemy_distance` shortens by `2` for each iteration.
- If an enemy is at a distance of `3` or less from the character, the character stops gaining health.

Return the new current_health after health regeneration stops.
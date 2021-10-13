some_builds = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]

n = len(some_builds)     # числа этажей
m = len(some_builds[0])  # число зданий

heights = []


for building_number in range(m):
    height = 0
    for floor_number in range(n):
        height += some_builds[floor_number][building_number]
    heights.append(height)

max_height = max(heights)

result = (heights.index(max_height) + 1, max_height)

print(result)
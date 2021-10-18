some_builds = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]

heights = []

for elem in zip(*some_builds):
    heights.append(sum(elem))

max_height = max(heights)

result = (heights.index(max_height) + 1, max_height)

print(result)
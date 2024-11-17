x, y, z = map(int, input().strip().split())
remaining_weight = z - y
if remaining_weight < 0:
    print(0)
else:
    max_mangoes = remaining_weight // x
    print(max_mangoes)

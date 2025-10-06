g = {}
while True:
    try:
        item = input().upper()
        if item in g:
            g[item] += 1
        else:
            g[item] = 1
    except EOFError:
        break

for i in sorted(g):
    print(f"{g[i]} {i}")


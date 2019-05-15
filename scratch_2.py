import json
a = '{"roomsize" : [5, 5], "coords" : [1, 2], "patches" : [[1, 0], [2, 2], [2, 3]], "instructions" : "ENWSSSS"}'
b = json.loads(a)
max = b["roomsize"]
present = b["coords"]
patchs = b["patches"]
direction = b["instructions"]
cleared = 0
for d in patchs:
    if present == d:
        patchs.remove(d)
        cleared+= 1
for c in direction:
    if c == 'E':
        if present[0] != max[0]:
            present[0]+= 1
            for d in patchs:
                if present == d:
                    patchs.remove(d)
                    cleared+= 1
        else:
            continue
    if c == 'W':
        if present[0] == 0:
            continue
        else:
            present[0]-= 1
            for d in patchs:
                if present == d:
                    patchs.remove(d)
                    cleared+= 1
    if c == 'N':
        if present[1] != max[1]:
            present[1]+= 1
            for d in patchs:
                if present == d:
                    patchs.remove(d)
                    cleared+= 1
        else:
            continue
    if c == 'S':
        if present[1] == 0:
            continue
        else:
            present[1]-= 1
            for d in patchs:
                if present == d:
                    patchs.remove(d)
                    cleared+= 1
out = {"coords" : present, "patches" : cleared}
print(out)
def permute(idx, value):
    if idx == len(value):
        print(''.join(value))
        return
    for i in range(idx, len(value)):
        value[i], value[idx] = value[idx], value[i]
        permute(idx + 1, value)
        value[i], value[idx] = value[idx], value[i]


permute(0, list('abc'))
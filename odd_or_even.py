def numbers(cmd, *args):
    odd = [x for x in args if x % 2 != 0]
    even = [x for x in args if x % 2 == 0]

    if cmd == 'Odd':
        return sum(odd) * len(args)

    if cmd == 'Even':
        return sum(even) * len(args)


command = input()
nums = [int(x) for x in input().split()]

print(numbers(command, *nums))
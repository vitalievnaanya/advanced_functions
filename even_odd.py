def even_odd(cmd, *args):
    odd = [int(x) for x in args if int(x) % 2 != 0]
    even = [int(x) for x in args if int(x) % 2 == 0]

    if cmd == '"odd"':
        print(odd)
    elif cmd == '"even"':
        print(even)


argss = input().split(', ')
command = argss[-1]
argss.pop()
even_odd(command, *argss)

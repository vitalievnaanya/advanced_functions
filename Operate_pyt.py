def operate(opr, n, *args):
    result = n
    for n in args:
        if opr == '+':
            result += n
        elif opr == '-':
            result -= n
        elif opr == '*':
            result *= n
        elif opr == '/':
            result /= n
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
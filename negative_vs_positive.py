def positive(*args):
    positive_sum = 0
    for n in args:
        if n > 0:
            positive_sum += n
    return positive_sum


def negative(*args):
    negative_sum = 0
    for n in args:
        if n < 0:
            negative_sum += n
    return negative_sum


n = input().split()
nums = [int(x) for x in n]

print(negative(*nums))
print(positive(*nums))

if positive(*nums) > abs(negative(*nums)):
    print(f'The positives are stronger than the negatives')
else:
    print(f'The negatives are stronger than the positives')

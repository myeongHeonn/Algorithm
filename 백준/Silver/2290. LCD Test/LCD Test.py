import sys
input = sys.stdin.readline

s, n = map(int, input().split())
h, v = '-', '|'
n = str(n)

def construct_segment(number):
    lcd = [[' ']*(s+2) for _ in range(2*s + 3)]
    for i in range(1, s+1):
        if number in '02356789':
            lcd[0][i] = h # a
        if number in '01234789':
            lcd[i][-1] = v # b
        if number in '013456789':
            lcd[-1-i][-1] = v # c
        if number in '0235689':
            lcd[-1][i] = h # d
        if number in '0268':
            lcd[-1-i][0] = v # e
        if number in '045689':
            lcd[i][0] = v # f
        if number in '2345689':
            lcd[(2*s+3)//2][i] = h
    return lcd

display = [construct_segment(i) for i in n]

for line in zip(*display):
    for r in line:
        print(''.join(r), end=' ')
    print()
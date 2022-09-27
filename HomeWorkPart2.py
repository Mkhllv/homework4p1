height = int(input('Enter the height: '))
# Exercise №5
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h):
        if h == 0 or \
                w == 0 or \
                h == height - 1 or \
                w == h:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for n in range(0, h + 1):
        if h == height - 1 or \
                n == h or \
                h == n - 1 or \
                n == h:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Exercise №6
print()
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for q in range(0, h):
        print('*', end=' ')
    print()

# Exercise №7
print()
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for q in range(0, h):
        print('*', end=' ')
    print()
for h in range(0, height):
    for i in range(0, h + 1):
        print(' ', end=' ')
    for w in range(height, h + 1, -1):
        if h == w or \
                w == height or \
                h == w - 1 or \
                w == h:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for n in range(h + 1, height - 1):
        if h == height or \
                n == height - 2 or \
                h == n or \
                n == h:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# Exercise №8
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for q in range(0, h):
        print('*', end=' ')
    print()
for h in range(0, height):
    for i in range(0, h + 1):
        print(' ', end=' ')
    for w in range(height - 1, h, -1):
        if h == w or w == height - 1 or h == w - 1 or w == h + 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for n in range(height - 3, h - 1, -1):
        if h == n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

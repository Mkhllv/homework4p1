height = int(input('Enter the height: '))
# Exercise №1
for h in range(0, height):
    for w in range(0, h + 1):
        print('*', end=' ')
    print()
for h in range(height, 0, -1):
    for w in range(0, h - 1):
        print('*', end=' ')
    print()

# Exercise №2
for h in range(height, 0, -1):
    for i in range(h, height):
        print(' ', end=' ')
    for w in range(0, h):
        print('*', end=' ')
    for q in range(0, h - 1):
        print('*', end=' ')
    print()

# Exercise №3
print()
for h in range(0, height):
    for a in range(0, height):
        print(' ', end=' ')
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    print()
for h in range(0, height - 1):
    for a in range(0, height):
        print(' ', end=' ')
    for i in range(0, h + 1):
        print(' ', end=' ')
    for w in range(h, height - 1):
        print('*', end=' ')
    print()

# Exercise №4
print()
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for q in range(0, h):
        print('*', end=' ')
    print()


def smaller_base(base):
    if str(base)[0] == '5':
        return int('2' + str(base)[1:])
    return base / 2

def X(base, i):
    if i == 0 or base == 1:
        return 1
    if base == 2:
        return int(i / 2) + 1

    count = 0
    while i >= 0:
        count += X(smaller_base(base), i)
        i -= base
    return count

print X(200, 200)


def J(start, stop, base):
    if base == 1:
        return 1
    count = 0
    for i in xrange(start, stop, base):
        count += J(i, stop, smaller_base(base))
    return count

print J(0, 201, 200)

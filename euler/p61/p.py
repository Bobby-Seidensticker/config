import sys


def p(x, n):
    return int(n * (n / 2.0 * (x - 2) + (4-x)/2.0))

print 'tris:', [p(3, n) for n in xrange(1, 6)]
print 'quads:', [p(4, n) for n in xrange(1, 6)]
print 'pents:', [p(5, n) for n in xrange(1, 6)]
print 'hex:', [p(6, n) for n in xrange(1, 6)]
print 'hept:', [p(7, n) for n in xrange(1, 6)]
print 'oct:', [p(8, n) for n in xrange(1, 6)]

all_nums = [[p(x, n) for n in xrange(2, 150)] for x in xrange(0, 9)]
all_indexes = []
for nums in all_nums:
    d = {}
    for n in nums:
        upper = n / 100
        lower = n % 100
        if upper not in d:
            d[upper] = []
        d[upper].append(lower)
    all_indexes.append(d)


def chunk(rem, n):
    for r in rem:
        new_rem = [x for x in rem if x != r]

        nums = all_nums[r]
        i = 0
        while nums[i] < 1000:
            i += 1
        upper = n / 100
        lower = n % 100
        while nums[i] < 10000:
            if nums[i] / 100 == lower:
                for cur in chunk(new_rem, nums[i]):
                    if len(cur) >= len(new_rem):
                        yield [n] + cur
            i += 1
    yield [n]


#rem = range(7, 2, -1)
#r = 8
r = 8
rem = range(r - 1, 2, -1)
i = 0
nums = all_nums[r]

while nums[i] < 1000:
    i += 1

while nums[i] < 10000:
    for cur in chunk(rem, nums[i]):
        if len(cur) >= len(rem):
            if cur[0] / 100 == cur[-1] % 100:
                print 'fuck yeah!', cur, sum(cur)
                sys.exit(-1)
    i += 1

'''        
    lower = n % 100
    upper = (n - lower) / 100
    #for num in all_nums:
'''

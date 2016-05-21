
class Fraction(object):
    def __init__(self, num, dem):
        self.num = int(num)
        self.dem = int(dem)

    def add_int(self, i):
        self.num += int(i) * self.dem

    def inv(self):
        tmp = self.num
        self.num = self.dem
        self.dem = tmp

    def __str__(self):
        return str(self.num) + '/' + str(self.dem)

    def num_more_digits(self):
        return len(str(self.num)) > len(str(self.dem))


def rep(i):
    f = Fraction(1, 2)
    for x in xrange(i):
        f.add_int(2)
        f.inv()
    f.add_int(1)
    return f

count = 0
for i in xrange(1000):
    if rep(i).num_more_digits():
        count += 1

print count

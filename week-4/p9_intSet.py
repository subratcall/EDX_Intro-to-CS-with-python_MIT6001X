class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, set):
        inters = intSet()
        for val in self.vals:
            if set.member(val):
                inters.insert(val)
        return inters

    def __len__(self):
        count=0
        for val in self.vals:
            count +=1
        return count

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


x = intSet()
x.insert(1)
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(5)

y = intSet()
y.insert(1)
y.insert(3)
y.insert(4)

print(intSet.intersect(x, y))
print(len(x))

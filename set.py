class Set:

    arr = []

    def __init__(self, lista):

        self.arr = lista

    def __xor__(self, other):

        r1 = self - other
        r2 = other - self
        return Set(r1 + r2)

    def __and__(self, other):

        r = []
        for i in self.arr:
            found = False
            for j in other.arr:
                if i == j:
                   found = True
            if found is True:
               r.append(i)
        return r

    def __add__(self, other):

        r = []
        for i in other.arr:
            r.append(i)

        for i in self.arr:
            found = False
            for j in other.arr:
                if i == j:
                   found = True
            if found is False:
                r.append(i)
        return r

    def __sub__(self, other):

        r = []
        for i in self.arr:
            found = False
            for j in other.arr:
                if i == j:
                   found = True
            if found is False:
                r.append(i)
        return r

    def contains(self, x):
        found = False
        for i in self.arr:
            if i == x:
               found = True
        return found

    def __str__(self):
        return str(self.arr)

ob1 = Set([0,1,2,3,4,5,-1])
ob2 = Set([5,6,7,8,9,0])
ob3 = ob1 - ob2
ob33 = ob2 - ob1
ob4 = ob1 + ob2
ob5 = ob1 & ob2
ob6 = ob1 ^ ob2
print(type(ob6))
print("A = ", ob1)
print("B = ", ob2)
print("Difference A - B: ", ob3)
print("Difference B - A: ", ob33)
print("Union:", ob4)
print("Intersection: ", ob5)
print(ob2.contains(1))
print("Symmetric Diff: ", ob6)

from math import sqrt
class Vector:
    def __init__(self, x, y, z):
        if not all(isinstance(coords, (int, float)) for coords in (x, y, z)):
            raise ValueError("Координати повинні бути числового типу")
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Вектор({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x, self.y == other.y, self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, other):
        return self.__mul__(other)

    def __len__(self):
        return int(sqrt(self.x **2 + self.y**2 + self.z**2))

    def __int__(self):
        return int(self.__len__())

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)


    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Індекс вектора поза діапазоном")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Індекс вектора поза діапазоном")

    def __contains__(self, value):
        return value in (self.x, self.y, self.z)

    def __bool__(self):
        return bool(self.__len__())

    def __call__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print("v1 =", v1)
    print("v2 =", v2)
    print("v1 == v2:", v1 == v2)
    print("v1 != v2:", v1 != v2)

    v3 = v1 + v2
    print("v1 + v2 =", v3)

    v4 = v1 - v2
    print("v1 - v2 =", v4)

    v1 += v2
    print("v1 += v2 =", v1)
    v1 -= v2
    print("v1 -= v2 =", v1)

    print("v1 * v2 =", v1 * v2)
    print("v1 * 2 =", v1 * 2)
    print("2 * v1 =", 2 * v1)

    print("Length of v1:", len(v1))
    print("Int length of v1:", int(v1))
    v5 = -v1
    print("-v1 =", v5)

    print("v1[0] =", v1[0])
    print("v1[1] =", v1[1])
    print("v1[2] =", v1[2])
    v1[0] = 10
    print("Modified v1[0] =", v1[0])

    print("2 in v1:", 2 in v1)
    print("10 in v1:", 10 in v1)

    print("bool(v1):", bool(v1))
    print("bool(Vector(0, 0, 0)):", bool(Vector(0, 0, 0)))

    v6 = v1(3)
    print("v1(3) =", v6)

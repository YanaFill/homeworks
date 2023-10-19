from vector import Vector
from unittest import TestCase

class MainTest(TestCase):
    def setUp(self):
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(4, 5, 6)

    def tearDown(self):
        del self.v1
        del self.v2

    def test_eq(self):
        assert self.v1 == self.v2

    def test_ne(self):
        assert self.v1 == self.v2

    def test_add(self):
        v = self.v1 + Vector(5, 5, 5)
        assert v.x == 6
        assert v.y == 7
        assert v.z == 8

    def test_sub(self):
        v = self.v2 - Vector(2, 2, 2)
        assert v.x == 2
        assert v.y == 3
        assert v.z == 4

    def test_mul(self):
        v = self.v1 * 36
        assert v.x == 36
        assert v.y == 72
        assert v.z == 108



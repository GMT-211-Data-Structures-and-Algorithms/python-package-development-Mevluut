import unittest
import math
from Point import point
from Line import line, read_points

class TestPoint(unittest.TestCase):
    def test_distance(self):
        p1 = point(0, 0)
        p2 = point(3, 4)
        self.assertEqual(p1.distance(p2), 5)

    def test_get_enlem(self):
        p = point(10, 20)
        self.assertEqual(p.get_enlem(), 10)

    def test_get_boylam(self):
        p = point(10, 20)
        self.assertEqual(p.get_boylam(), 20)

class TestLine(unittest.TestCase):
    def test_perpendicular_distance(self):
        p1 = point(0, 0)
        p2 = point(4, 0)
        line_obj = line([p1, p2])
        p3 = point(2, 3)
        self.assertEqual(line_obj.perpendicular_distance(p3), 3)

    def test_get_points(self):
        p1 = point(0, 0)
        p2 = point(4, 0)
        line_obj = line([p1, p2])
        self.assertEqual(line_obj.get_points(), [p1, p2])

    def test_str(self):
        p1 = point(0, 0)
        p2 = point(4, 0)
        line_obj = line([p1, p2])
        self.assertEqual(str(line_obj), "Line '' with 2 points")
    
    def test_read_points(self):
        # Create a temporary file with point data
        filename = "test_points.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("point\n")
            f.write("2\n")
            f.write("10,20,okul\n")
            f.write("30,40,park\n")
        points = read_points(filename)
        self.assertEqual(len(points), 2)
        self.assertEqual(points[0].get_enlem(), 10)
        self.assertEqual(points[0].get_boylam(), 20)
        self.assertEqual(points[1].get_enlem(), 30)
        self.assertEqual(points[1].get_boylam(), 40)


if __name__ == '__main__':
    unittest.main()    
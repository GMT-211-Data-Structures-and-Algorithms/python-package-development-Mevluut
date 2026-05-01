from Point import point
class line:
    """Represents a line consisting of multiple points."""

    def __init__(self, points, name=""):
        """
        :param points: List of point objects forming the line
        :param name: Optional name for the line
        """
        self.points = points
        self.name = name

    def __str__(self):
        """Returns string representation of the line."""
        return "Line '{}' with {} points".format(self.name, len(self.points))

    def get_points(self):
        """Returns the list of points in the line.
        
        :return: List of point objects
        :rtype: list
        """
        return self.points


def read_points(filename):
    """Reads points from a text file.
    
    :param filename: Path to the input file
    :type filename: str
    :return: List of point objects
    :rtype: list
    """
    points = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    count = int(lines[1])
    for i in range(count):
        parts = lines[2 + i].split(",")
        x = float(parts[0])
        y = float(parts[1])
        name = parts[2] if len(parts) > 2 else ""
        points.append(point(x, y, name))

    return points


def read_lines(filename):
    """Reads lines from a text file.
    
    :param filename: Path to the input file
    :type filename: str
    :return: List of line objects
    :rtype: list
    """
    line_objects = []
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read().splitlines()

    count = int(raw[1])
    idx = 2
    for _ in range(count):
        name = raw[idx]
        idx += 1
        pts = []
        while idx < len(raw) and raw[idx] != "" and "," in raw[idx]:
            parts = raw[idx].split(",")
            pts.append(point(float(parts[0]), float(parts[1])))
            idx += 1
        line_objects.append(line(pts, name))

    return line_objects


if __name__ == "__main__":
    print("point1.txt ")
    pts = read_points("point1.txt")
    for p in pts:
        print(p)

    print("\n points2.txt")
    pts = read_points("points2.txt")
    for p in pts:
        print(p)

    print("\nline1.txt ")
    lns = read_lines("line1.txt")
    for l in lns:
        print(l)
        for p in l.get_points():
            print("  ", p)

    print("\nline2.txt")
    lns = read_lines("line2.txt")
    for l in lns:
        print(l)
        for p in l.get_points():
            print("  ", p)
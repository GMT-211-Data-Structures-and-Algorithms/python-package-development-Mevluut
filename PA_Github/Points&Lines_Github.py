class point:
    def __init__(self, x, y, name=""):
        self.enlem = x
        self.boylam = y
        self.name = name

    def get_enlem(self):
        return self.enlem

    def get_boylam(self):
        return self.boylam

    def __str__(self):
        if self.name:
            return "point ({},{}) {}" .format(self.enlem, self.boylam, self.name)  
        return "point ({},{})" .format(self.enlem, self.boylam)


class line:
    def __init__(self, points, name=""):
        self.points = points  
        self.name = name

    def __str__(self):
        return "Line '{}' with {} points".format(self.name, len(self.points))

    def get_points(self):
        return self.points


def read_points(filename):
    points = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    
    count = int(lines[1])# lines[0] = "point", lines[1] = count
    for i in range(count):
        parts = lines[2 + i].split(",")
        x = float(parts[0])
        y = float(parts[1])
        name = parts[2] if len(parts) > 2 else ""
        points.append(point(x, y, name))

    return points


def read_lines(filename):
    line_objects = []
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read().splitlines()

     
    count = int(raw[1]) # raw[0] = "line", raw[1] = count of lines
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
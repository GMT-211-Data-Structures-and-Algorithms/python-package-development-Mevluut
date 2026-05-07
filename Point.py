import math

class point:
    """Represents a point in 2D space with optional name."""

    def __init__(self, x, y, name=""):
        """
        :param x: Latitude (enlem) of the point
        :param y: Longitude (boylam) of the point
        :param name: Optional name for the point
        """
        self.enlem = x
        self.boylam = y
        self.name = name

    def get_enlem(self):
        """Returns the latitude (enlem) of the point.
        
        :return: Latitude value
        :rtype: float
        """
        return self.enlem

    def get_boylam(self):
        """Returns the longitude (boylam) of the point.
        
        :return: Longitude value
        :rtype: float
        """
        return self.boylam

    def distance(self, other):
        """Returns the Euclidean distance between this point and another point.
        
        :param other: The other point
        :type other: point
        :return: Distance between the two points
        :rtype: float
        """
        return math.sqrt((self.enlem - other.enlem) ** 2 + (self.boylam - other.boylam) ** 2)

    def __str__(self):
        """Returns string representation of the point."""
        if self.name:
            return "point ({},{}) {}".format(self.enlem, self.boylam, self.name)
        return "point ({},{})".format(self.enlem, self.boylam)
class Board (object):
    """
    >>> Board.xDim
    2
    >>> Board.yDim
    3
    """

    xDim = 2
    yDim = 3

    @staticmethod
    def setX(x):
        """
        >>> Board.xDim
        2
        >>> Board.setX(10)
        >>> Board.xDim
        10
        """
        Board.xDim = x

    @staticmethod
    def setY(y):
        """
        >>> Board.yDim
        3
        >>> Board.setY(5)
        >>> Board.yDim
        5
        """
        Board.yDim = y

    @staticmethod
    def default():
        """
        >>> Board.setX(4), Board.setY(4)
        (None, None)
        >>> Board.xDim, Board.yDim
        (4, 4)
        >>> Board.default()
        >>> Board.xDim, Board.yDim
        (2, 3)
        """
        Board.xDim = 2
        Board.yDim = 3


class Point1D (object):
    """
    >>> p = Point1D()
    >>> p # doctest:+ELLIPSIS
    <...Point1D object at 0x...>
    """

    def __init__(self, val=0):
        """
        >>> Board.default()
        >>> p = Point1D()
        >>> p.val
        0
        >>> p = Point1D(0)
        >>> p.val
        0
        >>> p = Point1D(4)
        >>> p.val
        4
        """
        self.val = val

    def to2D(self):
        """
        >>> Board.default()
        >>> p1D = Point1D()
        >>> p1D.to2D() # doctest:+ELLIPSIS
        <...Point2D object at 0x...>
        >>> p2D = p1D.to2D()
        >>> p2D.x, p2D.y
        (0, 0)
        >>> p1D = Point1D(4)
        >>> p2D = p1D.to2D()
        >>> p2D.x, p2D.y
        (1, 1)
        >>> for x in range(Board.xDim * Board.yDim):
        ...     p1D = Point1D(x)
        ...     p2D = p1D.to2D()
        ...     p2D.x, p2D.y
        (0, 0)
        (0, 1)
        (0, 2)
        (1, 0)
        (1, 1)
        (1, 2)
        >>>
        """
        p2D = Point2D()
        p2D.x = int(self.val / Board.yDim)
        p2D.y = int(self.val % Board.yDim)
        return p2D

    def toGPoint(self):
        """
        >>> Board.default()
        >>> p1D = Point1D()
        >>> p1D.toGPoint() # doctest:+ELLIPSIS
        <...GPoint object at 0x...>
        >>> p = p1D.toGPoint()
        >>> p.x, p.y
        (1, 0)
        >>> p1D = Point1D(4)
        >>> p = p1D.toGPoint()
        >>> p.x, p.y
        (0, 1)
        >>> for x in range(Board.xDim * Board.yDim):
        ...     p1D = Point1D(x)
        ...     p = p1D.toGPoint()
        ...     p.x, p.y
        (1, 0)
        (1, 1)
        (1, 2)
        (0, 0)
        (0, 1)
        (0, 2)
        >>>
        """
        p = GPoint()
        p.x = (Board.xDim - 1) - int(self.val / Board.yDim)
        p.y = int(self.val % Board.yDim)
        return p

    def toString(self):
        """
        >>> Board.default()
        >>> p1D = Point1D(1)
        >>> p1D.toString()
        '1'
        """
        return str(self.val)


class Point2D (object):
    """
    >>> p = Point2D()
    >>> p # doctest:+ELLIPSIS
    <...Point2D object at 0x...>
    """

    def __init__(self, x=0, y=0):
        """
        >>> Board.default()
        >>> p = Point2D()
        >>> p.x, p.y
        (0, 0)
        >>> p = Point2D(1, 2)
        >>> p.x, p.y
        (1, 2)
        """
        self.x = x
        self.y = y

    def to1D(self):
        """
        >>> Board.default()
        >>> p2D = Point2D()
        >>> p1D = p2D.to1D()
        >>> p1D.val
        0
        >>> for x in range(Board.xDim):
        ...    for y in range(Board.yDim):
        ...        p2D = Point2D(x, y)
        ...        p1D = p2D.to1D()
        ...        p1D.val
        0
        1
        2
        3
        4
        5
        """
        p1D = Point1D(self.x * Board.yDim + self.y * (Board.xDim - 1))
        return p1D

    def toGPoint(self):
        """
        >>> Board.default()
        >>> p2D = Point2D()
        >>> p = p2D.toGPoint()
        >>> p.x, p.y
        (1, 0)
        >>> for x in range(Board.xDim):
        ...    for y in range(Board.yDim):
        ...        p2D = Point2D(x, y)
        ...        p = p2D.toGPoint()
        ...        p.x, p.y
        (1, 0)
        (1, 1)
        (1, 2)
        (0, 0)
        (0, 1)
        (0, 2)
        """
        p = GPoint()
        p.x = (Board.xDim - 1) - self.x
        p.y = self.y
        return p

    def toString(self):
        """
        >>> Board.default()
        >>> p2D = Point2D(1, 2)
        >>> p2D.toString()
        '(1, 2)'
        """
        return "({}, {})".format(self.x, self.y)


class GPoint (object):
    """
    >>> p = GPoint()
    >>> p # doctest:+ELLIPSIS
    <...GPoint object at 0x...>
    """

    def __init__(self, x=0, y=0):
        """
        >>> Board.default()
        >>> p = GPoint()
        >>> p.x, p.y
        (0, 0)
        >>> p = GPoint(1, 2)
        >>> p.x, p.y
        (1, 2)
        """
        self.x = x
        self.y = y

    def from1D(self, p1D):
        """
        >>> Board.default()
        >>> p1D = Point1D()
        >>> p = GPoint(1, 1)
        >>> p.x, p.y
        (1, 1)
        >>> p.from1D(p1D)
        >>> p.x, p.y
        (1, 0)
        >>> for x in range(Board.xDim):
        ...    for y in range(Board.yDim):
        ...        p2D = Point2D(x, y)
        ...        p1D = p2D.to1D()
        ...        p.from1D(p1D)
        ...        p.x, p.y
        (1, 0)
        (1, 1)
        (1, 2)
        (0, 0)
        (0, 1)
        (0, 2)
        """
        self.x = (Board.xDim - 1) - int(p1D.val / Board.yDim)
        self.y = int(p1D.val % Board.yDim)

    def from2D(self, p2D):
        """
        >>> Board.default()
        >>> p2D = Point2D()
        >>> p = GPoint(1, 1)
        >>> p.x, p.y
        (1, 1)
        >>> p.from2D(p2D)
        >>> p.x, p.y
        (1, 0)
        >>> for x in range(Board.xDim):
        ...    for y in range(Board.yDim):
        ...        p2D = Point2D(x, y)
        ...        p.from2D(p2D)
        ...        p.x, p.y
        (1, 0)
        (1, 1)
        (1, 2)
        (0, 0)
        (0, 1)
        (0, 2)
        """
        self.x = (Board.xDim - 1) - p2D.x
        self.y = p2D.y

    def to1D(self):
        """
        >>> Board.default()
        >>> p = GPoint()
        >>> p1D = p.to1D()
        >>> p1D.val
        3
        >>> for x in range(Board.xDim):
        ...    for y in range(Board.yDim):
        ...        p = GPoint(x, y)
        ...        p1D = p.to1D()
        ...        p1D.val
        3
        4
        5
        0
        1
        2
        """
        p1D = Point1D()
        p1D.val += ((Board.xDim - 1) - self.x) * Board.yDim
        p1D.val += self.y * (Board.xDim - 1)
        return p1D

    def to2D(self):
        """
        >>> Board.default()
        >>> p = GPoint()
        >>> p2D = p.to2D()
        >>> p2D.x, p2D.y
        (1, 0)
        >>> for x in range(Board.xDim):
        ...    for y in range(Board.yDim):
        ...        p = GPoint(x, y)
        ...        p2D = p.to2D()
        ...        p2D.x, p2D.y
        (1, 0)
        (1, 1)
        (1, 2)
        (0, 0)
        (0, 1)
        (0, 2)
        """
        p2D = Point2D()
        p2D.x = (Board.xDim - 1) - self.x
        p2D.y = self.y
        return p2D

    def toString(self):
        """
        >>> Board.default()
        >>> p = GPoint(1, 2)
        >>> p.toString()
        '(1, 2)'
        """
        return "({}, {})".format(self.x, self.y)


class Cell (object):
    """
    >>> c = Cell()
    >>> c # doctest:+ELLIPSIS
    <...Cell object at 0x...>
    """

    def __init__(self, p1D=None, p2D=None, gpoint=None):
        """
        >>> Board.default()
        >>> c = Cell()
        >>> c.p1D, c.p2D, c.gpoint
        (None, None, None)
        >>> c = Cell(p1D=Point1D(2))
        >>> c.p1D.toString()
        '2'
        >>> c.p2D.toString()
        '(0, 2)'
        >>> c.gpoint.toString()
        '(1, 2)'
        >>> c = Cell(p2D=Point2D(1, 1))
        >>> c.p1D.toString()
        '4'
        >>> c.p2D.toString()
        '(1, 1)'
        >>> c.gpoint.toString()
        '(0, 1)'
        >>> c = Cell(gpoint=GPoint(1, 2))
        >>> c.p1D.toString()
        '2'
        >>> c.p2D.toString()
        '(0, 2)'
        >>> c.gpoint.toString()
        '(1, 2)'
        """
        if p1D:
            self.p1D = p1D
            self.p2D = p1D.to2D()
            self.gpoint = p1D.toGPoint()
        elif p2D:
            self.p1D = p2D.to1D()
            self.p2D = p2D
            self.gpoint = p2D.toGPoint()
        elif gpoint:
            self.p1D = gpoint.to1D()
            self.p2D = gpoint.to2D()
            self.gpoint = gpoint
        else:
            self.p1D = None
            self.p2D = None
            self.gpoint = None


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

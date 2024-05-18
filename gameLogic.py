class Draw:

    def __init__(self, pointers=None):

        # initiaialing variables to be use
        self.gap = 6
        self.X = 0
        self.Y = 0
        self.PointerX = int(500 / 2)
        self.PointerY = int(500 / 2)

        # initialing trace
        if pointers is None:
            self.trace = {(self.PointerX, self.PointerY, 'Black')}
        else:
            self.trace = pointers

    def movement(self, key, color, draw):
        if key == 'Up':
            self.PointerY -= self.gap
            self.X = 0
            self.Y = (-self.gap)
        if key == 'Down':
            self.PointerY += self.gap
            self.X = 0
            self.Y = self.gap
        if key == 'Left':
            self.PointerX -= self.gap
            self.X = (-self.gap)
            self.Y = 0
        if key == 'Right':
            self.PointerX += self.gap
            self.X = self.gap
            self.Y = 0

        # adding co-ordinates
        if draw:
            self.trace.add((self.PointerX, self.PointerY, color))

    def getPointerX(self):
        return self.PointerX

    def getPointerY(self):
        return self.PointerY

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getPaint(self):
        return self.trace

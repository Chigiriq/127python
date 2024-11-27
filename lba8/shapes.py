import math
#----------------------------------------------------------------------#
class Shape:
    """ Shape class that defines a shape with name and shape methods """

    ## constructor
    def __init__(self, init_name):
        self.name = init_name

    ## getters
    def getArea(self):

        #XXX XXX XXX polymorphism XXX XXX XXX ---> allows area to exist in every sub-slass
        pass

    def getName(self):
        return self.name

    ## setters
    def setName(self, n):
        self.name = n

    
#----------------------------------------------------------------------#
class Rectangle(Shape):
    """ Rectangle class that inherits Shape and adds length and width """

    ## constructor
    def __init__(self, init_length, init_width):
        super().__init__("rectangle")                   #goto shape and steal constructor
        self.length = init_length
        self.width = init_width

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getArea(self):
        return self.length * self.width

    ## toString
    def __str__(self):
        return super().__str__() + " with length " + str(self.length) + " and width " + str(self.width)
#----------------------------------------------------------------------#
class Square(Rectangle):
    """ Square class that inherits Rectangle where length is width """

    ## constructor
    def __init__(self, init_side):
        super().__init__(init_side, init_side)         #goto rect and steal constructor
        #what is the name of this object? ...its rectangle
        self.setName("square") #..................now its square

    ## getters
    def getSide(self):
        return self.length

    ## toString
    def __str__(self):
        return self.name + " with side " + str(self.length)
#----------------------------------------------------------------------#
class Circle(Shape):
    """ Circle class that inherits Shape with radius """

    ## constructor
    def __init__(self, init_radius):
        super().__init__("circle")
        self.radius = init_radius

    ## getters
    def getRadius(self):
        return self.radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    ## toString
    def __str__(self):
        return super().__str__() + " with radius " + str(self.radius)
#----------------------------------------------------------------------#
class Triangle(Shape):
    """ Class Triangle that inherits Shape with height and base """

    ## constructor
    def __init__(self, init_height, init_base):
        super().__init__("triangle")
        self.height = init_height
        self.base = init_base

    ## getters
    def getHeight(self):
        return self.height

    def getBase(self):
        return self.base

    def getArea(self):
        return .5 * self.height * self.base

    ## toString
    def __str__(self):
        return super().__str__() + " with height " + str(self.height) + " and base " + str(self.base)
#----------------------------------------------------------------------#
def main():
    rect1 = Rectangle(2,3)
    rect2 = Rectangle(4,5)
    sq1 = Square(6)
    sq2 = Square(8)
    circ1 = Circle(3)
    circ2 = Circle(5)
    tri1 = Triangle(4,5)
    tri2 = Triangle(3,5)

    shapes = [rect1, rect2, sq1, sq2, circ1, circ2, tri1, tri2]
    for shape in shapes:
        print( str(shape) + " has area " + str(shape.getArea()) )
#----------------------------------------------------------------------#
main()

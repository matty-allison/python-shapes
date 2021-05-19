class Shapes:
    def __init__(self, name, side):
        self.name=name
        self.side=side
    def Area(self):
        print("I am a :" + self.name + "\n"+
              "I have " + self.side + " sides")
obj_shapes=Shapes("shapes", "so many")
obj_shapes.Area()

class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length=len1
        self.width=wid1
    def Area(self):
        result=self.length * self.width
        return result
obj_book=Rectangle(10, 7)
print("The area of the book is" + str(obj_book.Area()))
obj_screen=Rectangle(5,7)
print("The area of the screen is " + str(obj_screen.Area()))

class Circle(Shapes):
    def __init__(self,  raduis):
        self.raduis=raduis
    def Area(self):
        result=self.raduis*self.raduis* 3.14
        return result
obj_plate=Circle(10)
print("The area of a circle is ", obj_plate.Area())

class Triangle(Shapes):
    def __init__(self, height, base):
        self.height=height
        self.base=base
    def Area(self):
        result= self.base/2 * self.height
        return result
obj_samoosa=Triangle(8, 20)
print(obj_samoosa.Area())

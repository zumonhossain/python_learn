class Rectangle:
    def __init__(self, width, height):
        self.width = width;
        self.height = height;

    def get_area(self):
        print("Area:", self.width * self.height);

rect1 = Rectangle(5, 3);
rect2 = Rectangle(10, 7);

rect1.get_area();
rect2.get_area();
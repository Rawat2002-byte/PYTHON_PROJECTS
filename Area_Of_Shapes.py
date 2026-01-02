print("AREA OF WHICH SHAPE YOU WANT TO FIND")
print("circle")
print("rectangle")
print("triangle")
def Shape():
    OPTION = input("Enter a Shape")

    if (OPTION in ['circle','rectangle','triangle']):
        if OPTION=='circle':
            class Circle: 
                def __init__(self,radius):
                    self.radius= radius
                
            
                def area(self):
                    return 22/7*self.radius**2
            r = float(input("Enter Radius"))
            c = Circle(r)
            print("Area of a circle:" , c.area())
            
        elif OPTION=='rectangle':
            class rectangle:
                def __init__(self,length,width):
                    self.length= length
                    self.width = width
            
                def area(self):
                    return self.length * self.width

            l = float(input("Enter length"))
            w = float(input("Enter width"))
            L = rectangle(l,w)
            print("Area of a rectangle: ", L.area())
            
        elif OPTION=='triangle':
            class Triangle:
                def __init__(self,height,base):
                    self.height = height
                    self.base = base

                def area(self):
                    return 1/2*self.height * self.base

            b = float(input("Enter base "))
            h = float(input("Enter height"))
            tri = Triangle(b,h)
            print("Area of a Triangle: ",tri.area())
        else:
            print("Invalid shape choose correct shape")

        new_shape = input(f"New shape press 'x' or 'y' to exit. ").lower()

        if new_shape == 'x':
            Shape()
        else:
            print("Thank You for using")
Shape()
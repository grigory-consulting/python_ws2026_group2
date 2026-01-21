


class Point2D:
    """two dimensional point in plane"""
    def __init__(self, xx=0, yy=0):
        self.x = xx
        self.y = yy

    def __str__(self): # strings for humans
        return f"({self.x}, {self.y})"
    
    def __repr__(self): # strings for machines/programs 
        # usually you write something like this
        return f"Point2D(x={self.x}, y= {self.y})" 
    
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)
    
    def shift_x(self, dx): 
        """Shift point alongside the x-axis by the quanitity dx"""
        self.x += dx 

    def shift_y(self,dy):
        self.y += dy
    
    def shift(self,dx,dy):
        self.shift_x(dx)
        self.shift_y(dy) 
    
    def distance_0(self):
        return (self.x**2 + self.y**2)**0.5
     
p1 = Point2D()
p2 = Point2D(2,6)
print([p1], p2) # p1 is in the list -> __repr__
# p2 -> __str__
p2.shift(-1,2)
print(p2+p2+p2)



# help(p1)


import random 

points = []

for i in range(10000):
    points.append(Point2D(xx = random.randint(-10,10), yy = random.randint(-10,10)))

# TODO Count the number of points, that have distance to zero > 5. 

print(points[1].distance_0())

count = 0
for point in points:
    if point.distance_0()>5.0:
        count+=1
print(count)

print(len([point for point in points if point.distance_0()>5.0]))


class Point3D(Point2D): # Point3D ... subclass, Point2D ... superclass

    def __init__(self, xx, yy, zz):
        super(Point2D).__init__(xx,yy) # Constructor call from Point2D
        self.z = zz             # Extension with new attribute
        
    def __str__(self): 
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self): 
        return f"Point3D(x={self.x}, y= {self.y}, z= {self.z})" 
    
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def shift_z(self, dz):
        self.z += dz
    
    def shift(self,dx,dy,dz):
        super().shift(dx,dy)
        self.shift_z(dz)
    
    def distance_0(self):
        # return (self.x**2 + self.y**2)**0.5 for Point2D
        return (self.x**2 + self.y**2 + self.z**2 )**0.5 # for Point3D
        #dist = super().distance_0()
        #return (dist**2 + self.z**2)**0.5 


## Multiple Inheritance 

class A:
    def methodA(self):
        print("Method from A")

class B:
    def methodB(self):
        print("Method from B")
    
class C(A,B):
    pass

obj = C()
obj.methodA()
obj.methodB()


print("--------------------------")

class A:
    def method(self):
        print("Method from A")

class B:
    def method(self):
        print("Method from B")
    
class C(B,A):
    pass

obj = C()
obj.method()

print(C.mro()) # method resolution order 



### Diamond problem

class A:    # base
    def show(self):
        print("A.show")

class B(A): # parent 1
    def show(self):
        print("B.show")
        super().show()

class C(A): # parent 2
    def show(self):
        print("C.show")
        super().show()
    
class D(C,B): # child 
    def show(self):
        print("D.show")
        super().show() 

d = D()
d.show()

print(D.mro())
class Cuboid():
    # pass
    # Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume
    def __init__(self,x,y,z):

        self.x = x
        self.y = y
        self.z = z



    def get_surface(self):
        # surface = (2*self.x*self.z) + (2*self.z*self.y) + (2*self.y*self.x)
        surface = 2 * (self.x*self.y + self.x*self.z + self.y*self.z)

        return surface

    def get_volume(self):

        volume = self.x * self.y * self.z

        return volume






box = Cuboid(10, 20, 30)

print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000


# A = 2wl + 2lh + 2hw.  w=x h=y l=z 
# V = l × w × h

import math
def escvel(G,M,R):
       x=G*M
       y=x/R
       z=math.sqrt(y)
       return z
a=float(input("Enter the gravitrational constant of the planet"))
b=float(input("Enter the Mass of the planet"))
c=float(input("Enter the Radius of the planet"))
d = escvel(a, b, c)
print("Escape velocity from the surface of the planet:", d, "m/s")
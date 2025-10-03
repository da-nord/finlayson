import math

#114 1 rectangle
#Calculate the area
#Prompt user enter length width
#then calculate and print the area

print("what is the surface area in meters?")
l=int(input("give the length of the rectangle "))
w=int(input("give the width of the rectangle "))

print(f"the surface area is: length {l} * width {w} =" , l*w , "square meter")

#114 2 circle
#Calculate the area
#Prompt user enter radius
#then calculate and print the area
#import math then typing in math.pi

print("what is the surface area in meters of the circle?")
r=int(input("give the radius of the circle"))
area = math.pi * (r ** 2)
print(f"surface area is {r} ** 2 =", area)


#114 3 triangle
#Calculate the area
#prompt user enter base
#prompt user enter height
#then calculate and print the area

print("what is the surface area in meters of the triangle")
b=int(input("give the base"))
h=int(input("give the height"))


print(f"the surface area of the triangle is: base {b} * height {w} then the result divided by 2 =" , (b*h)/2 , "square meter")


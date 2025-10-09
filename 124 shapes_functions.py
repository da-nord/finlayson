import math
def l():
    print (" ")

#124.11 ___________________________________________________________________
# Define the rectangle, circle, and triangle area calculations as functions
#rectangle
l()
def rectangle_surface(l,w):
    s=l*w
    print(f"surface area is", s)
def rectangle():
    l=int(input("give the length of the rectangle "))
    w=int(input("give the width of the rectangle "))
    rectangle_surface(l,w)
    main()

def circle_surface(r):
    s=r**2*math.pi
    print(f"surface area is", s)
def circle():
    r=int(input("give radius circle "))
    circle_surface(r)
    main()
    
def triangle_surface(b,h):
    s=(b*h)/2
    print(f"surface area is", s)
def triangle():
    b=int(input("give base triangle "))
    h=int(input("give height triangle "))
    triangle_surface(b,h)
    main()


#124.12 ____________________________________
# create function namedsquare_perimeter that 
# takes the side length of a square and returns its perimeter
# perimeter of the square is defined as the total length of the boundary of a square
l()
def namedsquare_perimeter(l):
    s=l*4
    print(f"perimeter of the square is ", s)
def square():
    l=int(input("give side of square "))
    namedsquare_perimeter(l)
    main()

# 124.13 ___________________________
# write function namedcircle_details 
# that takes the radius of a circle as its only argument and 
# prints out both circumference and area circle
def namedcircle_details(r):
    o=r**2*math.pi
    c=r*2*math.pi
    print(f"surface area is ", o)
    print(f"circumference is ", c)
def circle_both():
    r=int(input("give radius circle "))
    namedcircle_details(r)
    main()

# 124.14
# write function namedgeometry that 
# takes side of square and radius circle 
# function should print which shape has a 
# larger perimeter circumference and 
# which shape has a larger area
def namedgeometry(s,r):
    #sop squarearea 
    # cop circlearea 
    #som square circumference
    #com circle circumference
    sop=s**2 
    cop=r**2*math.pi
    som=s*4
    com=r*2*math.pi
    print(f"square area is ", sop )
    print(f"circle area is ", cop )
    if sop>cop:
        print("the area of the square is larger")
    elif sop<cop:
        print("the area of the circle is larger")
    else:
        print("both the same")
        l()    
    print(f"square circumference is ", som)
    print(f"circle circumference is ", com)
    if som>com:
        print("the perimeter of the square is larger")
    elif som<com:
        print("the perimeter of the circle is larger")
    else:
        print("both the same")
def circle_both():
    s=int(input("give side square "))
    r=int(input("give radius circle "))
    print(" ")
    namedgeometry(s,r)
    main()



def main():
    print("r--- rectangle")
    print("c--- circle")
    print("t--- triangle")
    print("v---- perimeter")
    print("b--- circle both")
    print("z--- square circle ")
    choice=input("make choice ")
    if choice=="r":
        rectangle()
    elif choice=="c":
        circle()
    elif choice=="t":
        triangle()
    elif choice=="v":
        square()
    elif choice=="b":
        circle_both()
    elif choice=="z":
        circle_both()

main()





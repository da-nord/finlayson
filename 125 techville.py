#125 TECHVILLE
#if x==True print hello print bye

def move_forward():
    print("moving forward")
def turn(direction):
    print(f"turning {direction}")
def start_engine():
    print("starting engine")
def stop_engine():
    print("stopping engine")
def follow_roundabout(exit_number):
    print("you are at a roundabout ")
    print("choose:")
    print("hospital: 1")
    print("mall: 2")
    print("airport: 3")
    print("university: 4")
    print("stadium: 4 ")
    #exit_number=int(input("which exit number"))
    print(f"taking exit number {exit_number} from the roundabout")
    if exit_number==1:
        print("turn right")
    elif exit_number==2:
        print("move forward")
        print("turn right")
    elif exit_number==3:
        print("move forward")
        print("move forward")
        print("turn right")
    elif exit_number==4:
        print("move forward")
        print("move forward")
        print("move forward")
        i=input("stadium s or university u")
        if i=="s":
            print("turn right")            
            print("stadium")
        elif i=="u":
            print("turn left")            
            print("university")
        else:
            print("choose s or u")

#suggestion hint   if x in [val1, val2, val3]:  

def library():
    start_engine()
    move_forward()
    turn("left")
    print("you are at the library ")
    stop_engine()
def techpark():
    start_engine()
    move_forward()
    turn("right")
    print("you are at the techpark ")
    stop_engine()
def hospital():
    start_engine()
    move_forward()
    move_forward()
    follow_roundabout(exit_number)
    turn("right")
    print("you are at the hospital ")
    stop_engine()
def mall():
    start_engine()
    move_forward()
    move_forward()
    exit_number=int(input("which exit number"))
    follow_roundabout(exit_number)
    turn("right")
    print("you are at the mall ")
    stop_engine()
def airport():
    start_engine()
    move_forward()
    move_forward()
    exit_number=int(input("which exit number"))
    follow_roundabout(exit_number)
    turn("right")
    print("you are at the airport ")
    stop_engine()
def university(): 
    print("so your are heading for the university ")
    start_engine() 
    move_forward()
    move_forward()
    print("this is a roundabout")
    exit_number=int(input("give exit"))
    follow_roundabout(exit_number)
    turn("right")
    move_forward()
    turn("left")
    print("you are at the university ")
    stop_engine()
def stadium():
    start_engine()
    move_forward()
    move_forward()
    print("this is a round_about")
    exit_number=int(input("give exit"))
    follow_roundabout(exit_number)
    move_forward()
    turn("right")
    print("you are at the stadium ")
    stop_engine()

#---------------------------

def main():
    print("DESTINATIONS")
    print("a--- airport")
    print("h--- hospital")
    print("l--- library")
    print("m--- mall")
    print("s--- stadium")
    print("t--- techpark")
    print("u--- university")
    choice=input("make choice ")
    if choice=="a":
        airport()
    elif choice=="h":
        hospital()
    elif choice=="l":
        library()
    elif choice=="m":
        mall()
    elif choice=="s":
        stadium()
    elif choice=="t":
        techpark()
    elif choice=="u":
        university()
    else:
        print("follow menu please")

main()

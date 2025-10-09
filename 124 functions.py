#124 assignment three
#functions.py
# school>$chool  school>echool

def l():
    print(" ")

#124.1 __________124.1____________________________________________________________
#124.1 create function dollarizer takes word replaces every s with $ and output it
def dollarizer():
    #119
    l()
    print("this is task 124.1")
    s=input("give a word with an s in it ")
    s_r=s.replace("s","$")
    print(f"you typed ",s,"all the s will be replaced by $ ","   there you go:   ",s_r)
    l()
    main()

#124.2 __________124.2__________
#124.2 eurizer replaces e with €
def eurizer():
    #119
    l()
    print("this is task 124.2")
    e=input("give a word with an e in it ")
    e_r=e.replace("e","€")
    print(f"you typed ",e,"all the e will be replaced by € ","   there you go:   ",e_r)
    l()
    main()

#124.3 ________________________________________________
#124.3 combine dollarizer and eurizer function into one
#124.3 more general function called replacer
#124.3 that takes a word and 2 characters as input and replaces every occurrence of character 1 with character 2
def replacer():
    #119
    l()
    print("this is task 124.3")
    r=input("give a word  ")
    character_one=input("give one character in the word ")
    character_two=input("type replacer ")
    print(f"character ",character_one,"will be replaced with", character_two)
    r_r=r.replace(character_one,character_two)
    print(f"look: ",r_r)
    l()
    main()  

#124.4 _________________________________________
#124.4 create function wonky_text that replaces:
#124.4 every s with $
#124.4 every e with € 
#124.4 every l with £  
def wonkey_text():
    #119
    l()
    print("this is task 124.4")
    r=input("give a word with characters e  l  s ")
    r=r.replace("s","$")
    r=r.replace("e","€")
    r=r.replace("l","£")
    print(f"the great replacement: ",r)
    l()
    main()  

#124.5 ______________________________________________________________________________
#124.5 create function namedcelsius_to_fahrenheit that takes a temperature in celsius 
#124.5 and returns its equivalent in fahrenheit use the formula  F = C * 9/5 + 32
# www.geeksforgeeks.org/python/python-program-to-convert-celsius-to-fahrenheit
# def namedcelsius_to_fahrenheit():
    l()
    c=float(input("give a temperature in celsius "))
    f=(c*9/5) +32
    print(f"you typed ",c,"degrees celcius ","that is ",f,"degrees fahrenheit")
    main()
    

#124.6 create a function namedage_in_days that
#124.6 takes an age in years (assume whole years only) and 
#124.6 returns the age in days (ignore leap years) 
#124.6 assume each year has 365 days.
def namedage_in_days():
    c=int(input("how old are you? "))
    print(f"so you are ",c,"years old ", "that is ", c*365, "days")

#124.7 _______________________________________
#124.7 create function namedsimple_interest that 
#124.7 calculates simple interest
#124.7 it should take three arguments: 
#124.7 principal amount   rate of interest   time in years 
#124.7 use formula:  ( SI = P * R * T ) 
#124.7 return the calculated simple interest
def namedsimple_interest(p, r, t):
    s=p*r*t
def interest():
    #c=int(input("how old are you? "))
    p=int(input("how much to lend "))
    r=int(input("at what % rate "))
    t=int(input("for how many years "))
    s=int(p*r/100*t)
    namedsimple_interest(p, r, t)
    print(f"you lend ",p, "against ", r,"% ","over ",t,"years")
    print(f"the money amount of interest is ",s)
    
#124.8 _________________________________  
# write function namedplan_finances that 
# takes principal amount, interest rate, time in years and a 
# desired final amount after simple interest 
# function should return whether the final amount after simple interest 
# is achieved from the principal within the given time and rate
def namedplan_finances(p, r, t, g ):
    s=p*r*t
def goal_amount():
    p=int(input("how much to lend "))
    r=int(input("at what % rate "))
    t=int(input("for how many years "))
    g=int(input("what is the limit of the interest amount "))
    s=int(p*r/100*t)
    namedplan_finances(p, r, t, g)
    print(f"you lend ",p, "against ", r,"% ","over ",t,"years")
    print(f"the money amount of interest is ",s)
    print(f"the limit amount of interest was ",g)
    if g>s:
        print("you payed ", g-s, "interest too much")
    elif g<s:
        print("you payed ", s-g, "interest less than the limit")
    else:
        print("all well")
        l()    




    

    



#  -------------------------

def main():
    print("d--- dollarizer")
    print("e--- eurizer")
    print("r--- replacer")
    print("w--- wonkey_text")
    print("n--- namedcelsius_to_fahrenheit")
    print("t--- namedage_in_days")
    print("i--- interest")
    print("j--- interest_two")
    choice=input("make choice ")
    if choice=="d":
        dollarizer()
    elif choice=="e":
        eurizer()
    elif choice=="r":
        replacer()
    elif choice=="w":
        wonkey_text()
    elif choice=="n":
        namedcelsius_to_fahrenheit()
    elif choice=="t":
        namedage_in_days()
    elif choice=="i":
        interest()
    elif choice=="j":
        goal_amount()

main()


        

#simple datatypes
#compound data types

transactions=[10.20,31.32,5]
def intro():#1
    print(" ")
    print("variables can be of datatype text numerical sequence boolean")
    x=5
    print(f"x=5 what is data type?  type(x) ", type(x))
    print("2:00 COMPOUND DATA TYPE list a compound variable all values into just one variable")
    print("for instance transactions is 10.20  31,32  5   transactions is variable datatype list/sequence ")
    print("holding three values so compound refers to many/ a lot" )
    y="lorraine"
    print(f"for instance y='lorraine' is variable/datatype SINGLE DATA TYPE containing ONE item ", y, type(y))
    print("transaction1=10.20 is a single datatype numeric float")
    print("transaction2=31.32 also float")
    print("transaction3=5 this is integer")
    print("these are different data types in this case float and integer ")
    print(" ")
    print("python therefore has a list")
    transactions=[10.20,31.32,5]
    print("transactions=[10.20,31.32,5]")
    print(f"transactions[0] gives the FIRST VALUE in the list ",transactions[0])
    
    print(f"SUM  print(sum(transactions))",sum(transactions))
    print(" ")




def append():
    print("3:30 transactions.append(7.82) at the end of list transactions")
    transactions.append(7.82)
    print("transactions.append() append is called a method ")
    print(f"compound datatype list contains now 10.20  31.32  5  7.82",(transactions))
    print(" ")
    
    
def pop():#3
    print("transactions.pop() last value will disappear from compound datatype list")
    print(f"list transactions contains ", transactions)
    transactions.pop()
    print(f"we now delete value 5 by transactions.pop() as you can see ", transactions)
    print(" ")
    print("indexing refers to the position of the value in a list  transactions[1] ")
    print(f"the second value transactions[1] is ",transactions[1])
    print(f"the last value transactions[-1] after deleting 5 is ",transactions[-1])
    print(f"len(transactions) gives length of list transactions",len(transactions))  
    print(" ")

def insert():#4
    print(transactions)
    print("transactions.insert(1,40.8) wil put 40.8 before 31.32 ")
    print(f"the second value of  10.20  31.32  5  is {transactions[1]}")
    print(" ")

def phonebook():#5
    print("telefoonboek phonebook={[]} is of type DICTIONARY another compound datatype")
    phonebook={"alice":"555-1234","bob":"555-1324","lodewijk":"555-6663"}
    print("alice 555-1234  bob 555-1324   lodewijk 555-6663")
    print("the number of bob is phonebook['bob']")
    print(f"het nummer van bob is {phonebook['bob']}")
    print(" ")

def main():
    print("chose ")
    print(" ")
    print("append 2")
    print("compound data type 1")
    print("dictionary 5")
    print("first value 1")
    print("insert 4")
    print("intro 1")
    print("last value 3")
    print("length 3")
    print("phonebook 5")
    print("pop 3")
    print("push 6")
    print("single data type 1")
    print("sum 1")
    print(" ")
        
    
    
    choice=input("make choice ")
    if choice=="1":
        print("you made choice 1 INTRO ")
        intro()
    elif choice=="2":
        print("you made choice 2 APPEND ")
        append()
    elif choice=="3":
        print("you made choice 3 POP ")
        pop()
    elif choice=="4":
       insert()
    elif choice=="5":
       phonebook()
    elif choice=="6":
       push()
    else:
         print("follow menu please")

main()
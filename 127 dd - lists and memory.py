#


lijst1=['appel','braam','pruim','abrikoos','kers']
lijst2=['schaefer','richter','canada','cake','vinegar']
lijst3=lijst2

def l():
    print(" ")


def seven(): # minute 7
    print(" 7:45")
    print("this is function zeven")
    a=str(input(f"give word "))
    b=str(input(f"give word "))
    print(f"you typed {a} and {b}")
    words1=[a,b]
    c=str(input(f"give word "))
    d=str(input(f"give word "))
    words2=[c,d]
    all_words=words1+words2
    print (all_words)
    main()

def eight():
    lijst=['appel','peer','pruim','abrikoos','kers', 'schaefer']
    print(lijst.count('peer'))
    print(lijst.insert(1, 'james'))
    main()


def nine():
    print("")
    print("appel  peer  pruim  abrikoos  kers")
    lijst=['appel','peer','pruim','abrikoos','kers']
    print(f"print(lijst[-1]) geeft kers",lijst[-1])
    print(f"print(lijst[0:2]) geeft appel peer",lijst[0:2]," dit is slicing")
    print(f"print(lijst[1:5:2]) geeft peer abrikoos",lijst[1:5:2]," dit is slicing met stappen van 2")
    print(f"print(lijst[::-1]) draait de lijst om ",lijst[::-1])
    print("lijst[1]='braam' vervangt peer door braam ")
    lijst[1]="braam"
    print(lijst)
    l()
    main()

def ten():
    print("this is function ten")
    print("de lijst is nu: ")
    lijst=['appel','braam','pruim','abrikoos','kers']
    print("appel  braam  pruim  abrikoos  kers")
    lijst.append("blanke vla")
    print("via append blanke vla   appel  braam  pruim  abrikoos  kers  blanke vla")
    lijst[5]="moorkop"
    print("lijst[5]='moorkop vervangt blanke vla   appel  braam  pruim  abrikoos  kers  blanke vla")
    print("we hebben nu: appel  braam  pruim  abrikoos  kers  moorkop")
    print("via append schaefer   vla   appel  braam  pruim  abrikoos  kers  moorkop  schaefer")
    lijst.append("schaefer")
    print("we hebben nu: appel  braam  pruim  abrikoos  kers  moorkop  schaefer")
    print("del lijst[5]  moorkop gaat eruit")
    del lijst[5]
    print(lijst)
    print("lijst.append('lane'")
    print("lijst.append('monika'")
    lijst.append('lane')
    lijst.append('monika')
    print(lijst)
    print("lijst.remove('appel')  verwijdert appel")
    lijst.remove('appel') 
    print(lijst)
    main()

def eleven():
    print("dit is de functie _10 ")
    print("lijst 1 krijgt alles van lijst 2 erbij door lijst1.extend ")
    lijst1.extend(lijst2)
    print(lijst1)
    print("lijst1.index shows position of canada ")
    print(f"position canada in lijst1",lijst1.index('canada'))
    print(f"lijst1.sort() sorteert lijst1 op alfabet ",lijst1.sort(), (lijst1))
    print(f"lijst 3 kopie van lijst2 gekopieerd van lijst 2 via lijst2=lijst3 ",(lijst3))

def eighteen():
    print("this is function eighteen")
    print("new list hups with numbers 1 2 3 4 5 6 7  8 9 10")
    hups=[1,2,3,4,5,6,7,8,9,10]
    minimum=min(hups)
    print(f"the smallest number is {minimum} ")
    
def nineteen():
    print("this is function nineteen  contains a task")
    print("list transactions = [10.1, 22.0, 32.2, 17.8, 55.0]")
    transactions = [10.1, 22.0, 32.2, 17.8, 55.0]
    minimum=min(transactions)
    maximum=max(transactions)
    total=sum(transactions)
    print(f"smallest transaction ", minimum)
    print(f"largest transaction ", maximum)
    print(f"total transactions ", total)
    print(" ")
    print("task: how could you achieve this result without min max sum functions? ")
    print("hint: using loops ")
    print("here we go ")
    
def task():
        
        
        transactions = [10.1, 22.0, 32.2, 17.8, 55.0]

        # Initialize variables
        smallest = float('inf')
        largest = float('-inf')
        total = 0

        # Loop through the list
        for transaction in transactions:
            # Update smallest
            if transaction < smallest:
                smallest = transaction
            # Update largest
            if transaction > largest:
                largest = transaction
            # Update total
            total += len(transaction)

        # Print the results
        print("Smallest number:", smallest)
        print("Largest number:", largest)
        print("Total number of transactions:", total)

        
        
        
                    
      


def twenty():
    l()
    print("this is function twenty ")
    print("fruits is a list with three fruits for fruit in fruits: print(fruit) ")
    fruits=['apple','banana','cherry']
    for fruit in fruits:
        print(fruit)
    apple= 'apple'
    print("apple in fruits?")
    print(f"how much characters has apple? ",len(apple))
    print(f"how much fruits are there in fruits? ",len(fruits))
    characters=list(apple)
    print(f"word apple into a list and printing the characters", characters)
    if apple in fruits:
        print(f"yes {apple} is in fruits ")
    else:
        print(f"no {apple} is NOT in fruits ")
    
    l()



def main():
    print("127 kies")
    print("name function arrived from minute of covering ")
    print(" ")
    print("slicing 9")
    print("7--- 7")
    print("8--- 8")
    print("9---9")
    print("10--- 10")
    print("11--- 11")
    print("18--- 18")
    print("19--- 19")
    print("task---task")
    print("20--- 20")
    
    choice=input("make choice ")
    if choice=="7":
        seven()
    elif choice=="8":
        eight()
    elif choice=="9":
       nine()
    elif choice=="10":
        ten()
    elif choice=="18":
        eighteen()
    elif choice=="19":
       nineteen()
    elif choice=="task":
       task()
    elif choice=="20":
       twenty()
    else:
         print("follow menu please")

main()
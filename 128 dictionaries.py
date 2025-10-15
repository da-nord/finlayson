import math

words={1:"soul",2:"mate",3:"trap", 4:"energy"}

def intro():
    print("lists have indexes ")
    print("dictionaries have keys ")
    dictionary={}

    d={'name':'jan','age':26}
    d['age']=27 #update
    print(d)

    d['address']='downtown'
    d['vase']=23
    print(d)
    e={
    "jan":{"city":"moskau","street":"moskau street","phone":123},
    "jane":{"city":"moskau","street":"moskau street","phone":123},
    "john":{"city":"moskau","street":"moskau street","phone":123},
    "joan":{"city":"moskau","street":"moskau street","phone":123}
    }
    print(f"print dictionary e ",(e))
    print(f'jan_street=e["jan"]["street"] jan is the key and street is key ', e["jan"]["street"])

    my_dict={'name': 'jack', 'age': 69}
    my_dict['address']='downtown'
    print(f"(my_dict) name jack age 69  address downtown", my_dict)

def two():
    print(" ")
    d={1:"soul",2:"mate",3:"trap", 4:"energy"}
    elim=d.pop(4)
    print(f"dictionary words 1 soul  2 mate  3 trap  4 energy ",d)
    print(f"elim is words.pop(4) that is key 4 and its value are deleted",elim)
    print(f"print new words",d)
    print(f"before we had stored value  of key 4 being energy in elim ",elim)
    print(" ")

def three():
   my_dict = {'name': 'jack', 'age': 69}
   # Check if all keys have a non-empty value
   all_have_values = all(my_dict[key] for key in my_dict)

   print(all_have_values)  # This will print True if all values are non-empty, otherwise False
    

def four():
     my_dict = {1: "cheese", 2: "saw", 3: "one", 4: "girl"}
     
     sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
     print(sorted_by_values)
     my_dict.clear()
     print(f"na my_dict.clear() ",my_dict)
     print("all keys of my_dic")
     print(my_dic.keys())
     print("both keys and values now ")
     print("squares={1:1, 3:9,5:25,7:49,9:81} ")
     print("for i in squares:")
     print("    'key:',i,'value',sqares[i])")
     squares={1:1, 3:9,5:25,7:49,9:81}
     for i in squares:
         print('key:',i,'value', squares[i])
     
  



    

def five():
    print(f"the LENGTH of dictionary dict ",words)
    print(len(words))
    print(" ")
    for key in words.keys():
        print(f"one of the detail fields is: {key}")
    for value in words.values():
        print(f"here are the values: ", {value})
    for i in words:
        print('key: ',i, 'value: ',words[i])
    print(f"print(5 in words) true or false? ",(5 in words))
    print(f"{words[3]} in words? print(3 in words) true or false? ",(3 in words))
    print(" ")

def exercise():
    print(" ")


def main():
    print("128 DICTIONARIES ")
    print("chose ")
    print(" ")
    print("1 add  ")
    print("4 clear  ")
    print("3 create ")
    print("2 dict ")
    print("1 intro ")
    print("5 keys values items ")
    print("5 length ")
    print("2 pop  ")
    print("4 sorted ")
    print(" ")
    

    
    choice=input("make choice ")
    if choice=="1":
        intro()
    elif choice=="2":
        two()
    elif choice=="3":
        three()
    elif choice=="3":
        sorted()
    elif choice=="4":
        four()
    elif choice=="5":
         five()
    else:
         print("follow menu please")

main()
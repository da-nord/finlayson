def one():
    print("LIST MANIPULATION")
    print("\n 1 create a list called fruits containing the following fruits: \n apple, banana, cherry, date \n add 'elderberry' to the end of the list \n remove 'banana' from the list \n sort the list in alphabetical'order \n print the list")
    print(" ")
    bunch = {}#initialize
    bunch=["apple","banana","cherry","date"]
    
    bunch.append("elderberry")
    print(f"elderberry is added",bunch)
    bunch.pop(1)
    print("banana popped bunch.pop('banana')")
    print(bunch)
    print("list bunch is sorted")
    bunch.sort()
    print(bunch)

def two():
    print("DICTIONARY BASICS")
    print("1")
    print("create a dictionary called student with the following key-value pairs")
    print("name: john doe")
    print("age: 25")
    print("major: computer science")
    dictwo = {'name': 'john doe', 'major': 'computer science'}
    print(dictwo)
    print("change the value of 'major' to 'electrical engineering'")
    dictwo['major']= 'electrical engineering' #update
    print(dictwo)
    print("add a new key-value pair: 'year' with a value of 'senior'")
    dictwo['year']='senior'
    print(dictwo)
    print("print out the keys in the dictionary")
    print("print out the values in the dictionary") 
    for key in dictwo.keys():
        print(f"here are the keys: {key}")
    for value in dictwo.values():
        print(f"here are the values: ", {value})  
    print(" ") 
    print("2") 
    print("change the value of 'major' to 'electrical engineering'")
    print(" ") 

def three():
    print("3")
    print("list of Dictionaries")
    print(" ")
    print("create a list of dictionaries")
    print(" where each dictionary represents a book and has the following keys:")
    print("title,author, and year")
    print("add at least 3 books to your list")
    print("print the title of the second book in the list")
    print("print the year the third book was published")
    print("iterate over the list and print out each book's title and author")
    # Creating a list of dictionaries
    dicthree = [
    {'title': 'simulacron-3', 'author': 'galouye', 'year': 1964},
    {'title': 'ze great reset', 'author': 'swap', 'year': 2030},
    {'title': 'have we won the war', 'author': 'rudolf', 'year': 1946}
    ]
    print(dicthree)

    # Print the title of the second book in the list
    print("Title of the second book:", dicthree[1]['title'])

    # Print the year the third book was published
    print("Year the third book was published:", dicthree[2]['year'])
    print(" ")

    # Iterate over the list and print each book's title and author
    for book in dicthree:
           print("Title:", book['title'], "| Author:", book['author'])


def four():
    print("1  Create a dictionary called courses")
    print("where the keys are the names of courses")
    print("(e.g., 'math', 'history', 'chemistry'")
    print("and the values are lists of student names enrolled in each course")
    print("Initialize every course with a list of some random names")
    print("of your choosing (ie, a list of strings")
    print(" ")
    courses = {
    "math": ["eustace", "henrik", "monika", "leslie"],
    "history": ["lorraine", "frank", "john", "anneke"],
    "chemistry": ["james", "eli", "alfred", "david"],
    "literature": ["dave", "steve", "heinrich", "joseph"]
    #"physics": ["hermann", "hilde", "miguel", "felipe"]
    }
    print(" ")
    print(courses)
    print(" ")
    print("Then complete the following using methods/functions:")
    print(" ")
    print("2  Add 5 students to 'math'")

    print(f"students of math are", courses['math'])
    print("adding 5 names to the math students ")
    courses['math'].extend(['alfred','eli','james','gerard','ernst'])
    print(courses['math'])

    print(" ")
    print("the history students are ",courses['history'])
    print("3  Remove the third student from 'history'")
    courses['history'].remove('john')
    print("the history students are now ",courses['history'])

    print(" ")
    print("4  Print out the students in 'chemistry'")
    print("courses['chemistry']  the chemistry students are ",courses['chemistry'])
    print(" ")
    print("5  Add a new course 'physics' with a list of 4 students")
    #"physics": ["hermann", "hilde", "miguel", "felipe"]
    # Adding a new course 'biology' with an empty list of students
    #courses['physics'] = []
    courses['physics'] = ['eustace', 'ezra','truus','gerda']
    # Alternatively, you can initialize it with some student names
    # courses["physics"] = ['eustace', 'ezra','truus','gerda']
    print("the physics students are now ",courses['physics'])

    # Print the updated dictionary to verify the changes
    print(courses['physics'])


def main():
    print("129 ")
    print("2 dictionary basics")
    print("1 list manipulation ")
    print("2 change value/update")
    print("3 list of dictionries")
    print("4 dictionary containing a list")


    

    
    choice=input("make choice ")
    if choice=="1":
        one()
    elif choice=="2":
        two()
    elif choice=="3":
        three()
    elif choice=="4":
        four()
    else:
         print("follow menu please")

main()
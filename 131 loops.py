def currency_converter():
    transactions=[1000.0,1002.0,1490.0,1780.0,1100.0,1200.0]
    #print(transactions[1])
    deserved=[] #empty list
    
    for t in transactions:
        d=t * 2.85
        deserved.append(d)
        print(deserved)
    print(" ")
    
def studenten():
    students_data=[
    {'name':'monika','grades':[85,88,92],'age':20},
    {'name':'alfred','grades':[90,87,80],'age':21},
    {'name':'james','grades':[78,80,82],'age':22}
    ]
    for student in students_data:
        total_grades=sum(student['grades'])
        number_of_grades=len(student['grades'])
        average_grade=total_grades / number_of_grades
        max_grade=max(student['grades'])
        
        #create a message about the student
        message=f"{student['name']} is {student['age']} years old "
        message+=f"They have an average score of {average_grade:.2f} and their highest score was {max_grade}\n"
        message+="Here are their grades: \\n"

        #adding nested loop to iterate over grades and create a
        for idx, grade in enumerate(student['grades']):
            message+=f"\\t- Test {idx+1}: {grade}\\n"

        #check if student is graduating (assuming average grade)
        if average_grade>85:
            message+=f"{student['name']} is graduating with honors\\n"
        else:
            message+=f"{student['name']} is graduating\\n"

        print(message)
    
def main():
    print("131 LOOPS menu: ")
    print("1 currency_converter")
    print("2 studenten")
    

    
    choice=input("make choice ")
    if choice=="1":
        currency_converter()
    elif choice=="2":
        studenten()

    else:
         print("follow menu please")

main()


#1 prompt user enter a sentence then print sentence uppercase
#https://www.geeksforgeeks.org/python/python-string-upper/
print("117 task 1")
jouwzin=input("give a sentence ")
jouwzin_u=jouwzin.upper()
print(f"your sentence in upper, {jouwzin_u}")


#2 prompt user enter paragraph then count number of words in paragraph
#https://www.geeksforgeeks.org/python/python-program-to-count-words-in-a-sentence/
# s = "Python is fun and versatile." # Counting words
# word_count = len(s.split())
# print(word_count)
print("117 task 2")
word_count = len(jouwzin.split())
print(f"your sentence has", word_count, " woorden")

#3 prompt user for string check if all characters are digits output true or false
#https://www.geeksforgeeks.org/python/python-check-if-string-contains-any-number/
#s = "abc123"
#res = any(char.isdigit() for char in s)
#if res:  # If 'res' is True, it means there is at least one digit in the string
#    print("Yes") 
#else:
#    print("No")
print("117 task 3")
jouwwoord=input("give a word ")
res=any(char.isdigit() for char in jouwwoord)
if res:
    print("er zitten cijfers in")
else:
    print("er zitten geen cijfers in")

#4 prompt user for string replace all occurrences of "a" with  "o"
#s = "Hello World! Hello Python!" 
#s1 = s.replace("Hello", "Hi") # Replace "Hello" with "Hi"
#print(s1)
print("117 task 4")
jouwwoord=input("give a word ")
jouwwoord_ao = jouwwoord.replace("a", "o") # replace a with o
print(jouwwoord_ao)

#5 prompt user enter full name John Dee then print their initials
#https://zzzcode.ai/python/code-generator?id=8f391cd5-bab0-40ba-9a4f-125c3a232709
print("117 task 5")
a = input("give your full name ") # Split the full name into parts
b = a.split()   
c = '.'.join(part[0].upper() for part in b)  # Extract the first letter of each part and join them
print((c),".")  # Output: J.D

#6 prompt the user for a string, then print its length
print("117 task 6")
a = input("give some word ")
print("the length of the word", str(a), " is",(len(a))," characters")
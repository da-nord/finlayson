def main():
    print("128 deep dive dictionaries EXERCISE ")
    print(" ")
    print("\n Write a program in Python that uses a dictionary\n to store how many times each item has been seen. \n The program should ask the user to enter \n a list of items one at a time \n When the user has finished entering items \n the program should display a count of \n how many times each item was entered.")
    print("")
    bunch = {}#initialize
    print(f"bunch is an empty container now ", bunch)
    
    
    print("\n you will be asked to give an item for bunch for instance sheep ")
    while True:
        
        item = input("Enter an item (or type 'stop' to finish): ")
        
        if item.lower() == 'stop':
            break
        
        # Increment the count for the item in the dictionary
        if item in bunch:
            bunch[item] += 1
        else:
            bunch[item] = 1
    
    print("\nCount of items entered: ")
    print(bunch)
    for item, count in bunch.items():
        print(f"{item}: {count}")

if __name__ == "__main__":
    main()

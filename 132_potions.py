def l():
    print(" ")

	



potions = {
    "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"],
    "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"],
    "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"]
}
l()

# Create a mapping of initials to potion names (keys) being the initial of the potions
initials_mapping = {potion[0:3].lower(): potion for potion in potions.keys()}

# Display the menu
print("Choose a potion by its initial:")
for potion in potions.keys():
    print(f"{potion[0:3].lower()}: {potion}")
    l()


# Get user input


#print(f"choose i for invisibility potion ingredients ",potions['Invisibility Potion'])
#potions['Invisibility Potion']=="i"
user_input = input("Enter the initial of the potion: ").lower()
l()

# Display ingredients if the input matches a potion
if user_input in initials_mapping:
    selected_potion = initials_mapping[user_input]
    ingredients = potions[selected_potion]
    print(f"Ingredients for {selected_potion}: {', '.join(ingredients)}")
    index=0
    print("answer with y or n ")
    l()
    while index<len(potions[selected_potion]):
        
        buy=input(f"do you want to buy {potions[selected_potion][index]}? ")
        if buy=="y": 
            print(f"you bought ", {potions[selected_potion][index]})
            index+=1  
            if index==len(potions[selected_potion]):
                print("all bought, good luck!")
                l()
        elif buy=="n":
            print("good buy ! good bye") 
        else:
            print("invalid input")
        
                    
                    
else:
    print("Invalid input. Please enter a valid initial.")

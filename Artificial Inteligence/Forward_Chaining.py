# initialize database
database = ["Croaks", "Eats Flies", "Shrimps", "Sings", "Sings"]
knownbase = ["Frog", "Canary", "Green", "Yellow"]

# Function to display available facts for selection
def display_facts():
    print("\n X is: \n1.Croacks \n2.Eats Flies \n3.Shrimps \n4.Sings", end=' ')
    print("\nSelect an option:", end=' ')


# main function
def main():
    print("*-----Forward Chaining-----*", end=' ')
    display_facts()


    # get user input and ensure its valid
    try:
        x = int(input())
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return
    
    # check if corresponds to a known fact about objects
    if x == 1 or x == 2:
        print("Chance of a frog", end=' ')
    elif x == 3 or x == 4:
        print("Chance of a canary", end=' ')
    else:
        print("Invalid option. Please select a number between 1 and 4.")
        return
    
    # if optionis valid, display more details
    if 1 <= x <= 4:
        print("\n X is:", database[x - 1])
        print("\nColor is: 1. Green 2. Yellow", end=' ')

        # Get the color input from the user
        try:
            k = int(input())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 2.")
            return
        
        if k == 1 and (x == 1 or x == 2):
            print("Yes, It is", knownbase[0], "And Color is", knownbase[2])
        elif k == 2 and (x == 3 or x == 4):
            print("Yes, It is", knownbase[1], "And Color is", knownbase[3])
        else:
            print("\n---Invalid Knowledge Database! Please select valid options")


if __name__ == "__main__":
    main()
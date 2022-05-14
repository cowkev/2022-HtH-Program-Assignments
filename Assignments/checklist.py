# creating empty list
checklist = [] 

# CREATE
def create(item):
    '''
    Create item code here

    this creates item in the list
    '''
    
    checklist.append(item)   

# READ
def read(index):
    ''' 
    read code here

    reads whatever you input into the list
    '''
   
    print(checklist[index])  


# UPDATE
def update(index, item):
    '''
    Update code here
    
    allows to update items currently in your list
    '''

    old = checklist[index]          
    checklist[index] = item

# DESTROY
def destroy(index):
    ''' add multi line comment to replace multiple single line comments '''

    removed = checklist[index]      #removes item in your list

    # Destroy code here
    checklist.pop(index)


# SEE ALL ITEMS
def all_items():

    items = []

    for element in checklist:
        print(element)
        items.append(element)
    
    return items
# USER INPUT FUNCTION
def user_input(prompt):

    entry = input(prompt)

    return entry
# USER CHOICE FUNCTI
def user_choice():

    running = True 

    while running:

        choice = user_input("Which function would you like to use? Enter C for create, R for read, U for update, D for destroy, and A to view all items in checklist. ")

        if choice == "C" or choice == "c":

            item = user_input("What item do you want to create? Type the name of the item. ")

            create(item)
        
            continue

        elif choice == "R" or choice == "r":

            index = user_input("What item do you wanto  read? Give a number for the position of the item. ")

            read(int(index))

            
            continue

        elif choice == "U" or choice == "u":

            update_index = user_input("What item do you want to update? Give the number for the position. ")

            new_item = user_input("what is your new item. ")

            update(int(update_index), new_item)

            
            continue

        elif choice == "D" or choice == "d":

            delete_index = user_input("What item do you want to delete? what is the number of the item. ")

            destroy(int(delete_index))
        
            continue
        elif choice == "A" or choice == "a":

            all_items()
            
            
            continue

        else:

            end = user_input("Quit? Enter Y or N. ")

            if end == "Y" or end == "y":
                print(checklist)
                editing = False

            else:
                
                continue

def test():

    # create("purple sox")
    # create("red cloak")
    # print(read(0))
    # print(read(1))
    # update(0, "purple socks")
    # destroy(1)
    # print(read(0))
    # print(all_items())
    # print(checked(0))
    # print(user_input("Is this working? "))
    user_choice()

user_choice()
#Control flow with dictionary:
d1 = {"k1": [1, 2, 3, (100, 300, 500)], "k2": [4, 5, 6, ["phone", "computer", "robot"]]}
var = eval(input("Enter a number:"))
if var in d1["k1"]:
    print("Found you!")
    num = input("Enter the number:")
    if eval(num) in d1["k2"][:3]:
        print("Found another one!")
        
        item = input("Enter an item:")
        
        if item in d1["k2"][3]:
            print("Got a ", item)
        else:
            print("Cant find a", item)
    else:
           print("Cant find anything")
            
elif var in d1["k1"][3]:
    print("Cant hide!")
else:
    print("Where are you?")


Enter a number:3
Found you!
Enter the number:4
Found another one!
Enter an item:car
Cant find a car


    


# In[7]:


d1 = {"k1": [1, 2, 3, (100, 300, 500)], "k2": [4, 5, 6, ["phone", "computer", "robot"]]}
var = eval(input("Enter a number:"))
if var in d1["k1"]:
    print("Found you!")
    num = input("Enter the number:")
    if eval(num) in d1["k2"][:3]:
        print("Found another one!")
        
        item = input("Enter an item:")
        
        if item in d1["k2"][3]:
            print("Got a ", item)
        else:
            print("Cant find a", item)
    else:
           print("Cant find anything")
            
elif var in d1["k1"][3]:
    print("Cant hide!")
else:
    print("Where are you?")
    

Enter a number:4
Where are you?

# In[8]:


#Control flow with only one if statement:
choose_dish = eval(input("Enter a number from 0 to 2:"))
pick_sauce = eval(input("Enter a number from 0 to 2:"))
if choose_dish > 2 and pick_sauce > 2 or choose_dish <3 and pick_sauce > 2 or choose_dish > 2 and pick_sauce < 3:
    None
else:
    cooked_pasta = ["hot", "cold", "over cooked"][choose_dish]
    sauce = ["spicy", "sweet", "savoury"][pick_sauce]
    
    print("My meal is", cooked_pasta, "and very", sauce, "!")




Enter a number from 0 to 2:0
Enter a number from 0 to 2:0
My meal is hot and very spicy !












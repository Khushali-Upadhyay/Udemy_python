try:
    print(10 + "90")
except:
    for i in range(3):
        print(i)
finally:
    print("End Code")


0
1
2
End Code

# In[2]:


try:
    print(10 + 90)
except:
    for i in range():
        print(i)
finally:
    print("End Code")

100
End Code



# In[3]:


try:
    print(10 + "90")
except:
    for i in range():
        print(i)
finally:
    print("End Code")


End Code
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-355f4dfeb1a8> in <module>
      1 try:
----> 2     print(10 + "90")
      3 except:

TypeError: unsupported operand type(s) for +: 'int' and 'str'

During handling of the above exception, another exception occurred:

TypeError                                 Traceback (most recent call last)
<ipython-input-3-355f4dfeb1a8> in <module>
      2     print(10 + "90")
      3 except:
----> 4     for i in range():
      5         print(i)
      6 finally:

TypeError: range expected 1 arguments, got 0


# In[5]:


def error(var):
    try:
        return 10 + var
    except:
        print("Type error found")
        print("String: "+ str(10) + " " + var)
    finally:
        print("End code!")
        
error(20)        


End code!
30



# In[6]:


def error(var):
    try:
        return 10 + var
    except:
        print("Type error found")
        print("String: "+ str(10) + " " + var)
    finally:
        print("End code!")
        
error("hello")   


Type error found
String: 10 hello
End code!

# In[7]:


def error(var):
    try:
        return 10 + var
    except:
        print("Type error found")
        print("String: "+ 10 + " " + var)
    finally:
        print("End code!")
        
error("hello")   


Type error found
End code!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-cf85b4ad517f> in error(var)
      2     try:
----> 3         return 10 + var
      4     except:

TypeError: unsupported operand type(s) for +: 'int' and 'str'

During handling of the above exception, another exception occurred:

TypeError                                 Traceback (most recent call last)
<ipython-input-7-cf85b4ad517f> in <module>
      8         print("End code!")
      9 
---> 10 error("hello")

<ipython-input-7-cf85b4ad517f> in error(var)
      4     except:
      5         print("Type error found")
----> 6         print("String: "+ 10 + " " + var)
      7     finally:
      8         print("End code!")

TypeError: can only concatenate str (not "int") to str

# In[8]:


def divide(x, y):
    try:
        res = x / y
        return res
    except ZerodivisionError:
        print("Division by zero is forbidden!")
    except TypeError:
        print("Cant be divided or divide by a string")
        
    finally:
        print("executing finally clause")
        
divide(10, 2)

executing finally clause
5.0



# In[10]:


def divide(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        print("Division by zero is forbidden!")
    except TypeError:
        print("Cant be divided or divide by a string")
        
    finally:
        print("executing finally clause")
        
divide(10, 0)

Division by zero is forbidden!
executing finally clause



# In[11]:


def divide(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        print("Division by zero is forbidden!")
    except TypeError:
        print("Cant be divided or divide by a string")
        
    finally:
        print("executing finally clause")
        
divide(10, "hello")

Cant be divided or divide by a string
executing finally clause


# In[ ]:


numbers  = 10, 20, 30, 40
numbers
while True:
    try:
        
        num = input("Enter an integer:")
        if eval(num) in numbers:
            print(num, "is in numbers")
            break
            
        elif num = "quit":
            break
            
        else:
            print("Not in numbers list")
            
    except:
        print("Try again, please")
        
    finally:
        print("End code")

Enter an integer: 11
Not in numbers list
End code!
Enter an interger: egregtre
Try again, please!
End code!
Enter an integer: 20
20 is in numbers
End code!



# In[ ]:


numbers  = 10, 20, 30, 40
numbers
while chance < 3:
    
while True:
    try:
        
        num = input("Enter an integer:")
        if eval(num) in numbers:
            print(num, "is in numbers")
            break
            
        elif num = "quit":
            break
            
        else:
            print("Not in numbers list")
            chance = chance + 1
    except:
        print("Try again, please")
        
#    finally:
#        print("End code")


Enter an integer: 11
Not in numbers list
End code!
Enter an integer:quit
End code!


Enter an integer: 8
Not in numbers list
Enter an integer: 3
Not in numbers list
Enter an integer: 6
Not in numbers list


# In[ ]:


def friends():
    animals = "bird", "cat", "dog", "cow", "lamb", "pig"
    try:
        num = int(eval(input("Please select a friend:")))
        
        try:
            if animals[num] in animals:
                print(animals[num])
        except:
                print("You did not choose a friend")
        finally:
                print("_______")
                for pet in animals:
                    print(pet)
                print("___END LOOP___")
        
        except:
            print("You did not enter a valid index")
            
friends()            

Please select a friend: 2.23432
dog
_____________________
bird
cat
dog
cow
lamb
pig
___End Loop____



# In[ ]:








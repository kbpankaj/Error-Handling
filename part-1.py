# Syntax Errors
# print("Hello")
# try:
#     print("Stmt-1")
#     print(10/0)
# except ZeroDivisionError:
#     print("Stmt-2")
#     print("Stmt-3")
#     print("Stmt-4")
#     print(10/2)
# print("baby")    

# try:
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))
#     print(x/y)
# except ZeroDivisionError as msg:
#     print("Cant divide with zero")    
# except ValueError:
#     print("Please provide int value")    

# try:
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))
#     print(x/y)
# except ArithmeticError as msg:
#     print("ArithmeticError")    
# except ZeroDivisionError:
#     print("ZeroDivisionError") 

# try: 
#     x =int(input("Enter First Number: "))
#     y =int(input("Enter Second Number: "))
#     print(x/y)
# except (ZeroDivisionError) as msg:
#     print(msg)    
# except (ValueError) as msg:
#     print(msg)   
# try :
#     print(10/0)
# except:
#     print("Default error")    
# except ZeroDivisionError:
#     print("zerodevision errror")    ERROR
# import os
# try :
#     print("Try")
#     os._exit(0)
# except ValueError:
#     print("except")
# finally:
#     print("finally")        



# try:
#     print("Outer try block")
#     print(10/0)
#     try:
#         print("inner try block")
#     except ZeroDivisionError:
#         print("inner except block")
#     finally:    
#         print("inner finally block")
# except:
#     print("outer except block")  
# finally:
#     print("outer finally block")       


class TooYoungException(Exception):
     def __init__(self,arg):
         self.msg = arg

class TooOldException(Exception):
     def __init__(self,arg):
         self.msg = arg         

age = int(input("Enter Age: "))
if age > 60 :
    raise TooYoungException("plz wait some more time yout will get best match soon ")  
elif age < 18 :
    raise TooOldException("No Channce")             
else:
    print("You will get match soon!!!")    
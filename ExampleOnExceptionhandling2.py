try:  #error code
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)
 
except ZeroDivisionError: #handling
    print("dont enter zero as denominator!!")
 
except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")
 
except NameError:
    print('enter only numbers for division')
except Exception:
    print('enter only numbers for division')
else:
    print("No exceptions")
 
finally:    #
    print("This will execute no matter what")#cleanup code
print("remaining 100 lines code ")


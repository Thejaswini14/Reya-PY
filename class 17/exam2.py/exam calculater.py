# 1.  def and return     →  define 4 functions: add, subtract, multiply, divide
# 2.  try/except         →  catch ZeroDivisionError and ValueError without crashing
# 3.  float(input())     →  to read numbers from the user
# 4.  return values      →  each function must return the correct result
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  4 functions defined — add, subtract, multiply, divide        →  10 marks
# 2.  Each function returns the correct result for any two numbers →  10 marks
# 3.  ZeroDivisionError caught and prints a clear message          →  10 marks
# 4.  ValueError caught for non-number input                       →   5 marks
# 5.  Program runs without any errors                              →   5 marks
# ========================================================================
# Total  →  40 marks



def add (x, y):
    return (x + y)
def subtract (x, y):
    return (x - y)
def multiply (x, y):
    return (x * y)
def divide (x, y):
    return (x / y)
try:
    print(add(1, 3))
    print(subtract(1, 3))
    print(multiply(1, 3))
    print(divide(1, 3))
except ZeroDivisionError:
    print("it a zero divison error")
except ValueError:
    print("ita a value error")  
      

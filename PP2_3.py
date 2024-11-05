

def q1(): 
  #Write Assignment code here
  word = input("In: ")
  if word.endswith("ife"):
    print("-ives")
  elif word.endswith("ey"):
    print("-eys")
  elif word.endswith("y"):
    print("-ies")
  else:
    print("-s")

def q2(): 
  #Write Assignment code here
  num=int(input("In: "))
  if num > 0:
    print(f"{num} is positive")
  else:
    print(f"{num} is negative")
  

def q3():
  #Write Assignment code here
  num=float(input("Input a number: "))
  num1=float(input("Input a number: "))
  num2=float(input("Input a number: "))
  if num <= 0 or num1 <= 0 or num2 <= 0:
    print("No Triangle")
  elif num == num1 == num2:
    print("Equilateral")
  elif num == num1 or num == num2 or num2 == num1:
    print("Isosceles")
  else:
    print("Scalene")



#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()

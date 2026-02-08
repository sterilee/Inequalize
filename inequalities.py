import math
print("Solve the inequality ax²+bx+c <=> 0")
a = float(input("What is the value of a?: "))
if a <= 0:
    print("Enter a positive value. Restart program"), exit ()
b = float(input("What is the value of b?: "))
c = float(input("What is the value of c?: "))
sign = input("What is the sign of the inequality? choose between <, <=, >, >=: ")

delta = pow(b, 2)-4*a*c

if sign == ">": 
    if delta < 0 : print("the inequality is true for every real number")
    exit()
    
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    if delta == 0:
      print(f"x =/= {x1}")
    exit()  
    if delta > 0:
        if x1 < x2 :
         print(f"x1 < {round(x1, 2)}, x2 > {round(x2, 2)}")
        if x1 > x2:
            print(f"x1 > {round(x1, 2)}, x2 < {round(x2, 2)}")
    
if sign == ">=":
    if delta <= 0 : print("the inequality is true for every real number")
    exit()
    
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    if delta > 0:
      print(f"x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
if sign == "<": 
    if delta <= 0 : print("the inequality is not satisfied for every real number")
    exit()
    
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    
    if delta > 0:
        if x1 < x2 :
         print(f"{x1}<x<{x2}")
        if x1 > x2:
            print(f"{x2}<x<{x1}")
if sign == "<=": 
    if delta < 0 : print("the inequality is true for every real number")
    exit()
    if delta == 0:
      print(f"x = {x1}")
      exit()
    
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    if delta > 0:
        if x1 < x2 :
          print(f"{x1}<=x<={x2}")
        if x2 < x1:
          print(f"{x2}<=x<={x1}")
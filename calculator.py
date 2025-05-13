n1 = float(input("Enter first number : "))
n2 = float(input("Enter second number: "))
op = input("Enter operator     : ")

if op=='+': print(F"{n1} + {n2} = {n1+n2}")
elif op=='-': print(F"{n1} - {n2} = {n1-n2}")       
elif op=='*': print(F"{n1} * {n2} = {n1*n2}")
elif op=='/' and n2==0: print("Error: Division by zero")
elif op=='/': print(F"{n1} / {n2} = {n1/n2}")
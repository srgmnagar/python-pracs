
lst=[int(input("Enter a number: ")) for i in range(5)]
sq=lambda x: x**2
sq_list=list(map(sq,lst))
print("The square of the numbers are: ",sq_list)
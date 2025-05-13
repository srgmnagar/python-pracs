dict={}
for i in range(3):
    key=input(f"Enter {i}th key")
    value=input(f"enetr value for {key}")
    dict[key]=value
print(dict)
print("keys are: ",dict.keys())
print("values are: ",dict.values())
search=input("Enter key to search")
if search in dict:
    print(f"value for {search} is {dict[search]}")
else:
    print(f"{search} not found")
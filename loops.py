# n = input("\nEnter your name \n")



list=["p1","p2","p3","p4"]
#for i in list:
#     print(i)

tuple=(1,2,)
# sum = 0
# for i in tuple:
#     sum+=i

# print(sum(tuple))

# for i in list:
#     for j in i:
#         print(j, sep="")
#     print("\n")

list=["Name","Phone","age","sal"]
for i in list:
    if(i=="Name"):
        name = input("Enter your first name \n")
        if(name.isalpha() and len(name)>0):
            print(f"Valid {i}\n")
        else:
            print(f"Not valid {i}")
    elif(i=="Phone"):
        phone = input("Enter your phone\n")
        if phone.isnumeric() and len(phone)==10:
            print(f"Valid {i}\n")
        else:
            print(f"Not valid {i}")
    elif(i=="age"):
        age = input("Enter your age\n")
        if age.isnumeric() and (int(age)>=20 and int(age)<=60):
            print(f"Valid {i}\n")
        else:
            print(f"Not valid {i}")
    elif(i=="sal"):
        sal = input("Enter your sal\n")
        if sal.isnumeric() and float(sal)>=10000.0:
            print(f"Valid {i}\n")
        else:
            print(f"Not valid {i}")

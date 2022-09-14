sal=float(input("\nEnter Salary\n"))
tenure=int(input("\nEnter tenure\n"))
gross=0
if(tenure>=10):
    gross=sal+(0.15*sal)
elif(tenure>=5):
    gross=sal+(0.1*sal)
elif(tenure>=3):
    gross=sal+(0.05*sal)
else:
    print("Employee is not eligible for bonus\n")
    gross=sal
print("Employee's total sal = ", gross)

import mariadb
conn = mariadb.connect(
    user="root",
    password="560096",
    host="localhost",
    port = 3306,
    database = "python_test",
)
cur= conn.cursor()
name=input("enter your name : ")
while len(name)==0 or name.isalpha()== False:
    name=input("Enter Valid Name : ")
    
phone=input("Enter phone Number : ")
while len(phone)!=10 or phone.isnumeric()==False:
    phone=input("Enter Valid Telephone Number : ")

age=input("Enter Your Age : ")
while len(age)==0 or age.isnumeric()==False or int(age)<20 or int(age)>100:
    age=(input("Enter Valid Age : "))
         
sal=input("Enter your salary : ")
while len(sal)==0 or sal.isnumeric()==False or int(sal)<0 :
    sal=input("Enter Valid salary: ")
    
city=input("Enter your city: ")
while city.isalpha()==False or len(city)==0:
    city=input("Enter Valid City name: ")
    
dept=input("Enter Your Department: ")
while len(dept)==0 or dept.isalpha()==False:
    dept=input("Enter Valid Department: ")

# print("\nName:", name)
# print("Phone:", phone)
# print("Age:", age)
# print("Sal:", sal)
# print("City:", city)
# print("Dept:", dept)

try:
    cur.execute("create table emp (name varchar(255), phone varchar(10), age int, sal int, city varchar(255), dept varchar(255));")
except Exception as y:
    print(y)
query = """insert into emp(name,phone,age,sal,city,dept) values(%s,%s,%d,%d,%s,%s)"""
record = (name,phone,int(age),int(sal),city,dept)
cur.execute(query,record)
cur.execute("select name, phone, age, sal,city,dept from emp;")
for (name,phone,age,sal,city,dept) in cur:
    print("Name:", {name},"Phone:", {phone},"Age:", {age},"Salary:", {sal},"City:", {city},"Dept:", {dept})
    
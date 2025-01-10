from app1.models import Employee
from django.db.models import Avg

# exec(open(r'E:\python  class new\python pratice b12\Django_framework\first_project\app1\db_shell.py').read())

# all_emps = Employee.objects.all()

# print(all_emps)

# for emp in all_emps:
#     print(emp.__dict__)

# for single read
# try:
#     emp = Employee.objects.get(id=4)
#     print(emp)
# except Employee.DoesNotExist:
#     print("empoyee with gien id doesnot exist in database")

# create
# 1st way:
# emp = Employee(
#     name="D", email="d@gmil.com", mobile_num=1234567, designation="Tester", salary=78651,
# )
# emp.save()

# # 2nd way:
# Employee.objects.create(name="E", email="e@gmil.com", mobile_num=2134567, designation="fullstack developer", salary=98651,)

# # update
# try:
#     emp_obj = Employee.objects.get(id=1)
#     emp_obj.salary = 4567
#     emp_obj.save()
# except Employee.DoesNotExist:
#     print("empoyee with gien id doesnot exist in database")

# multiple update
# try:
#     emp_obj = Employee.objects.get(id=1)
#     emp_obj.salary = 987410
#     emp_obj.email = "aa@gmail.com"
#     emp_obj.save()
# except Employee.DoesNotExist:
#     print("empoyee with gien id doesnot exist in database")

# delete
# try:
#     emp_obj = Employee.objects.get(id=5)
#     emp_obj.delete()
# except Employee.DoesNotExist:
#     print("empoyee with gien id doesnot exist in database")


# emp = Employee.objects.filter(email = "b@gmail.com")
# print(emp)     #op:<QuerySet [<Employee: B>]>

# emp = Employee.objects.filter(email = "a@gmail.com")
# print(emp)    #<QuerySet []>      not available

# emp = Employee.objects.get(email = "a@gmail.com")
# print(emp)    #error

# emp = Employee.objects.filter(salary = 23000)
# print(emp)    #<QuerySet [<Employee: C>]>

# emp = Employee.objects.filter(designation__startswith = "p")   #2 underscore
# print(emp)    #<QuerySet [<Employee: B>]>

# emp = Employee.objects.filter(salary__gte = 4000)      #grater than equal to
# print(emp)

# employees = Employee.objects.filter(salary__gte=30000, salary__lte=60000)

# Retrieve employees in descending order of salary
# employees = Employee.objects.order_by("-salary")


#



# Update salary of a specific employee
# Employee.objects.filter(id=1).update(salary=60000)


# Increase salary by 10% for all employees

# from django.db.models import F
# Employee.objects.update(salary=F('salary') * 1.10)



# date multiple fields of an employee
# Employee.objects.filter(id=2).update(designation="Senior Developer", salary=80000)


# Calculate the average salary of all employees


# avg_salary = Employee.objects.aggregate(Avg('salary'))
# print(avg_salary)



# Count the total number of employees
# from django.db.models import Count
# total_employees = Employee.objects.aggregate(Count('id'))


#  imp asked in interview
# Retrieve the top 5 employees with the highest salary
top_employees = Employee.objects.order_by("-salary")[:]

all_emps = Employee.objects.all()

print(all_emps)
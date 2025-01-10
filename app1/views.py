from django.shortcuts import render,redirect


from .models import Employee


# Create your views here.

# business logic



def get_employees(request):    # select * from employees;
    all_emps = Employee.objects.all()  # Fetch data from database  using django ORM  queries
    print(all_emps)  # Debug: Print retrieved data in console
    return render(request=request, template_name="employee_f_get_employee.html", context={"emps": all_emps})



def create_employee(request):
    if request.method == "POST":
        print(request.POST)
        Employee.objects.create(name=request.POST.get("nm"), email=request.POST.get("em"), 
                                mobile_num=request.POST.get("mb"), 
                                designation=request.POST.get("desn"), 
                                salary=request.POST.get("sal"))
        return redirect("get_emps")

    elif request.method == "GET":
        return render(request,"create_employee.html")


def get_employee(request, eid):
    emp = Employee.objects.get(id = eid)
    return render(request,"create_employee.html",{"single_emp":emp})

    

# def update_employee(request):
#     pass


# def delete_employee(request):
#     pass


# pdb means python debuger and set trace means we are applying break 
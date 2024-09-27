from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def create_employee(request):
    if request.method == 'POST' :
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        else:
            print(form.errors)
    else:
        form = EmployeeForm()
        return render(request, 'employees/employee_form.html', {'form':form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html',{'employees': employees})

def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html',{'form': form})

def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST' :
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html',{'employee': employee})
    
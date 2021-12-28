from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistraion
from .models import User

# This function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
     fm = StudentRegistraion(request.POST)
     if fm.is_valid():
        #  fm.save()
        nm = fm.cleaned_data['name']
        em = fm.cleaned_data['email']
        pw = fm.cleaned_data['password']
        reg = User(name=nm, email=em, password=pw)
        reg.save()
        fm = StudentRegistraion()

    else:
     fm = StudentRegistraion()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This function will delete
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# This function will update
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistraion(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistraion(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})
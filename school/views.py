from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


# Create your views here.
def home_view(request):
    return render(request, 'school/home.html')


def student_reg_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            human = True
            form.save()
            return redirect(request.path_info)
    else:
        form = StudentForm()
    return render(request, 'school/student_reg.html', {'form': form})
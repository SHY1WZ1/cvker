from django.shortcuts import redirect, render

from cvkerapp.forms import CVForm
from cvkerapp.models import CV

# Create your views here.


def start_page(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new CV to the database
            return redirect('cv_success')  # Redirect to a success page or CV list
    else:
        form = CVForm()

    return render(request, 'start_page.html', {'form': form})

def cv_success(request):
    cv_list = CV.objects.all()
    return render(request, 'cv_success.html', {'cv_list': cv_list})
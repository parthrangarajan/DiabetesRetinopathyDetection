from django.shortcuts import render, redirect
from user.forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form  = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
        else:
            form = UserRegistrationForm()
        return render(request, 'register.html', {'form':form})
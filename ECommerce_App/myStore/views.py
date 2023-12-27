from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm

def streamlit_view(request):
    # Run the Streamlit app as a subprocess
    import subprocess
    subprocess.run(["streamlit", "run", "myStore/streamlit_ecommerce_app.py"])

    return HttpResponse()

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data (save user, etc.)
            # Add your registration logic here
            form.save()
    else:
        form = RegistrationForm()

    return render(request, 'login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process the form data (login user, etc.)
            # Add your login logic here
            form.save()
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
from django.shortcuts import render, redirect
from ..forms.auth import SignupForm
from django.contrib.auth import authenticate, login,logout


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to home page or dashboard
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})






def login_view(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            
            login(request,user)
            return redirect("home")
        else:
            error_message = 'Invalid phone number or password'
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
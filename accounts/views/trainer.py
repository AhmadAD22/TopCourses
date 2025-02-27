from django.shortcuts import render, redirect
from ..forms.trainer import SignupForm
from django.contrib.auth import authenticate, login,logout


def trainer_signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('trainer_main')  # Redirect to home page or dashboard
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})



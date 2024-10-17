# views.py
from django.shortcuts import render, redirect, get_object_or_404
from ..models import SessionRating
from ..forms.rating import SessionRatingForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')  
def add_session_rating(request, session_id):
    if request.method == 'POST':
        form = SessionRatingForm(request.POST)
        if form.is_valid():
            session_rating = form.save(commit=False)
            session_rating.student = request.user  # Assuming the user is logged in
            session_rating.session_id = session_id  # Set the session foreign key
            session_rating.save()
            return redirect('session_details', session_id=session_id)  # Redirect to session detail or another page
    else:
        form = SessionRatingForm()
    
    return render(request, 'sessions/add_session_rating.html', {'form': form})

def update_session_rating(request, rating_id):
    session_rating = get_object_or_404(SessionRating, id=rating_id)
    
    if request.method == 'POST':
        form = SessionRatingForm(request.POST, instance=session_rating)
        if form.is_valid():
            form.save()
            return redirect('session_details', session_id=session_rating.session_id)  # Redirect after update
    else:
        form = SessionRatingForm(instance=session_rating)
    
    return render(request, 'sessions/update_session_rating.html', {'form': form})

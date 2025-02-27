from django.shortcuts import render, redirect
from ..forms.evaluation import QuestionTemplateForm

def create_question_template(request):
    if request.method == 'POST':
        form = QuestionTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_template_list')  # Redirect to a list view or another page
    else:
        form = QuestionTemplateForm()
    return render(request, 'question_template_form.html', {'form': form})

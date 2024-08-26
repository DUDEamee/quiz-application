from django.shortcuts import render, redirect
from .models import Question,Choice,QuizAttempt
from django.contrib.auth.decorators import login_required
# Create your views here.

def quiz_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_choice = request.POST.get(str(question.id))
            if selected_choice:
                choice = Choice.objects.get(id=selected_choice)
                if choice.is_correct:
                    score += 1
                QuizAttempt.objects.create(user=request,question=question,selected_choice=choice)
        
        return render(request, 'quiz/result.html',{'score':score})
    return render(request ,'quiz/quiz.html',{'questions':questions})

                 

    
# quiz/views.py

from django.shortcuts import render
from .models import Question

def quiz_view(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        results = []
        score = 0
        unanswered = []

        for q in questions:
            user_answer = request.POST.get(f"question_{q.id}")
            if not user_answer:
                unanswered.append(q)
                continue

            is_correct = (user_answer.strip().upper() == q.correct_answer.upper())
            if is_correct:
                score += 1

            results.append({
                'question': q,
                'user_answer': user_answer,
                'is_correct': is_correct,
            })

        if unanswered:
            return render(request, 'quiz/quiz_form.html', {
                'questions': questions,
                'error': '모든 문항에 응답해야 합니다.'
            })

        return render(request, 'quiz/quiz_result.html', {
            'results': results,
            'score': score,
            'total': questions.count(),
        })

    return render(request, 'quiz/quiz_form.html', {'questions': questions})

from django.db import models

# quiz/models.py

from django.db import models

class Question(models.Model):
    text = models.TextField()  # 문제 내용
    explanation = models.TextField(blank=True)  # 해설
    correct_answer = models.CharField(max_length=10)    # 정답 ("O", "X")

    def __str__(self):
        return self.text[:50]

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
#     selected = models.CharField(max_length=200)  # 보기 텍스트 ("O", "X")
#     is_correct = models.BooleanField(default=False)  # 정답 여부

#     def __str__(self):
#         return f"{self.question} - {self.selected}"


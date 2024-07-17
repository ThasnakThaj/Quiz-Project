from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.BigIntegerField()
    start_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class Questions(models.Model):
    question = models.CharField(max_length=250)

    def __str__(self):
        return self.question

class Choices(models.Model):
    question = models.ForeignKey(
        Questions, related_name= "choices", # Reverse access name for choices of a question
        on_delete=models.CASCADE
    )
    choice = models.CharField(max_length=250)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice

class Exam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choices, on_delete=models.CASCADE)
    date = models.DateField()
    exam_start_datetime = models.DateTimeField()
    exam_end_datetime = models.DateTimeField()

class QuizzExam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    user_phone = models.BigIntegerField()
    question_id = models.IntegerField()
    question_name = models.CharField(max_length=250)
    selected_choice = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=200)
    is_answer_correct = models.BooleanField(default=False)
    choice_selected_time = models.DateTimeField()

class Results(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    user_phone = models.BigIntegerField()
    exam_start_datetime = models.DateTimeField()
    exam_end_datetime = models.DateTimeField()
    duration = models.IntegerField()
    no_of_questions_attended = models.IntegerField()
    correct_answers = models.IntegerField()
    wrong_answers = models.IntegerField()
    percentage = models.FloatField()
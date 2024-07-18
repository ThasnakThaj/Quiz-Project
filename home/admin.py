from django.contrib import admin
from home import models

# Register your models here.
admin.site.register(models.Questions)
admin.site.register(models.Choices)
admin.site.register(models.User)
admin.site.register(models.Exam)
admin.site.register(models.QuizzExam)
admin.site.register(models.Results)
admin.site.register(models.States)
admin.site.register(models.Districts)

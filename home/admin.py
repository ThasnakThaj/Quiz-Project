from django.contrib import admin
from home import models
import csv
from django.http import HttpResponse

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','if_view']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'start_time','company', 'type', 'district', 'state', 'ip_address']

class BgImageAdmin(admin.ModelAdmin):
    list_display = ['image','type']

class ChoicesAdmin(admin.ModelAdmin):
    list_display = ['question','choice', 'is_answer']

class QuizzExamAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_name', 'user_phone', 'question_id', 'question_name', 'selected_choice', 'correct_choice', 
                    'is_answer_correct', 'choice_selected_time']
    
class ResultsAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_name', 'ip_address', 'user_phone', 'user_company', 'user_type', 'user_district', 
                    'user_state', 'exam_start_datetime', 'exam_end_datetime', 'duration', 'no_of_questions_attended',
                    'correct_answers', 'wrong_answers', 'percentage']
    actions = ['export_results']

    def export_results(self, request, queryset):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="results.csv"'

        writer = csv.writer(response)
        # Write the header row
        writer.writerow(['User Name', 'User Phone', 'ip_address', 'User Company', 'User Type', 'User District',
                         'User State', 'Exam Start', 'Exam End', 'Duration', 'Questions Attended',
                         'Correct Answers', 'Wrong Answers', 'Percentage'])

        # Write data rows
        for result in queryset:
            writer.writerow([result.user_name, result.user_phone, result.ip_address, result.user_company, result.user_type,
                             result.user_district, result.user_state, result.exam_start_datetime,
                             result.exam_end_datetime, result.duration, result.no_of_questions_attended,
                             result.correct_answers, result.wrong_answers, result.percentage])

        return response

    export_results.short_description = 'Export Selected Results to CSV'


admin.site.register(models.Questions, QuestionAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.BgImage, BgImageAdmin)
admin.site.register(models.Choices, ChoicesAdmin)
admin.site.register(models.QuizzExam, QuizzExamAdmin)
admin.site.register(models.Results, ResultsAdmin)

# admin.site.register(models.Questions)
# admin.site.register(models.Choices)
# admin.site.register(models.User)
# admin.site.register(models.Exam)
# admin.site.register(models.QuizzExam)
# admin.site.register(models.Results)
admin.site.register(models.States)
admin.site.register(models.Districts)
# admin.site.register(models.BgImage)

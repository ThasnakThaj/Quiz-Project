from django.shortcuts import render, redirect
from theme_material_kit.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
import random
from django.contrib.auth import views as auth_views
#from django.shortcuts import render
from django.http import JsonResponse
from home import models
from datetime import datetime

# Create your views here.


# Authentication
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/sign-up.html', context)

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/sign-in.html'
  form_class = LoginForm
  success_url = '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')


# Pages
def index(request):
  # return render(request, 'pages/index.html')
  #return render(request, 'accounts/sign-in.html')
  message = ""
  msg_alert = False
  duplicate_checking = request.session.get('duplicate_check')
  if duplicate_checking:
    message = "The entered phone number has already used"
    msg_alert = True
    request.session['duplicate_check'] = False

  if request.method == 'POST':
      print("user")
      name = request.POST.get('name')
      phone = request.POST.get('phone')
      if models.User.objects.filter(phone_number=phone).exists():
        request.session['duplicate_check'] = True
        return redirect('index')
      else:
      # print("home name : ", user.name)
      # print("home phone : ", user.phone_number)
      # print("home Id: ", user.id)
        user = models.User.objects.create(name=name, phone_number=phone, start_time=datetime.now())
        request.session['User ID'] = user.id
        request.session['participant Name'] = user.name
        request.session['participant Phone number'] = user.phone_number
        # Optionally, you can log to a file
        # with open('log.txt', 'a') as f:
        #     f.write(f"Name: {name}, Phone: {phone}\n")
        
        # Return a JSON response (optional)
        return redirect('quiz_page')
  
  # Render the initial form if GET request
  return render(request, 'pages/quiz_home.html', {
                'msg_alert': msg_alert,
                'error_message': message
            })

def quiz_page(request):
  if 'shuffled_questions' not in request.session:
    all_questions = list(models.Questions.objects.all())
    random.shuffle(all_questions)
    request.session['shuffled_questions'] = [question.pk for question in all_questions]
    request.session['current_question_index'] = 0
    request.session['sequence_number'] = 1

  shuffled_questions = request.session['shuffled_questions']
  current_question_index = request.session['current_question_index']
  sequence_number = request.session['sequence_number']

  if current_question_index >= len(shuffled_questions):
      return redirect('quiz_results')  # No more questions, go to the results page

  current_question_id = shuffled_questions[current_question_index]
  question = models.Questions.objects.get(pk=current_question_id)
  choices = question.choices.all()

  if request.method == 'POST':
      user_id = request.session.get('User ID')
      users_name = request.session.get('participant Name')
      users_phone = request.session.get('participant Phone number')
      
      selected_choice_id = request.POST.get('choice')
      selected_choice = models.Choices.objects.get(pk=selected_choice_id)
      correct_choice = question.choices.filter(is_answer=True).first()

      user_obj = models.User.objects.get(id=user_id)
      models.QuizzExam.objects.create(
          user=user_obj, user_name=users_name, user_phone=users_phone, 
          question_id=question.id, question_name=question.question, 
          selected_choice=selected_choice.choice, correct_choice=correct_choice.choice, 
          is_answer_correct=(selected_choice == correct_choice), choice_selected_time=datetime.now()
      )

      request.session['current_question_index'] += 1
      request.session['sequence_number'] += 1

      if request.session['current_question_index'] >= len(shuffled_questions):
          exam_start_time = user_obj.start_time.replace(tzinfo=None)  # Convert to naive datetime
          end_time = datetime.now().replace(tzinfo=None)
          correct_answers_count = models.QuizzExam.objects.filter(user=user_obj, is_answer_correct=True).count()
          wrong_answers_count = models.QuizzExam.objects.filter(user=user_obj, is_answer_correct=False).count()
          duration_in_minutes = (end_time - exam_start_time).total_seconds()
          total_questions_count = models.Questions.objects.count()
          percent = (correct_answers_count * 100) / total_questions_count
          models.Results.objects.create(
              user=user_obj, user_name=users_name, user_phone=users_phone, 
              exam_start_datetime=exam_start_time, exam_end_datetime=end_time, 
              duration=duration_in_minutes, correct_answers=correct_answers_count, 
              wrong_answers=wrong_answers_count, percentage=percent
          )
          request.session.flush()  # Clear the session data
          return redirect('quiz_results')  # Redirect to the results page

      return redirect('quiz_page')  # Redirect to the same page to load the next question

  # Render the template with the current question and its choices
  return render(request, 'pages/quiz_data.html', {'question': question, 'choices': choices, 'sequence_number': sequence_number})
def quiz_page2(request):
  return render(request, 'pages/quiz_data2.html')

def quiz_results(request):
    # Logic to calculate and display results
    return render(request, 'pages/quiz_results.html')


# Sections
def presentation(request):
  return render(request, 'sections/presentation.html')
  
def page_header(request):
  return render(request, 'sections/page-sections/hero-sections.html')

def features(request):
  return render(request, 'sections/page-sections/features.html')

def navbars(request):
  return render(request, 'sections/navigation/navbars.html')

def nav_tabs(request):
  return render(request, 'sections/navigation/nav-tabs.html')

def pagination(request):
  return render(request, 'sections/navigation/pagination.html')

def forms(request):
  return render(request, 'sections/input-areas/forms.html')

def inputs(request):
  return render(request, 'sections/input-areas/inputs.html')

def avatars(request):
  return render(request, 'sections/elements/avatars.html')

def badges(request):
  return render(request, 'sections/elements/badges.html')

def breadcrumbs(request):
  return render(request, 'sections/elements/breadcrumbs.html')

def buttons(request):
  return render(request, 'sections/elements/buttons.html')

def dropdowns(request):
  return render(request, 'sections/elements/dropdowns.html')

def progress_bars(request):
  return render(request, 'sections/elements/progress-bars.html')

def toggles(request):
  return render(request, 'sections/elements/toggles.html')

def typography(request):
  return render(request, 'sections/elements/typography.html')

def alerts(request):
  return render(request, 'sections/attention-catchers/alerts.html')

def modals(request):
  return render(request, 'sections/attention-catchers/modals.html')

def tooltips(request):
  return render(request, 'sections/attention-catchers/tooltips-popovers.html')
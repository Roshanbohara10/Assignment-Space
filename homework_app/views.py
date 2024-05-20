from .models import *
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def dashboard(request):
    if request.user.is_superuser:
        student_group = Group.objects.get(name='Student')
        teacher_group = Group.objects.get(name='Teacher')
        students = User.objects.filter(groups=student_group)
        teachers = User.objects.filter(groups=teacher_group)
        context = {'students': students, 'teachers': teachers}
        return render(request, 'homework/dashboard.html', context)
    elif request.user.groups.filter(name='Teacher').exists():
        subject = request.user.teacher.subject
        homework = Homework.objects.filter(subject=subject).order_by('-id')
    elif request.user.groups.filter(name='Student').exists():
        homework = Homework.objects.filter(student=request.user).order_by('-id')
    else:
        homework = Homework.objects.all().order_by('-id')

    context = {'homeworks':homework}
    return render(request, 'homework/dashboard.html', context)

    # return render(request, 'homework/dashboard.html', context)


# def homework_create(request):
#     if request.method == 'POST':
#         form = HomeworkForm(request.POST, request.FILES, user=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = HomeworkForm(user=request.user)
#     return render(request, 'homework/add_homework.html', {'form': form})


@login_required
def homework_create(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST, request.FILES)
        if form.is_valid():
            print('i am called')
            homework = form.save(commit=False)
            homework.student = request.user
            homework.save()
            return redirect('/')
    else:
        form = HomeworkForm()
    return render(request, 'homework/add_homework.html', {'form': form})


@login_required
def homework_instance(request, id):
    homework = Homework.objects.get(id=id)
    existing_review = None
    
    # Check if there is an existing review for the homework
    try:
        existing_review_obj = HomeworkReview.objects.get(homework=homework)
        existing_review = existing_review_obj.review
    except HomeworkReview.DoesNotExist:
        existing_review_obj = False

    if request.user.groups.filter(name='Student').exists():
        if homework.status == 'Reviewed':
            homework.viewed = True
            homework.save()

    return render(request, 'homework/homework.html', {
        'homework': homework,
        'existing_review': existing_review
    })
# @login_required
# def review_homework(request, id):
#     homework = Homework.objects.get(id=id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.data['review']
#             HomeworkReview.objects.create(homework=homework, review=review)
#     form = ReviewForm()
#     return render(request, 'homework/review.html',{'homework':homework, 'form':form})


@login_required
def review_homework(request, id):
    homework = Homework.objects.get(id=id)
    existing_review = None
    
    # Check if there is an existing review for the homework
    try:
        existing_review_obj = HomeworkReview.objects.get(homework=homework)
        existing_review = existing_review_obj.review
    except HomeworkReview.DoesNotExist:
        existing_review_obj = False
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.cleaned_data['review']
            if existing_review_obj:
                # If an existing review exists, update it
                existing_review_obj.review = review
                existing_review_obj.save()
            else:
                HomeworkReview.objects.create(homework=homework, review=review)

            homework.status = 'Reviewed'
            homework.save()
            return redirect('/')
            # return redirect('review_homework', id=id)
    else:
        # Initialize the form with the existing review as the initial value
        form = ReviewForm(initial={'review': existing_review})
        if not homework.status == 'Reviewed':
            homework.status = 'Pending'
        homework.save()
    
    return render(request, 'homework/review.html', {
        'homework': homework,
        'form': form,
        'existing_review': existing_review
    })



@login_required
def delete_model_instance(request, id):
    try:
        instance = Homework.objects.get(id=id)
        instance.delete()
    except Homework.DoesNotExist:
        print("Object not found.")
    
    return redirect('/')


# @login_required
# def delete(request, model_name, id, redirect_url_name):
#     model = apps.get_model(app_label='hrms_app', model_name=model_name)
#     object_to_delete = get_object_or_404(model, id=id)
#     object_to_delete.delete()
#     return redirect(redirect_url_name)
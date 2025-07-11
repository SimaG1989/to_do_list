from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View

from .models import Task, User
from .forms import TaskForm, RegisterForm
from .Serializers import UserSerializer


@login_required
def task_list_view(request):
    tasks = Task.objects.filter(user_id=request.user).order_by('-id')

    status_filter = request.GET.get('status')
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    form = TaskForm()

    paginator = Paginator(tasks, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = request.user
            task.save()
            return redirect('task_list')

    return render(
        request,
        'to_do_app/task_list.html',
        {
            'form': form,
            'page_obj': page_obj,
            'selected_status': status_filter,
        },
    )


@login_required
def toggle_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user_id=request.user)
    if request.method == 'POST':
        checked = request.POST.get('completed_checkbox') == 'on'
        task.status = 'Completed' if checked else 'New'
        task.save()
    return redirect('task_list')


@login_required
def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user_id=request.user)
    task.delete()
    return redirect('task_list')


@login_required
def task_update_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user_id=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'to_do_app/task_update.html', {'form': form, 'task': task})


class RegisterFormView(APIView):
    authentication_classes = []  # отключаем требование авторизации
    permission_classes = []

    def get(self, request):
        form = RegisterForm()
        return render(request, 'to_do_app/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # хешируем пароль правильно
            user.save()
            return redirect('login')
        return render(request, 'to_do_app/register.html', {'form': form})


class LoginFormView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'to_do_app/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('task_list')
        return render(request, 'to_do_app/login.html', {'form': form})


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Home(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': f'Hello, {request.user.username}'}
        return Response(content)
@login_required
def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'to_do_app/task_detail.html', {'task': task})

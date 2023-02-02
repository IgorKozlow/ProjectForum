from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    important = {'Регистрация.': 'Регистрация.',
                 'Вход для пользователей.': 'Вход для пользователей.',
                 'Cоздать тему для обсуждения.': 'Создать тему для обсуждения.',
                 'Оставить свой комменатрий.': 'Оставить свой комменатрий.',
                 'Увидеть свою статистику.': 'Увидеть свою статистику.',
                 'И многое другое будет в следующих обновалениях!' : 'И многое другое будет в следующих обновалениях!',
                 }
    context = {'important' : important}
    return render(request, 'user/index.html', context=context)


def userRegistration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = UserRegistration()
    else:
        form = UserRegistration()
    return render(request, 'user/register.html', {'form': form, })


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('forum')
        else:
            return redirect('forum')
    else:
        return render(request, 'user/login.html', )


def userLogout(request):
    logout(request)
    return render(request, 'user/login.html')


def forum(request):
    important = {'Правило форума.': 'Правило форума.',
                 'Задать вопрос? / FAQ': 'Задать вопрос? / FAQ',
                 'Нашли ошибку, БАГ ?': 'Нашли ошибку, БАГ ?',
                 'Обновление': 'Обновление',
                 'Как Создать Свою категорию': 'Как Создать Свою категорию',
                 }
    topic = Content.objects.all().order_by('-time_create')
    paginator = Paginator(topic, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        form = Addforms(request.POST)
        if form.is_valid():
            name_form = form.save(commit=False)
            name_form.author = request.user
            name_form.save()
            return redirect('forum')
    else:
        form = Addforms()
    context = {'topic': topic,
               'form': form,
               'page_obj': page_obj,
               'important': important,
               }
    return render(request, 'forum/index.html', context=context)


@login_required(login_url='login')
def profile(request, user_id):
    name = user_id
    topic = Content.objects.filter(author=name).order_by('-time_create')
    context = {'topic': topic,
               }
    return render(request, 'user/profile.html', context=context)


def thread(request, thread_id):
    return render(request, 'forum/thread.html')


def show_thread(request, thread_id):
    topic = Content.objects.get(slug=thread_id)
    comments = Comments.objects.filter(post=topic.id)
    print(topic.id, comments)
    if request.method == ('POST'):
        form = AddComment(request.POST)
        if form.is_valid():
            name_form = form.save(commit=False)
            name_form.post = Content.objects.get(title=topic.title)
            name_form.author = request.user
            name_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return
    else:
        form = AddComment()
    context = {'topic': topic,
               'form': form,
               'comments': comments,
               }
    return render(request, 'forum/thread.html', context=context)


def edit_page(request, thread_id):
    topic = Content.objects.get(slug=thread_id)
    form = Addforms(instance=topic)
    if request.method == 'POST':
        form = Addforms(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('forum')
    context = {'topic': topic,
               'form': form,
               }
    return render(request, 'forum/edit_page.html', context=context)


def delete_page(request, thread_id):
    topic = Content.objects.get(slug=thread_id)
    topic.delete()
    return redirect(reverse('forum'))


def delete_comment(request, comment_id):
    comments = Comments.objects.get(id=comment_id)
    comments.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_page(request):
    if request.method == 'POST':
        form = Addforms(request.POST)
        if form.is_valid():
            name_form = form.save(commit=False)
            name_form.author = request.user
            name_form.save()
            return redirect('forum')
    else:
        form = Addforms()
    return render(request, 'Forum/add_page.html', {'form': form})
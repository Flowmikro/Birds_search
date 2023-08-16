from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import AddBirdForm, BirdForm
from .services import _birds_list_db, _delete_bird_db, _get_info_bird_db, validate_form


@login_required(login_url='/')
def add_new_birds(request):
    """Добавление новой птицы в БД"""
    form = BirdForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if validate_form(form):
            return redirect('birds_list')
    return render(request, 'birds/add_birds.html', {'form': form})


@login_required(login_url='/')
def birds_list(request):
    """Вывод список птиц"""
    birds = _birds_list_db()
    return render(request, 'birds/birds_list.html', {'birds': birds})


@login_required(login_url='/')
def bird_detail(request, pk):
    """Вывод подробной информации о птице"""
    data = _get_info_bird_db(pk)
    return render(request, 'birds/bird_detail.html', data)


@login_required(login_url='/')
def bird_post(request):
    """Добавление записи о птице"""
    form = AddBirdForm(request.POST or None)
    if request.method == 'POST':
        if validate_form(form):
            return redirect('birds_list')
    return render(request, 'birds/bird_post.html', {'form': form})


@login_required(login_url='/')
def delete_bird(request, pk):
    """Удаление птицы"""
    _delete_bird_db(pk)
    return redirect('birds_list')
